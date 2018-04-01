# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# * Name: Yonghong Chen
# * Description: This program capture key from the login.html and display victim ip address and logged keys

import os
import base64
import cv2
from flask import Flask, jsonify, request, send_file, json

app = Flask(__name__)

keys = ""


@app.route('/')
def Welcome():
    return app.send_static_file('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    fileJson = request.get_json()
    head, imageData = fileJson['image'].split(',', 1)
    image = base64.decodestring(imageData)
    image = processImage(image)
    # print imageData
    # print file
    resultImageData = head + ',' + base64.encodestring(image)
    return jsonify(result=resultImageData)


def processImage(image):
    # try save image as a file
    with open("image.jpg", "wb") as fh:
        fh.write(image)
    return image


port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port), debug=True)
