# The-book-hub

## About

'The Book Hub' is a Book recommendation system for all avid readers out there who are always on the look-out for their next book. It is overwhelming to choose your next book from a pool of millions with different authors and various genres available. This project aims to provide you with accurate recommendations for your next favorite book. The system recommends books to the user based on their recent read by using singular value decomposition by KNN approach on user-item sparse matrix.

The Goal of this project is to create a web app that helps the user find similar books of based on their preference with the help of search as well as recommendation algorithms. The website is also integrated with goodreads.com that provides the users with the book description, rating as well as user reviews. Users will have a ability to select their recommended book and buy it from Amazon Kindle

## Dataset

The dataset used is goodreads-10k dataset that contains 6 million ratings for ten thousand most popular books (https://github.com/zygmuntz/goodbooks-10k).

## Prerequisites

- python >= 3.6
- flask >= 10.12.0
- pandas >=1.0.3
- numpy >=1.18.3

## Installation steps

### Optional: Create virtual environment for python

```
pip install --user virtualenv
virtualenv env
source env/bin/activate
```

### Clone the repository and install required packages

```
git clone https://github.com/yashaswi2311/the-book-hub.git
cd the-book-hub
pip3 install -r requirements.txt
Run Python app.py on command line
```
