#James Moore
#SDEV220-50P 
#Moduel 4 Lab - Case Study - Python APIs

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# 1. THE MODEL: 'Book' primary structure
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publisher = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"{self.book_name} - {self.author}"

# Initialize the database 
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return 'Hello!'

# 2. READ: Returns all books in the database
@app.route('/books')
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {
            'id': book.id, 
            'book_name': book.book_name, 
            'author': book.author, 
            'publisher': book.publisher
        }
        output.append(book_data)
    return {"books": output}

# 3. READ: Get a specific book by the bookID
@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {
        "book_name": book.book_name, 
        "author": book.author, 
        "publisher": book.publisher
    }

# 4. CREATE: Add a new book to the database
@app.route('/books', methods=['POST'])
def add_book():
    book = Book(
        book_name=request.json['book_name'], 
        author=request.json['author'], 
        publisher=request.json['publisher']
    )
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

# 5. DELETE: Remove a book form the database
@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "yeet!"} # Keeping the video's humor

if __name__ == '__main__':
    app.run(debug=True)
