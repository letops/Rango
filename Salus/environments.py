from Salus import models, forms, queries, serializers


class Environment:

    def __init__(self, action):
        self.action = action
        self.model = None
        self.data_model = None
        self.form = None
        self.function = None
        self.template = None
        self.action_completed_urlname = None

        self.load_data()

    def load_data(self):
        if self.action == 'list_password':
            self.model = 'Password'
            self.data_model = models.Password
            self.template = 'lists.html'
            self.function = queries.PasswordsListQuery

        elif self.action == 'add_password' or self.action == 'change_password':
            self.model = 'Password'
            self.data_model = models.Password
            self.form = forms.PasswordForm
            self.template = 'gork_password.html'
            self.action_completed_urlname = 'list_password'