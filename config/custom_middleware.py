import logging


class CustomFormatter:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        logger = logging.getLogger('django.request')
        logger.info(f"{request.method} {request.path} {response.status_code} {request.user}")
        return response
