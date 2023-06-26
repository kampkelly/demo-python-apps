# simple flask app to receive image upload and and return a json response of the image and the prediction

from flask import Flask, request, jsonify

import os
from flask_cors import CORS
from fake_image_detection.index import predict

def create_app():
  app = Flask(__name__)
  CORS(app)

  @app.route('/predict/fake-image', methods=['POST'])
  # predict function above
  def predict_fake_image():
      #  call method
      print('request receiveds')
      f = request.files['file']
        # save the file to ./uploads
      basepath = os.path.dirname(__file__)
      file_path = os.path.join(
          basepath, 'uploads', f.filename)
      f.save(file_path)
      
      prediction = predict(file_path)

      response = {
          'prediction': {
              'image': file_path,
              # 'label': labels[np.argmax(preds)]
              'prediction': prediction
          }
      }
      
      # return data and 200 OK HTTP status code
      return jsonify(response)
    
  @app.route('/predict/test', methods=['POST'])
  # predict function above
  def tesr():
      #  call method
      print('request 2 receiveds')

      response = {
          'user': {
              'name': 'okay',
              # 'label': labels[np.argmax(preds)]
              'email': 'test@example.com'
          }
      }
      
      # return data and 200 OK HTTP status code
      return jsonify(response)


  return app

app = create_app()
