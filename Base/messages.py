SUCCESS = 'Success!'
ERROR = 'Error'
WARNING = 'We are sorry'

TICKET = 'An error has occurred. Please contact the administrator for more information.'
NO_PERM = 'You do not have enough permissions to execute this action. If this is a mistake, please contact the administrator.'

errors_list = {
    'title': {
        '400': 'Bad Request',
        '401': 'Unauthorized',
        '403': 'Forbidden',
        '404': 'Not Found',
        '405': 'Method not allowed',
        '406': 'Not Acceptable',
        '409': 'Conflict',
        '415': 'Unsupported Media Type',
        '500': 'Internal Server Error',
        '503': 'Service Unavailable',
    },
    'body': {
        'no_action': 'We are sorry. You are trying to execute an unknown or prohibited action.',
        'bad_login': 'The user/password combination is invalid. Please try again.',
        }
}