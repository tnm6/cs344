"""Class Module for Keras-friendly datasets from Cornell Movie-Dialogs Corpus

Based on SQLite conversion found here:
    https://www.kaggle.com/mrlarichards/cornell-movie-dialogs-corpus-sqlite
And overall implementation inspired by keras.datasets.imdb

For:    Final Project for CS-344: Artificial Intelligence,
        Prof. Keith VanderLinden, Calvin University
By:     Nathan Meyer (tnm6)
Date:   5/20/2020
"""

import sqlite3 as sql
import numpy as np
from keras.preprocessing.text import Tokenizer
from sklearn.preprocessing import LabelEncoder


class Cornell:

    def __init__(self):
        self.genre_index = {}   # later filled by load_data()

    def load_data(self, num_words=10000, path='movie_lines.db',
                  oov_token='?', seed=113, train_size=462):
        """Loads Cornell Movie-Dialogs Corpus dataset
        and returns it as Keras-friendly Numpy arrays.

        args
            num_words: maximum number of words to include in index,
                based on most frequent occurrence
            path: location of SQLite database to load in
            oov_token: which character to replace 'unknown' (i.e. out of index)
                words with
            seed: random seed for shuffling the datasets
            train_size: how many entries should be in the training dataset,
                with the rest being used for testing dataset
        
        returns
            Tuple of Numpy arrays:
                '(train_data, train_labels), (test_data, test_labels)'
        """
        db = sql.connect(path)
        cursor = db.cursor()
        tokenizer = Tokenizer(num_words=num_words, oov_token=oov_token)
        encoder = LabelEncoder()

        # Gather data
        cursor.execute("SELECT COUNT(movie_id) FROM movies")
        count = cursor.fetchone()[0]

        movie_lines = []    # list of lines per movie
        for i in range(count):
            cursor.execute(
                "SELECT line_text FROM lines WHERE movie_id = {}".format(i))
            lines = ""
            # Gather all movies' lines into one string
            lines = " ".join([line[0] for line in cursor.fetchall()])
            movie_lines.append(lines)

        tokenizer.fit_on_texts(movie_lines)
        data = np.array(tokenizer.texts_to_sequences(movie_lines))

        # Gather labels
        cursor.execute("SELECT name FROM genres")
        genre_names = np.array([genre[0] for genre in cursor.fetchall()])

        genre_ints = encoder.fit_transform(genre_names)

        for i in range(len(genre_names)):
            self.genre_index[genre_names[i]] = genre_ints[i]

        movie_genres = []   # list of genres per movie
        for i in range(count):
            cursor.execute("""
                SELECT genres.name
                FROM movies, genres, movie_genre_linking
                WHERE movies.movie_id = movie_genre_linking.movie_id
                AND genres.genre_id = movie_genre_linking.genre_id
                AND movies.movie_id = {}
                """.format(i))
            genres = [genre[0] for genre in cursor.fetchall()]
            movie_genres.append(genres)

        movie_genres_int = []   # list of encoded genres by movie
        for entry in movie_genres:
            int_encoded = []
            for genre in entry:
                int_encoded.append(self.genre_index[genre])
            movie_genres_int.append(int_encoded)

        labels = np.array(movie_genres_int)

        # Randomize data and labels
        # Based on keras.datasets.imdb implementation of shuffling
        np.random.seed(seed)
        indices = np.arange(len(data))
        np.random.shuffle(indices)
        data = data[indices]
        labels = labels[indices]

        train_data = data[:train_size]
        train_labels = labels[:train_size]
        test_data = data[train_size:]
        test_labels = labels[train_size:]

        return (train_data, train_labels), (test_data, test_labels)

    def get_genre_index(self):
        """Returns the dictionary mapping genres to genre indices.
        """
        return self.genre_index
