from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^board_data/$', views.BoardList.as_view()),
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^registration/$', views.RegisterView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
