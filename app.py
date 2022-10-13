from flask import Flask, request, render_template
import os
ON_HEROKU = os.environ.get('ON_HEROKU')
app = Flask(__name__)


@app.route('/ner')
def getBirds():
  return "Hello World!"
  
  
  
if __name__ == '__main__':
  app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
  app.run() 
