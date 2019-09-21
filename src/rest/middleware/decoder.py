from rest_framework.response import Response


class MyReqDecoder:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)

        return response

    def process_template_response(self, request, response):
        # if isinstance(response, Response):
        #     response.data['status'] = 'Xer'
        return response