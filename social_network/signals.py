from django.core.signals import request_started
from django.dispatch import receiver
from .models import UserActivity


@receiver(request_started)
def some(sender, environ, **kwargs):
    """ Активность юзера """

    username = environ['USERNAME']
    path = environ['PATH_INFO']

    UserActivity.objects.update_or_create(
        user_name=username, defaults={'endpoint': path})
