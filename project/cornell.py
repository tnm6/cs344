import sqlite3 as sql
import numpy as np
from keras.preprocessing.text import Tokenizer

NUM_WORDS = 10000

data = sql.connect("movie_lines.db")
cursor = data.cursor()

cursor.execute("SELECT line_text FROM lines")

# fetchall() always returns tuples, so keep only first index of each tuple
lines = [i[0] for i in cursor.fetchall()]
# print(lines[:10])

tokenizer = Tokenizer(num_words=NUM_WORDS)
tokenizer.fit_on_texts(lines)

lines_by_movie = []
cursor.execute("SELECT COUNT(movie_id) FROM movies")
for i in range(cursor.fetchone()[0]):
    cursor.execute("SELECT line_text FROM lines WHERE movie_id = {}".format(i))
    cur_lines = np.array(cursor.fetchall())[:,0]
    cur_sequence = tokenizer.texts_to_sequences(cur_lines)
    lines_by_movie.append(cur_sequence)
features = np.array(lines_by_movie)
# print(features[0][:10])
print(features.shape)

np.random.shuffle(features)
# train_features = 
