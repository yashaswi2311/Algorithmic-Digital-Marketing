# from helper import search_books, filter_list
from book_recommender import find_k_similar_books, book_lookup, get_top_books
from flask import Flask, render_template, request, jsonify, Response
import json

app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    # filtered_books = get_top_books(n=10)
    search_string = 'Star'
    filtered_books = book_lookup(search_string, n=10)
    return render_template('index.html', books = filtered_books)


@app.route('/search_book', methods=['GET'])
def search_book():
    # Get parameter from the URL
    search_string = request.args.get('search_field')  
    filtered_books = book_lookup(search_string, n=20)
    return render_template('index.html', books=filtered_books)


@app.route('/book_recommendations/<id_goodreads>')
def book_recommendations(id_goodreads):
    recommended_books = find_k_similar_books(goodreads_book_id=id_goodreads, n=20)
    return render_template('index.html', books=recommended_books)



@app.route('/topbooks.html', methods=['GET'])
def topbook():
    # Get parameter from the URL
    filtered_books = get_top_books(n=20)
    return render_template('topbooks.html', books=filtered_books) 

@app.route('/bookanalysis.html')
def bookanalysis():
    return render_template('bookanalysis.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug = True)