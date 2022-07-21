import json

from flask import request
from flask_restful import Resource

dev_list = list()


class DevList(Resource):
    def get(self):
        return dev_list

    def post(self):
        data = json.loads(request.data)
        id = len(dev_list)
        data['id'] = id
        dev_list.append(data)
        return dev_list[id]


class Dev(Resource):
    def get(self, id):
        try:
            response = dev_list[id]
        except IndexError:
            message = f'Dev with id {id} not founded!'
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
        dev_list[id] = data
        return data

    def delete(self, id):
        data_removed = dev_list.pop(id)
        return data_removed
