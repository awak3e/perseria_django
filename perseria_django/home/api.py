from tastypie.resources import ModelResource
from django.contrib.auth.models import User

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.get(username="awak3e")
        resource_name = 'user'