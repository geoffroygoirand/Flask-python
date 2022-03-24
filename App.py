from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

def load_model(): 
    model = "model.py  

    with open(model.py, 'wb') as file:  
       pickle.dump(model, file)


@app.route('/')
def hello():
    return 'Hello, World!'
    
@app.route('/predict',methods=['POST'])
def predict():
    if flask.request.method == "POST":
        if flask.request.files.get("image"):
            # read the image in PIL format
            image = flask.request.files["image"].read()
           
            preds = model.predict(image)
            results = imagenet_utils.decode_predictions(preds)
            data["predictions"] = []

            # indicate that the request was a success
            data["success"] = True

    # return the data dictionary as a JSON response
    return flask.jsonify(data)
   
   
if __name__ == "__main__":
    app.run(debug=True)
