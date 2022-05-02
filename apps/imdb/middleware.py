import logging
from datetime import datetime

from django.http import HttpResponse
from rest_framework import status

logger = logging.getLogger(__name__)


class IMDBMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        logger.info("BEFORE VIEW")

        response = self.get_response(request)

        logger.warning("AFTER VIEW")
        if request.GET.get("add_current_time"):
            response.headers["current_time"] = str(datetime.now())

        # Code to be executed for each request/response after
        # the view is called.

        return response
