from flask import Flask
from flask_restful import Api

from controllers import dev_controller
from controllers import skill_controller

app = Flask(__name__)
api = Api(app)

api.add_resource(dev_controller.DevList, '/devs')
api.add_resource(dev_controller.Dev, '/devs/<int:id>')

api.add_resource(skill_controller.SkillList, '/skills')
api.add_resource(skill_controller.Skill, '/skills/<int:id>')


if __name__ == '__main__':
    app.run(debug=True)
