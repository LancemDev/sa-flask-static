from flask import Flask, send_from_directory
import os

app = Flask(__name__)


# Configuration for static files directory
STATIC_FOLDER = os.path.join(os.getcwd(), 'api/static')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(STATIC_FOLDER, filename)

@app.route('/')
def home():
    return 'This is the static subdomain!'

@app.route('/about')
def about():
    return 'About'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)