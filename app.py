from flask import Flask, request, render_template 
app = Flask(__name__)

@app.route('/home')
def helloWorld():
  return "Hello World"

if __name__ == '__main__':
  app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
  app.run()
