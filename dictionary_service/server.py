#!flask/bin/python
from flask import Flask, jsonify, abort
from dictionary_reader import search

app = Flask(__name__)

@app.route('/dictionary/api/v1.0/words/<string:word>', methods=['GET'])
def getSentimentValue(word):
    if len(word.strip()) == 0: abort(404)
    return jsonify(search(word))

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Word cannot be empty'}), 404

if __name__ == '__main__':
    app.run(debug=True)