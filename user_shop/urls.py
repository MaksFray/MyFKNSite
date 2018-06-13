from django.conf.urls import url
from user_shop import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'user_shop'


urlpatterns = [
               url(r'^home', views.home, name='home'),
               url(r'^profile/$', views.user_profile, name='profiler'),
               url(r'^profile/information$', views.magic, name='myinformation'),
               url(r'^userlist$', views.usrlist, name="userlist"),
               url(r'^registration/$', views.register_user, name="registration"),
               url(r'^registration/register_success/$', views.register_success, name="sreg"),
               url(r'^logout/$', views.logout_request, name="logout_request"),
               url(r'^login/$', views.login, name="login"),
               ]
