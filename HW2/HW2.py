from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.run('/')
def index()
    return render_template()







if __name__ == '__main__':
    app.run(debug=True)