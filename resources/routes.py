from .user import UserRegister, UserLogin
from .template import UserTemplates


def initialize_routes(api):
    api.add_resource(UserRegister, '/register')
    api.add_resource(UserLogin, '/login')
    api.add_resource(UserTemplates, '/template', '/template/<template_id>')
