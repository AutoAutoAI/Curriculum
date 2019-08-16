# Program an Autonomous Car using Computer Vision and Neural Networks

Learn how to use Computer Vision and Neural Networks to drive your autonomous car around a track. This project requires an AutoAuto Car, which can be purchased [here](https://www.autoauto.ai/).

### Step 1: Access your Jupyter Server

We'll heavily use Jupyter for this project. The first step now is to get access to the Jupyter server that is running on your device. To do that, go to your [device page](https://labs.autoauto.ai/autopair/) and click the yellow `i` button to see your device's "Info for Advanced Users". The modal that pops up will contain a link to your device's Jupyter server, and it will show you the password to access it (you can copy-paste that password).

### Step 2: Obtain command-line access

After Jupyter opens in a new tab in your browser, and after you enter the password successfully, you now need to get command-line access to your device. In the top-right of the Jupyter tab, click the dropdown-menu that says "New", then click "Terminal". This opens another tab giving you command-line access to your device.

### Step 3: Try a pre-trained Neural Network model

This repo has a pre-trained Neural Network model saved in the file name `model_01.hdf5`. It was trained on ~8,000 data points to drive around a track at the AutoAuto headquarters (image below).

<img src="https://static.autoauto.ai/uploads/2702760e8fc348b795ac597fa376f0ca.JPG" alt="AutoAuto headquarters Car-on-track" width="200"/>

**Very Important:** One of the key facts about Machine Learning is that is is hard! Why is it hard? Well, one reason is that when you train a machine learning model to do a task (like drive a car around a track), the model will learn only what it can _from the data you provide it_. So, if you provide the car training data to drive around a certain track (like the one in the picture above), then the car will learn how to drive on tracks like _that one_. It will **not** learn how to drive on a _different_ track. Super lame, right? One key to success in machine learning is to have a **great** dataset to train your model. You want to have a dataset that represents _all_ the different things your model might encounter in the real world. Now, there are also some tricks we can do to make our datasets better (we'll discuss those in a later lesson), but for now here is the takeaway: the pre-trained network we provide here might not work on a track _you_ build at home (especially if your track is very different from ours). There is no harm in trying it, just keep this important fact in mind while you do. If this model doesn't work on your track, then we will teach you how to collect training data on your track and train your own machine learning model! Get excited!

Now that you've read the important note above, head over to your Jupyter session, and click on the notework named `Car-on-Track.ipynb`. (Do not open it in GitHub, you must open that file from inside the Jupyter session of your AutoAuto car.) Read through that notebook and execute the code. See if our pre-trained model works on your track!

### Step 4: Collect your own Training Dataset

From a Jupyter terminal session (like you used in Step 2), run the python script named `Data-Collector.py`, like this:

```bash
cd Car-On-Track
python Data-Collector.py
```

That starts the program that lets you drive your car around the track. Use the keys below to drive your car. Each time you press a key, you will collect one data point. You'll want to collect ~8,000 data points (at least, for _our_ track, that's what we needed!).

That program saves files into a folder named `data`. You'll use the files inside `data` in the next step.

### Step 5: Train your own Neural Network!

The notebook named `NN.ipynb` will train a new Neural Network model using the dataset your collected in the previous step. Open that notebook, and follow the instructions inside it.

**NOTE:** Running this on your AutoAuto device will be very slow! It is recommended that you run this notebook on a Desktop or Laptop computer instead. As such, you'll have to copy the files in the `data` folder off the device and onto your Desktop or Laptop so you can train the model there.

### Step 6: Test your Neural Network!

In the previous step, you trained your own Neural Network on your own dataset. Now you will use your model and see if it works! Modify the notebook named `Car-on-Track.ipynb` so that it loads your model, and try it out. Good luck!

## Resources for Future Enhancements

- https://github.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pi
- https://medium.com/nanonets/how-to-easily-detect-objects-with-deep-learning-on-raspberrypi-225f29635c74
- https://medium.com/nanonets/how-to-automate-surveillance-easily-with-deep-learning-4eb4fa0cd68d
- https://medium.com/nanonets/how-we-flew-a-drone-to-monitor-construction-projects-in-africa-using-deep-learning-b792f5c9c471
