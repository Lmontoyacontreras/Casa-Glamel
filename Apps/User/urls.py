from django.conf.urls import url

from .views import login

urlpatterns = [
    url(r'^$', login, name='login')
]
