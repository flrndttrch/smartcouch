from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.constants import ALL
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer

from lights.models import Lighting, Type, Timer, Day


class UserResource(ModelResource):
    class Meta:
        resource_name = 'users'
        queryset = User.objects.all()
        allowed_methods = ['get']
        excludes = ['email', 'password', 'is_superuser']
        #authentication = OAuth20Authentication()
        authentication = BasicAuthentication()
        authorization = Authorization()
        filtering = {"username": ALL}

class TypeResource(ModelResource):
    class Meta:
        queryset = Type.objects.all()
        resource_name = 'types'
        allowed_methods = ['get', 'post', 'put', 'delete']
        # authentication = OAuth20Authentication()
        authentication = BasicAuthentication()
        authorization = Authorization()
        serializer = Serializer(formats=['json', 'jsonp'])
        always_return_data = True
        filtering = {"name": ALL}

class LightingResource(ModelResource):
    type = fields.ToOneField(TypeResource, 'type', full=True)
    user = fields.ToOneField(UserResource, 'user', full=True)

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

class TimerResource(ModelResource):
    lighting = fields.ToOneField(LightingResource, 'lighting', full=True)
    days = fields.ManyToManyField('lights.api.DayResource', 'days', full=True)

    class Meta:
        queryset = Timer.objects.all()
        resource_name = 'timers'
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = BasicAuthentication()
        authorization = Authorization()
        serializer = Serializer(formats=['json', 'jsonp'])
        always_return_data = True


class DayResource(ModelResource):
    class Meta:
        queryset = Day.objects.all()
        resource_name = 'days'
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = BasicAuthentication()
        authorization = Authorization()
        serializer = Serializer(formats=['json', 'jsonp'])
        always_return_data = True