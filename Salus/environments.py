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
        if self.action == 'list_passwords':
            self.model = 'Password'
            self.data_model = models.Password
            self.template = 'lists.html'
            self.function = queries.PasswordsListQuery