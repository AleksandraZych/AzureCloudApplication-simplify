from flask import Flask, render_template
from mock import *
app = Flask(__name__)

@app.route("/")
def homepage():
	""" returns rendered homepage """
	# items = db_helper.fetch_todo()
	items = all_mock
	# files = os.listdir("app/uploads")
	#  ,, files=files
	return render_template("index.html", items=items)


if __name__ == '__main__':
	app.run()