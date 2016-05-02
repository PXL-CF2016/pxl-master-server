from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'api/v1/weather/', views.weather_api_endpoint)
]
