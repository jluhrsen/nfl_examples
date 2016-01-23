__author__ = 'jamo'

class rest_response_validation(object):

    is_valid = False

    def __init__(self, response):
        if response.status_code != 200:
            raise ValueError('response code was not 200')
        elif response.content == '[]':
            raise Warning('response content was empty')
