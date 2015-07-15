from django.conf.urls import url

from .views import login,Logout

urlpatterns = [
    url(r'^$', login, name='login'),
    url(r'^$', Logout, name='logout')
]
