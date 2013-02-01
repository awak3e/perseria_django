from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from django.contrib.auth.models import User
from tastypie.http import HttpUnauthorized, HttpForbidden
from django.conf.urls import url
from django.contrib.auth import authenticate, login, logout
from tastypie.utils import trailing_slash

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        allowed_methods = ['get', 'post']
        resource_name = 'user'
        excludes = ['is_superuser', 'password']
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()
        
    def override_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/login%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('login'), name="api_login"),
            url(r'^(?P<resource_name>%s)/logout%s$' %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('logout'), name='api_logout'),
            url(r"^(?P<resource_name>%s)/(?P<username>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
        ]
        
    def login(self, request, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not username or not password:
            return self.create_response(request, {
                'success': False,
                'reason': 'incorrect',
                }, HttpUnauthorized )

    def logout(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        if request.user and request.user.is_authenticated():
            logout(request)
            return self.create_response(request, { 'success': True })
        else:
            return self.create_response(request, { 'success': False }, HttpUnauthorized)