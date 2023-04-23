# from flask import Flask, jsonify, request
# app = Flask(__name__)


# @app.route('/api/predict', methods=['POST'])
# def predict():
#     # # Load the JSON data from the request
#     # data = request.get_json()

#     # # Extract the values from the JSON data
#     # feature1 = data['feature1']
#     # feature2 = data['feature2']
#     # feature3 = data['feature3']

#     # # Load the trained model
#     # model = pd.read_pickle('model.pkl')

#     # # Make a prediction using the model
#     # features = np.array([feature1, feature2, feature3]).reshape(1, -1)
#     # prediction = model.predict(features)[0]

#     # # Return the prediction as a JSON response
#     # response = {'prediction': prediction}
#     # return jsonify(response)


# if __name__ == '__main__':
#     app.run(debug=True)