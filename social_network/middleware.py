from .models import UserActivity
from django.middleware.common import MiddlewareMixin

class UserActivityMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            UserActivity.objects.update_or_create(
                user_name=request.user, defaults={'endpoint': request.path_info})
        return response
