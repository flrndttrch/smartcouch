from tastypie import fields
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer

from lights.models import Lighting, LightingHistory


class LightingHistoryResource(ModelResource):
    lightings = fields.ToManyField('lights.api.LightingResource', 'lightings_set', related_name='lightings', blank=True,
                                   null=True, full=True)

    class Meta:
        queryset = LightingHistory.objects.all()
        resource_name = 'lightings_history'
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = Authentication()
        authorization = Authorization()
        serializer = Serializer(formats=['json', 'jsonp'])
        always_return_data = True


class LightingResource(ModelResource):
    history = fields.ForeignKey(LightingHistoryResource, 'history')

    class Meta:
        queryset = Lighting.objects.all()
        resource_name = 'lightings'
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = Authentication()
        authorization = Authorization()
        serializer = Serializer(formats=['json', 'jsonp'])
        always_return_data = True
