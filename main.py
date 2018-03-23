from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

page_header = """
<!doctype html>
<html>
    <head>
        <title>Web Caesar</title>
    </head>
    <body>

"""
page_footer = """
    </body>
</html>
"""

form = """
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form id="caesar"method="POST">
            Rotate by:
            <input type="text" name="rot"/>
            <textarea name="text">{0}</textarea>
            <input type="submit"/>
        </form>
"""

@app.route("/", methods=["POST"])
def encrypt():
    input_rot = request.form['rot']
    input_text = request.form['text']
    message = rotate_string(input_text, int(input_rot))
    return page_header + form.format(message) + page_footer

@app.route("/")
def index():
    return page_header + form.format('') + page_footer

app.run()