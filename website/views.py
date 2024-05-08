from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json



from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user


from flask import Flask, request, render_template 
from PIL import Image, ImageDraw
from gradio_client import Client
from PIL import Image
import requests
from io import BytesIO
import os
views = Blueprint('views', __name__)

def image(i):
    client = Client("https://e78b5e7744275751ce.gradio.live/")
    result = client.predict(
        prompt = 'i',
        api_name="/predict"
    )
    print(result)
    save(result)


def save(result):
    output_directory = "C:/Users/crush/OneDrive/Desktop/repairing the project/Flask-Web-App-Tutorial-main/Flask-Web-App-Tutorial-main/website/static"
    with open(result, 'rb') as file:
        image_data = file.read()
    image = Image.open(BytesIO(image_data))
    output_path = os.path.join(output_directory, "output_image.png")
    image.save(output_path)
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == "POST":
        i = request.form.get("q") 
        image(i)
        print(i)
    return render_template("index.html")