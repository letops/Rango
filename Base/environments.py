from Base import models, forms, queries, serializers


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
        if self.action == "signup":
            self.model = 'RangoUser'
            self.data_model = models.RangoUser
            self.form = forms.RangoUserSignForm
            self.template = 'signup.html'
            self.action_completed_urlname = 'home'

        if self.action == 'list_users':
            self.model = 'RangoUser'
            self.data_model = models.RangoUser
            self.template = 'lists.html'
            self.function = queries.UsersListQuery

        if self.action == "change_user":
            self.model = 'RangoUser'
            self.data_model = models.RangoUser
            self.form = forms.RangoUserProfileForm
            self.template = 'profile.html'
            self.action_completed_urlname = 'home'
