from django.urls import path

from instagram.views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name='index')
]
