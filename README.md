# Iris Flower Classification

A well-understood project that helped me grasp some of the basics of Machine Learning. The project uses supervised learning to predict the type of flower.

*You can visit [this link](https://iris-flower-anantsinghcross.herokuapp.com/) to have a look at the website for this project.*

### Overview of what we have to do

* Loading the dataset
* Evaluating some algorithms
* Making some predictions

### Check your Libraries

You should have your libraries updated. You will need the following libraries:
* `numpy`
* `scipy`
* `pandas`
* `matplotlib`
* `sklearn`

### Steps to get it up and running

1. The *trainer.py* loads the dataset available within the library and fits the data in several different models.
The trained model is then pickled so as to make it easier to load at the time of prediction.

2. The *api.py* makes the server and runs as the backend program.
To run the *api.py* head to the command prompt and type `python api.py`.

3. Finally, go to http://localhost:8000/ to get your *index.html* running.

### What you should see

* **index.html**

![index.html](index.JPG)

* **predictPage.html**

![predictPage.html](predictPage.JPG)

### Brief of what's happening

* The *index.html* takes in values which are sent to the *api.py* running in the background.
* *api.py* loads the pickled model, predicts the iris flower using the supplied data and sends back the prediction by redirecting you to the prediction page.
