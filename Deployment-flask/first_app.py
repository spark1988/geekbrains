import numpy as np
from flask import Flask, request, jsonify, render_template
from joblib import load

app = Flask(__name__)

@app.route('/')
def check_luck():
    test_np_input = np.array([[30,20,20],[65,4,3], [55,40,30]]) 
    model = load('model.joblib')
    preds = model.predict(test_np_input)
    preds_as_str = str(preds)
    return preds_as_str
if __name__ == "__main__":
    app.run(debug=True)