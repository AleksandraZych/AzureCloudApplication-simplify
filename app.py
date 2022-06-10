from flask import Flask, render_template, jsonify, request
from database_helper import fetch_todo,update_task_entry, update_status_entry, insert_new_task, remove_task_by_id
app = Flask(__name__)
from my_own_logging import insert_log

@app.route("/")
def homepage():
	""" returns rendered homepage """
	items = fetch_todo()
	to_log = ', '.join(str(d) for d in items)
	insert_log('Found items in to do list ' + str(to_log))
	return render_template("index.html", items=items)

@app.route("/delete/<int:task_id>", methods=['POST'])
def delete(task_id):
	try:
		remove_task_by_id(task_id)
		result = {'success': True, 'response': f'Removed task{task_id}'}
	except:
		result = {'success': False, 'response': 'Something went wrong'}

	return jsonify(result)

@app.route("/create", methods=['POST'])
def create():
	data = request.get_json()
	insert_new_task(data['description'])
	result = {'success': True, 'response': 'Done created new task'}
	return jsonify(result)


if __name__ == '__main__':
	app.run()