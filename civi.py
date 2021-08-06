from flask import Flask, render_template
from flask.helpers import url_for
import os


project=Flask(__name__)

pic_folder= os.path.join('static')
project.config['UPLOAD_FOLDER']=pic_folder

@project.route("/")

def enterance():
    pic1=os.path.join(project.config['UPLOAD_FOLDER'],'Hajar.png')
    return render_template("enterance.html", EnterImg=pic1)

@project.route("/contact/")
def contact():
    return render_template ("contact.html")

def read():
    img= open('Hajar.png','r')
    img.show()




project.run(debug=True)



