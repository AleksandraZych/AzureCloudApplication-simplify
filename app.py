from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def homepage():
	""" returns rendered homepage """
	items = [
		{
			'id': '1',
			'task': 'Zdać',
			'status': 'In progress'
		},
		{
			'id': '2',
			'task': 'Chlać',
			'status': 'In progress'
		}

	]
	return render_template("index.html", items=items)

# @app.route("/delete/<int:task_id>", methods=['POST'])
# def delete(task_id):
# 	""" recieved post requests for entry delete """
#
# 	try:
# 		db_helper.remove_task_by_id(task_id)
# 		result = {'success': True, 'response': 'Removed task'}
# 	except:
# 		result = {'success': False, 'response': 'Something went wrong'}
#
# 	return jsonify(result)

if __name__ == '__main__':
	app.run()