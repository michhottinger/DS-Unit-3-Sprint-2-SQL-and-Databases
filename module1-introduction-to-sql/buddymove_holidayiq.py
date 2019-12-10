"""Unit 3 week 2 assignment 1 question 2 """

#imports
import pandas as pd
import sqlite3
from sqlalchemy import create_engine

url = 'https://archive.ics.uci.edu/ml/datasets/BuddyMove+Data+Set'
df = pd.dataframe(url)
#sql method
df.to_sql('User', con=engine)
engine.execute("SELECT * FROM User").fetchall()
