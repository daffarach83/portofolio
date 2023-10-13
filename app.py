import os
from os.path import join, dirname
from dotenv import load_dotenv

from flask import Flask, render_template, request

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
app = Flask(__name__)

IMG_FOLDER = os.path.join("static", "IMG")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hello', methods=['POST'])
def hello():
   path = request.form['path']
   image = [i for i in os.listdir('static/img') if i.endswith('.png', 'jpg')][0]
   return render_template('Image.html', user_image = image)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)