import io
import json                    
import base64                  
import logging             
import numpy as np
from PIL import Image

from flask import Flask, request, jsonify, abort

app = Flask(__name__)          
app.logger.setLevel(logging.DEBUG)
  
  
@app.route("/test", methods=['POST'])
def test_method():         
    # print(request.json)
    if request.json:
        print('recieved')

    if not request.json or 'ImageData' not in request.json: 
        abort(400)

    print(request.json['Face_Id'])
             
    # get the base64 encoded string
    im_b64 = request.json['ImageData']
    # convert it into bytes  
    img_bytes = base64.b64decode(im_b64.encode('utf-8'))
    # convert bytes data to PIL Image object
    img = Image.open(io.BytesIO(img_bytes))
    img_a = img.save("image.jpg")
    print('Image recived check image_test.jpg')
    # PIL image object to numpy array
    # img_arr = np.asarray(img_a)      
    # print('img shape', img_arr.shape)
    # process your img_arr here    
    # access other keys of json
    # print(request.json['other_key'])

    # timetamp = request.json['timestamp']
    print("---------------------")
    print("JSON Data sent through POST request from pi")
    print("Timestamp:",request.json['Timestamp'],"Face_ID:",request.json['Face_Id'],"Device_Id:",request.json['Device_Id'])
    print('---------------------')

    return "recieved"
    
  
def run_server_api():
    app.run(host='0.0.0.0', port=8080)
  
  
if __name__ == "__main__":     
    run_server_api()