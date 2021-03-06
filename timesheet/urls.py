from django.conf.urls import patterns, include, url
from django.views.generic import DetailView
from activities.models import Activity
from activities import views
from leaves import views as leaves_views
from django.contrib.auth.decorators import login_required

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),

    url(r'^login/$', 'django.contrib.auth.views.login', name="login"),

    url(r'^password/$', 'django.contrib.auth.views.password_change', name="password_change"),

    url(r'^password/changed/$', 'django.contrib.auth.views.password_change_done', name="password_change_done"),

    url(r'^logout/$', views.logout_view, name="logout"),

    url(r'^reports/$', views.reports, name="reports"),

    url(r'^export/$', views.export, name="export"),

    url(r'^myreports/$', views.my_reports, name="my_reports"),

    url(r'^activity/edit/(?P<pk>\d+)', login_required(views.ActivityUpdate.as_view()),
                                       name="activity_edit"),

    url(r'^activity/delete/(?P<pk>\d+)', login_required(views.ActivityDelete.as_view()),
                                         name="activity_delete"),

    url(r'^all/activity/(?P<activity>\d+)/$', views.all_activities, name="all_activities"),

    url(r'^api/activities', views.api_activities, name="api_activities"),

    url(r'^api/categories', views.api_categories, name="api_categories"),

    url(r'^api/activity/(?P<activity_id>\d+)/$', views.api_activity, name="api_activity"),

    url(r'^redmine/$', views.redmine, name="redmine"),

    url(r'^leaves/$', leaves_views.index, name="leaves"),

    url(r'^admin/', include(admin.site.urls))
)
