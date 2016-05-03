from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^user_data/$', views.UserList.as_view()),
    url(r'^board_data_1/$', views.BoardList_1.as_view()),
    url(r'^board_data_2/$', views.BoardList_2.as_view()),
    url(r'^board_data_3/$', views.BoardList_3.as_view()),
    url(r'^authentication/$', views.LoginView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
