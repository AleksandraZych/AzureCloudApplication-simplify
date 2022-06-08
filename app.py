from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
	""" returns rendered homepage """
	# items = db_helper.fetch_todo()
	# files = os.listdir("app/uploads")
	#  items=items,, files=files
	return render_template("index.html")
if __name__ == '__main__':
	app.run()