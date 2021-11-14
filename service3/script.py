from flask import Flask, flash, request, redirect, url_for, render_template, json
import psycopg2
from main import get_predictions
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = './data/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

conn = psycopg2.connect(database="postgres", user="postgres", password="pswd", host="service1", port="5432")
cur = conn.cursor()

@app.route("/", methods=['GET'])
def getdata():
    cur.execute("SELECT * from dataset;")
    data = {"data" : [{'word' : item[0], 'probability': item[1]} for item in cur]}
    response = app.response_class(
        response=json.dumps(data),
        mimetype='application/json'
    )
    return response

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            #filename = secure_filename(file.filename)
            filename = 'test.png'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file', name=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload image file with a handwritten word and after that go to /recognize </h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route("/recognize", methods=['GET'])
def get_recognized_text():
    (label, prob) = get_predictions(app.config['UPLOAD_FOLDER'] + 'test.png')
    cur.execute("INSERT INTO dataset (word, probability) VALUES (%s, %s)",(label[0], prob[0].astype(float)))
    conn.commit()
    return json.dumps("Return to '/' and see detected word"), 200, {'ContentType':'application/json'} 


@app.route("/<param>", methods=["GET"])
def getmassage(param):
    if param != "recognize" and param != "" and param != "upload":
        return "Not supported", 404


if __name__ == '__main__':
    app.run(debug=True)