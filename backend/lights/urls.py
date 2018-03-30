from django.conf.urls import url, include
from tastypie.api import Api

from lights.api import LightingResource, UserResource

v1_api = Api(api_name='v1')
v1_api.register(LightingResource())
v1_api.register(UserResource())

urlpatterns = [
    url(r'^api/', include(v1_api.urls)),
    # url('', views.index, name='index'),
    # url('<int:lighting_id>/', views.detail, name='detail')
]