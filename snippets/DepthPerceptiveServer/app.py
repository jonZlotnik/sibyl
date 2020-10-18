import os
from flask import Flask, request

app = Flask(__name__)


l_image_counter = 1
r_image_counter = 1

@app.route('/submit-right-picture', methods = ['POST'])
def upload_right_pic():
   img_data = request.data
   global r_image_counter
   with open("pairs/right_"+format(r_image_counter, '02')+".jpeg", "wb") as f:
      f.write(img_data)
   r_image_counter += 1
   return "success"

@app.route('/submit-left-picture', methods = ['POST'])
def upload_left_pic():
   img_data = request.data
   global l_image_counter
   with open("pairs/left_"+format(l_image_counter, '02')+".jpeg", "wb") as f:
      f.write(img_data)
   l_image_counter += 1
   return "success"