from jupyterhub.auth import Authenticator
from tornado import gen
from traitlets import Dict, Unicode

class CustomAuthenticator(Authenticator):
    user_passwords = Dict(
        Unicode(),
        config=True,
        help="Dictionary of usernames and passwords"
    )

    @gen.coroutine
    def authenticate(self, handler, data):
        username = data['username']
        password = data['password']
        if self.user_passwords.get(username) == password:
            return username

        return None

c = get_config()

c.JupyterHub.authenticator_class = CustomAuthenticator

c.Authenticator.allowed_users = {
        'amir',
}
c.Authenticator.admin_users = {
        'amir',
}

c.CustomAuthenticator.user_passwords = {
        'amir': 'password', # your username and password
}