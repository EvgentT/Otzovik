from flask import render_template, redirect, url_for
from . import app, db
from .forms import ReviewForm
from .models import  Review, Movie


@app.route("/")
def index():
    movies = Movie.query.order_by(Movie.id.desc()).all()
    return render_template('index.html',
                           movies= movies)


@app.route('/movie/<int:id>', methods=['GET', 'POST'])
def movie(id):
    movie = Movie.query.get(id)
    #if movie.reviews:
    #    avg_score = round(sum(review.score for review in movie.reviews) / len(movie.reviews), 2)
    #else:
    #    avg_score = 0
    form = ReviewForm(score=10)
    if form.validate_on_submit():
        review = Review()
        review.name = form.name.data
        review.text = form.text.data
        review.score = form.score.data
        review.movie_id = movie.id
        db.session.add(review)
        db.session.commit()
        return redirect(url_for('movie', id=movie.id))
    return render_template('movie.html',
                           movie=movie,
                           avg_score=0,
                           form=form)