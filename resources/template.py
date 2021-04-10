from flask import request, make_response
from flask_restful import Resource
from database.models import User, Template
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.models import Template


class UserTemplates(Resource):
    # insert new template into db; no template id needed
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        body = request.get_json()
        user = User.objects.get(id=user_id)
        template = Template(**body, added_by=user)
        template.save()
        user.update(push__templates=template)
        user.save()
        id = template.id
        return {'id': str(id)}, 200

    # update existing template; needs to have template id
    @jwt_required()
    def put(self, template_id):
        user_id = get_jwt_identity()
        template = Template.objects.get(id=template_id, added_by=user_id)
        body = request.get_json()
        Template.objects.get(id=template_id).update(**body)
        return {'output': 'success'}, 200

    @jwt_required()
    def get(self, template_id=None):
        # return all templates owned by user
        if template_id is None:
            user_id = get_jwt_identity()
            # to print all templates
            # templates = Template.objects().to_json()

            templates = []
            for template in Template.objects():
                if str(template.added_by.id) == user_id:
                    templates.append((template.to_json()))
            resp = make_response(str(templates))
            resp.headers['status'] = 200
            resp.headers['Content-Type'] = "application/json"
            return resp

        # return single template; has to be owned by user
        else:
            user_id = get_jwt_identity()
            template = Template.objects.get(
                id=template_id, added_by=user_id).to_json()
            resp = make_response(template)
            resp.headers['status'] = 200
            resp.headers['Content-Type'] = "application/json"
            return resp

    # delete single template
    @ jwt_required()
    def delete(self, template_id):
        user_id = get_jwt_identity()
        template = Template.objects.get(id=template_id, added_by=user_id)
        template.delete()
        return {'output': 'successfully deleted'}, 200
