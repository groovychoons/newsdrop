
from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^$', views.register, name='news_display'),
    url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^categories/$', views.categories, name='categories'),


    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),



]

