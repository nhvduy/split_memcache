import flask
from flask import request, send_file
from os import path
from mylibs.big_file import MyLib

lib = MyLib()
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Duy Nguyen Ha Vu</h1><p>This site is for Interview from Setel.</p>"

@app.route('/api/v1/resources/file', methods=['POST','GET'])
def api_id():
    if request.method == 'POST':
        if 'name' in request.form:
            name = request.form['name']
        else:
            return "Error: No file name provided."
        uploaded_file = request.files['file']
        file_obj = uploaded_file.stream
        res = lib.set_file(name, file_obj)
        return res

    if request.method == 'GET':
        if 'name' in request.args:
            name = request.args['name']
        else:
            return "Error: No file name provided."

        file_path = lib.get_file(name)
        if not path.exists(file_path):
            return "File does not exists."
        return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run()