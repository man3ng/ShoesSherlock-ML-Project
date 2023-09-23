from flask import Flask, request
app = Flask(__name__)
from flask import render_template
import os
from machinelearning import shoes_prediction
import PIL
from PIL import UnidentifiedImageError


@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/model")
def model():
    return render_template('model.html')

@app.route("/upload")
def upload():
    return render_template('upload.html')

@app.route('/upload_image', methods = ['POST'])  
def upload_image():
    try:  
        if request.method == 'POST':  
            f = request.files['file']
            f.save('/workspaces/shoesherlock-Tri-Kevin/static/userinput.jpg')  
            success_message = "File uploaded succcessfully!"
            user_img = "/workspaces/shoesherlock-Tri-Kevin/static/userinput.jpg"
            prediction = shoes_prediction(user_img)
            if prediction == "Nike":
                return render_template("nike.html", picture = user_img)
            elif prediction == "Adidas":
                return render_template("adidas.html", picture = user_img) 
        else:
            error_message = "Failed to upload file."
            return render_template("upload.html", message = error_message)
    except PIL.UnidentifiedImageError:
        empty_message = "Bad upload, try again."
        return render_template("upload.html", message = empty_message)

if __name__ == "__main__":
   os.system('gdown 1-c4HhyNewS-J5Ytp9pJYfiGlg3TyVcNW')
   app.run(host='0.0.0.0')