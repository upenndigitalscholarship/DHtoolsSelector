from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.inquiry, name='inquiry'),
	url(r'^inquiry/(?P<id>[0-9]+)/$', views.page, name='page'),
	url(r'^mappingtool/(?P<id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^result',views.result, name='result'),
]
