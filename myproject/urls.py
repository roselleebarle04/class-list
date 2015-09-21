"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from students import views

urlpatterns = [
	url(r'^$', views.list_students, name='list_students'),
	url(r'^add/', views.add_student, name='add_student'),
	url(r'^update/$', views.update_student, name='update_student'),
	url(r'^update/(?P<student_id>[0-9]+)/$', views.update_student, name='update_student'),
	url(r'^drop/(?P<student_id>[0-9]+)/$', views.drop_student, name='drop_student'),

	url(r'^admin/', include(admin.site.urls)),
]
