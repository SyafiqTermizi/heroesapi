from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import path
from . import views


urlpatterns = [
    path('', views.HeroList.as_view()),
    path('detail/<int:pk>', views.HeroDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)