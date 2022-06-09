from flask import Flask, render_template, jsonify, request
from mock import all_logs
app = Flask(__name__)

@app.route("/")
def homepage():
	""" returns rendered homepage """
	items = all_logs
	return render_template("index.html", items=items)

@app.route("/delete/<int:task_id>", methods=['POST'])
def delete(task_id):
	try:
		# db_helper.remove_task_by_id(task_id)
		result = {'success': True, 'response': f'Removed task{task_id}'}
	except:
		result = {'success': False, 'response': 'Something went wrong'}

	return jsonify(result)

@app.route("/create", methods=['POST'])
def create():
	""" recieves post requests to add new task """
	data = request.get_json()
	# db_helper.insert_new_task(data['description'])
	result = {'success': True, 'response': 'Done created new task'}
	return jsonify(result)


if __name__ == '__main__':
	app.run()