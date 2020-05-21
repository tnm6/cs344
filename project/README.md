# Predicting Movie Genre From Only Its Dialog

For CS-344: Artificial Intelligence by Professor Keith VanderLinden, Calvin University.\
Project and report by Nathan Meyer.

This project is an extension of sorts of the ["Classifying movie reviews"](https://github.com/fchollet/deep-learning-with-python-notebooks/blob/master/3.5-classifying-movie-reviews.ipynb) exercise from François Chollet's Deep Learning with Python Notebooks textbook. In particular, instead of identifying whether a film's review is positive or negative, this machine learning model looks at a dataset of 617's movies dialog, [collected by Cornell University](https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html), and attempts to identify the genre(s) with which to categorize each movie. The model is trained on and makes predictions solely based upon an extended string of the entire movies' collected dialog.

## The Dataset

This project utilizes the Cornell Movie-Dialogs Corpus, but particularly the SQLite conversion by Lee Richards on Kaggle.

It can be downloaded from either of these sources:

- [My temporary Google Drive link](https://drive.google.com/open?id=1GELSM9urKIt8jBVVlRUIfXzoAv9kk3K5)
- [The Kaggle source (account required)](https://www.kaggle.com/mrlarichards/cornell-movie-dialogs-corpus-sqlite)

## Modules

Besides the final report Jupyter Notebook file, there is only one additional file:

- `cornell.py`, the module from which the dataset is loaded

All other modules are those which have been used in the course materials (Keras, Numpy, etc.).

## How to Run

- Download the dataset
  - By default, the code looks for it in this directory
  - Otherwise, the path must be passed in to the load_data() function from `cornell.py`
- Work through `report.ipynb` and run the cells in order