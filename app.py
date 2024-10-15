from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data
books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
]

# GET endpoint to retrieve all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# POST endpoint to add a new book
next_id = 3  # Initialize the next ID to be used

@app.route('/books', methods=['POST'])
def add_book():
    global next_id 
    new_book = request.json
    new_book["id"] = next_id  
    next_id += 1  
    books.append(new_book)
    return jsonify(new_book), 201

# PUT endpoint to update an existing book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book_data = request.json
    for book in books:
        if book['id'] == book_id:
            book.update(book_data)
            return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

# DELETE endpoint to delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return jsonify({"message": "Book deleted"})
    return jsonify({"message": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
