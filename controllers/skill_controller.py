import json

from flask import request
from flask_restful import Resource

skills = list()


class SkillList(Resource):
    def get(self):
        return skills

    def post(self):
        data = json.loads(request.data)
        id = len(skills)
        data['id'] = id
        skills.append(data)
        return skills[id]


class Skill(Resource):
    def get(self, id):
        try:
            response = skills[id]
        except IndexError:
            message = f'Skill with id {id} not founded!'
            response = {
                "status": "Error!",
                "message": message
            }
        except Exception:
            message = f'Unknown error!'
            response = {
                "status": "Error!",
                "message": message
            }
        return response

    def put(self, id):
        data = json.loads(request.data)
        skills[id]['skill'] = data['skill']
        return skills[id]

    def delete(self, id):
        data_removed = skills.pop(id)
        return data_removed
