from app.auth.v1.models.user_models import UserModels
from flask import request
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
parser = RequestParser()

parser.add_argument("username", type=str, required=True,
 help="Please input your name")
parser.add_argument("task", type=str, required=True,
 help="Please input your task")

class User(Resource):
    """
    User endpoints
    """

    def post(self):
        """
        Register a user endpoint
        """
        args = parser.parse_args()
        args = request.get_json()
        username = args["username"]
        task = args["task"]
        task_timer = args["task_timer"]
        break_timer = args["break_timer"]
        task_completed = args["task_completed"]

        newUser = UserModels(username, task, task_timer, break_timer, task_completed)
        newUser.save_user()

        return {
            "message": "TASK CREATED SUCCESFULLY",
            "user" : newUser.__dict__
        }, 201

    def get(self):
        pass