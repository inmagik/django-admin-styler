from .views import compile_view
from django.conf.urls import url


urlpatterns = [
    url(r'^compile_scss/(?P<path>.+)/$', compile_view, name="compile_scss")
]

