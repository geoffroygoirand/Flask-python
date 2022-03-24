from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
    
@app.route('/predict',methods=['POST'])
def predict():
   
   
if __name__ == "__main__":
    app.run(debug=True)
