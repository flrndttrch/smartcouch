from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer

from lights.models import Lighting


class UserResource(ModelResource):
    class Meta:
        resource_name = 'users'
        queryset = User.objects.all()
        allowed_methods = ['get']
        #authentication = OAuth20Authentication()
        authentication = BasicAuthentication()
        authorization = Authorization()


class LightingResource(ModelResource):
    user = fields.ToOneField(UserResource, 'user')
    class Meta:
        queryset = Lighting.objects.all()
        resource_name = 'lightings'
        allowed_methods = ['get', 'post', 'put', 'delete']
        #authentication = OAuth20Authentication()
        authentication = BasicAuthentication()
        authorization = Authorization()
        serializer = Serializer(formats=['json', 'jsonp'])
        always_return_data = True

    def hydrate(self, bundle, request=None):
        bundle.obj.user = bundle.request.user
        return bundle
