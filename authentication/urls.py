from django.conf.urls import include, url
from django.contrib.auth import views

from . import views as authentication_views

password_reset_args =  {'template_name': 'authentication/password_reset_form.html',
    					'email_template_name':'authentication/password_reset_email.html', 
    					'post_reset_redirect': 'user:password_reset_done',
    					'current_app': 'user'}
reset_args = 	{	'template_name': 'authentication/password_reset_confirm.html',
    					'post_reset_redirect': 'user:password_reset_complete',
    					'current_app': 'user'}

urlpatterns = [
    url(r'^signup/$', authentication_views.signup, name='signup'),
    url(r'^login/$', views.login, {'template_name': 'authentication/login.html'}, name='login'),
    url(r'^logout/$', views.logout, {'template_name': 'authentication/logout.html'}, name='logout'),
    url(r'^profile/$', authentication_views.profile, name='profile'),
    url(r'^edit/$', authentication_views.edit, name='edit'),
    url(r'^passwordchange/$', authentication_views.passwordchange, name='passwordchange'),
    url(r'^password_reset/$', views.password_reset, password_reset_args, name='password_reset'),
    url(r'^password_reset/done/$', views.password_reset_done, {'template_name': 'authentication/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_confirm, reset_args, name='password_reset_confirm'),
    url(r'^reset/done/$', views.password_reset_complete,  {'template_name': 'authentication/password_reset_complete.html'}, name='password_reset_complete'),
]
