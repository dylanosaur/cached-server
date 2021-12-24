# from flask import Flask, render_template, jsonify
#
#
# def create_app():
#     app = Flask(__name__)
#
#     @app.route('/')
#     def home():
#         return render_template("index.html")
#
#     @app.route('/first')
#     def first():
#         return render_template("index.html")
#
#     @app.route('/first/second')
#     def second():
#         return render_template("index.html")
#
#     return app
#
#
# app = create_app()

from bottle import route, request, response, template, run
@route('/forum')
def display_forum():
    forum_id = request.query.id
    page = request.query.page or '1'
    return template('Forum ID: {{id}} (page {{page}})', id=forum_id, page=page)

run(host='0.0.0.0', port=5000, debug=True)