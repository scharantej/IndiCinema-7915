
# main.py
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import numpy as np

app = Flask(__name__)

# Sample data
movies = pd.DataFrame({
    'title': ['Sholay', 'Dilwale Dulhania Le Jayenge', '3 Idiots', 'Dangal', 'Baahubali 2: The Conclusion'],
    'genre': ['Action', 'Romance', 'Comedy', 'Drama', 'Action'],
    'year': [1975, 1995, 2009, 2016, 2017],
    'rating': [8.4, 8.3, 8.4, 8.3, 8.0]
})

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    genre = request.form.get('genre')
    start_year = int(request.form.get('start_year'))
    end_year = int(request.form.get('end_year'))

    filtered_movies = movies[(movies['genre'] == genre) & (movies['year'] >= start_year) & (movies['year'] <= end_year)]

    return render_template('results.html', movies=filtered_movies)


if __name__ == '__main__':
    app.run(debug=True)
