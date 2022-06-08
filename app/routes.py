""" Specifies routing for the application"""
import os

from flask import render_template, request, jsonify, flash, \
    url_for, redirect, abort, send_from_directory
from app import app
from app import database as db_helper

@app.route("/")
def homepage():
    """ returns rendered homepage """
    # items = db_helper.fetch_todo()
    files = os.listdir("app/uploads")
    #  items=items,
    return render_template("index.html", files=files)


# @app.route("/", methods=['POST'])
# def upload_file():
#         if 'file' not in request.files:
#             flash('No file part')
#             return jsonify({'success': False, 'response': 'No file in request'})
#
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit a empty part without filename
#         if file.filename != '':
#             file.save(os.path.join('app/uploads',file.filename))
#             return redirect(url_for('homepage'))
#         #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         else:
#             flash('No selected file')
#             return jsonify({'success': False, 'response': 'No filename'})
#
# @app.route('/uploads/<filename>')
# def upload(filename):
#     return send_from_directory('C:/Users/cp24/Desktop/todolist/flask-gcp-mysql-demo/app/uploads', filename)

#
# @app.route("/delete/<int:task_id>", methods=['POST'])
# def delete(task_id):
#     """ recieved post requests for entry delete """
#
#     try:
#         db_helper.remove_task_by_id(task_id)
#         result = {'success': True, 'response': 'Removed task'}
#     except:
#         result = {'success': False, 'response': 'Something went wrong'}
#
#     return jsonify(result)
#
#
# @app.route("/edit/<int:task_id>", methods=['POST'])
# def update(task_id):
#     """ recieved post requests for entry updates """
#
#     data = request.get_json()
#
#     try:
#         if "status" in data:
#             db_helper.update_status_entry(task_id, data["status"])
#             result = {'success': True, 'response': 'Status Updated'}
#         elif "description" in data:
#             db_helper.update_task_entry(task_id, data["description"])
#             result = {'success': True, 'response': 'Task Updated'}
#         else:
#             result = {'success': True, 'response': 'Nothing Updated'}
#     except:
#         result = {'success': False, 'response': 'Something went wrong'}
#
#     return jsonify(result)
#
#
# @app.route("/create", methods=['POST'])
# def create():
#     """ recieves post requests to add new task """
#     data = request.get_json()
#     db_helper.insert_new_task(data['description'])
#     result = {'success': True, 'response': 'Done'}
#     return jsonify(result)
#
#
