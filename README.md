# Iris Flower Classification

A well-understood project that helped me grasp some of the basics of Machine Learning

## Overview of what we have to do

* Loading the dataset
* Evaluating some algorithms
* Making some predictions

#### Check your Libraries

You should have your libraries updated. You will need the following libraries:
* `numpy`
* `scipy`
* `pandas`
* `matplotlib`
* `sklearn`

### Steps to get it up and running

1. The *trainer.py* loads the dataset available within the library and *fits* the data in several different models.
The trained model is then *pickled* so as to make it easier to load at the time of prediction.

2. The *api.py* makes the server and runs as the backend program.
To run the *api.py* head to the command prompt and type `python api.py`.

3. Finally, go to http://localhost:8000/ to get your *index.html* running.

### Brief of what's happening

* The *index.html* takes in values which are sent to the *api.py* running in the background.
* *api.py* loads the pickled model and sends back the prediction.

#### Note

* I'll definitely be improving the frontend as well as the backend for this project (2nd October '18) :D

#### Change Notes

* Improved Frontend. Totally ignore the *CSS* formatting in the `<style>` tags. (3rd October '18) 
