from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BoardList, LoginView, RegisterView
# from rest_framework.authtoken import views


urlpatterns = [
    url(r'^board_data/$', BoardList.as_view()),
    url(r'^login/$', LoginView.as_view()),
    url(r'^registration/$', RegisterView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
