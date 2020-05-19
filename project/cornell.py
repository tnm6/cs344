import sqlite3 as sql
import numpy as np

data = sql.connect("movie_lines.db")
cursor = data.cursor()

