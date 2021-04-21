#!flask/bin/python
from flask import Flask, jsonify, abort
from dictionary_reader import search
import sys
import pika
import logging
import platform

app = Flask(__name__)

@app.route('/dictionary/api/v1.0/words/<string:word>', methods=['GET'])
def getSentimentValue(word):
    logger = logging.getLogger('Dictionary Service')
    if len(word.strip()) == 0: abort(404)
    word_value = search(word)
    if word_value[0]["value"] == 'unknown':
        #send_to_unknown(word)
        word_value[0]["value"] = 0
    logger.info("DICTIONARY: word: " + word + " - hostname: " + platform.node())
    return jsonify(word_value)

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Word cannot be empty'}), 404

def send_to_unknown(word):
    message = word
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.17.0.5'))
    channel = connection.channel()
    channel.queue_declare(queue='unknown')
    channel.basic_publish(exchange='', routing_key='unknown', body=message)
    print(" [x] Sent " + message)
    connection.close()

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    app.run(host= '0.0.0.0', debug=True)