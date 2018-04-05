from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import path
from . import views


urlpatterns = [
    path('heroes', views.HeroList.as_view()),
    path('heroes/<int:pk>', views.HeroDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)