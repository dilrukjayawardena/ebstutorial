from email.mime import application
from flask import Flask, render_template
import aws_controller

application = Flask(__name__)

@application.route('/')
def index():
    data=aws_controller.get_items()
    return render_template('index.html',films=data)

if __name__ == "__main__":
    application.run(debug=False,port=8000)