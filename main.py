from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, flash, jsonify, session, redirect, Markup
import sqlite3
import datetime
import os
import random

app = Flask(__name__)
app.config.from_object(__name__)

file = r'articles.csv'
df = pd.read_csv(file)

df1 = df.drop_duplicates(subset = ["title"])

top20 = df1.sort_values(by="claps", ascending=False).head(20)['title'].tolist()

def getRandomQuote():
	text = df['text'].unique().tolist()
	text = "\n".join(text)
	n_chars = len(text)
	r = random.randint(1, n_chars)
	return text[r:r + 250].split(' ', 1)[1]

@app.route("/")
def home():
	quote = getRandomQuote()
	return render_template("home.html", top20=top20, quote=quote)

if __name__ == "__main__":
	app.run()