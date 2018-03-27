from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie_oauth.authentication import OAuth20Authentication

from lights.models import Lighting, LightingHistory


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        allowed_methods = ['get']
        #authentication = OAuth20Authentication()
        authentication = BasicAuthentication
        authorization = Authorization()


class LightingResource(ModelResource):
    class Meta:
        queryset = Lighting.objects.all()
        resource_name = 'lightings'
        allowed_methods = ['get', 'post', 'put', 'delete']
        #authentication = OAuth20Authentication()
        authentication = BasicAuthentication
        authorization = Authorization()
        serializer = Serializer(formats=['json', 'jsonp'])
        always_return_data = True

class LightingHistoryResource(ModelResource):
    lighting = fields.ToOneField(LightingResource, 'lighting', blank=True,
                                 null=True, full=True)
    user = fields.ToOneField(UserResource, 'user')

    class Meta:
        queryset = LightingHistory.objects.all()
        resource_name = 'lighting_histories'
        allowed_methods = ['get', 'post', 'put', 'delete']
        #authentication = OAuth20Authentication()
        authentication = BasicAuthentication
        authorization = Authorization()
        serializer = Serializer(formats=['json', 'jsonp'])
        always_return_data = True
        ordering = ['activation_date']

    def hydrate_user(self, bundle, request=None):
        #TODO: Check if it works, otherwise change back to hydrate()
        bundle.obj.user = bundle.request.user
        return bundle.obj.user
