from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
	<head>
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
    	<form method = 'POST'>
        	Rotate by:
        	<input name="rot" type="text" value="0">
        	<textarea name="text" type="text">{0}</textarea>
        	<input type="submit">
    	</form>
	</body>
</html>
"""
@app.route("/", methods=['POST'])
def encrypt():
	rot = request.form['rot']
	text = request.form['text']

	rotation = int(rot)
	not_encrypt = str(text)

	encrypt_text = rotate_string(not_encrypt, rotation)

	return form.format(encrypt_text)


@app.route("/")
def index():
	return form.format('')

app.run()



