from django.conf.urls import url, include
from tastypie.api import Api

from lights import views
from lights.api import LightingResource, LightingHistoryResource

v1_api = Api(api_name='v1')
v1_api.register(LightingHistoryResource())
v1_api.register(LightingResource())

urlpatterns = [
    url(r'^api/', include(v1_api.urls)),
]