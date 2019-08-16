from car.motors import (
        set_steering,
        set_throttle,
        CAR_THROTTLE_FORWARD_SAFE_SPEED,
        CAR_THROTTLE_REVERSE_SAFE_SPEED,
)

from auto.camera import CameraRGB

from itertools import count
import numpy as np
import time
import os

import curses

from preprocessing import resize


SAVE_DIRECTORY = 'data'


def collect_one_point(camera, steering_angle, Xs, ys):
    frame = camera.capture()
    frame = resize(frame)
    set_steering(steering_angle)
    time.sleep(0.1)
    set_throttle(CAR_THROTTLE_FORWARD_SAFE_SPEED)
    time.sleep(0.2)
    set_throttle(0.0)
    Xs.append(frame)
    ys.append(steering_angle)


def reverse():
    set_throttle(CAR_THROTTLE_REVERSE_SAFE_SPEED)
    time.sleep(0.2)
    set_throttle(0.0)


def save_data(Xs, ys):
    os.makedirs(SAVE_DIRECTORY, exist_ok=True)
    for i in count():
        x_file = os.path.join(SAVE_DIRECTORY, "X{}.npy".format(i))
        y_file = os.path.join(SAVE_DIRECTORY, "y{}.npy".format(i))
        if not os.path.exists(x_file):
            break
    np.save(x_file, Xs)
    np.save(y_file, ys)


def main():
    camera = CameraRGB()

    screen = curses.initscr()  # get the curses screen window
    curses.noecho()            # turn off input echoing
    curses.cbreak()            # respond to keys immediately (don't wait for enter)
    screen.keypad(True)        # map arrow keys to special values

    screen.addstr(0, 0, "Press 'q' to save and quit.")
    screen.addstr(1, 0, "Collect data using arrow keys `left`, `right`, and `up`.")
    screen.addstr(2, 0, "For more detailed control, you can use the keys: a, s, d, f.")
    screen.addstr(5, 0, "We recommend collecting ~200 data points, then save & quit, then run again.")

    Xs = []
    ys = []

    key_map = {
        ord('a'): {'angle': +45.0, 'text': 'hard left '},
        ord('s'): {'angle': +25.0, 'text': 'soft left '},
        ord('d'): {'angle': -25.0, 'text': 'soft right'},
        ord('f'): {'angle': -45.0, 'text': 'hard right'},
        ord(' '): {'angle':   0.0, 'text': 'straight  '},

        curses.KEY_LEFT:  {'angle': +45.0, 'text': 'hard left '},
        curses.KEY_RIGHT: {'angle': -45.0, 'text': 'hard right'},
        curses.KEY_UP:    {'angle':   0.0, 'text': 'straight  '},
    }

    try:
        while True:
            screen.addstr(7, 0, "{} data points collected".format(len(Xs)))

            char = screen.getch()

            if char == ord('q'):
                break

            elif char == curses.KEY_DOWN:
                screen.addstr(9, 0, 'reverse   ')
                reverse()

            elif char in key_map:
                val = key_map[char]
                screen.addstr(9, 0, val['text'])
                collect_one_point(camera, val['angle'], Xs, ys)

            else:
                screen.addstr(9, 0, '??????????')

        if len(Xs) > 0:
            save_data(Xs, ys)

    finally:
        # Clean up the PTY
        curses.nocbreak();
        screen.keypad(0);
        curses.echo()
        curses.endwin()


if __name__ == '__main__':
    main()

