
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
	return "Hello, World!"
if __name__ == '__main__':
	app.run(host='192.168.137.10', port=5000, debug=True)
