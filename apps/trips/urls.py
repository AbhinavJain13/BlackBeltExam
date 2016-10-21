from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^showaddpage$', views.showaddpage, name = 'showaddpage'),
    url(r'^add$', views.add, name = 'add')
#     url(r'^success$', views.success, name = 'success'),
#     url(r'^logout$', views.logout, name = 'logout')
]
