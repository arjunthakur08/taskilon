from django.conf.urls import url, include
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.urls import reverse_lazy
from . import views

app_name='accounts'
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^login/$', views.login_view, name='login'),
	url(r'^logout/$', views.logout_view, name='logout'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^profile/$', views.profile, name="profile"),
	url(r'^change-password/$', views.changePassword, name='changepwd'),
    url(r'^reset_password/$', views.CustomPasswordReset.as_view(), name='password_reset'),
	# url(r'^reset_password/$',
    #     PasswordResetView.as_view(template_name='accounts/password_reset_form.html', success_url=reverse_lazy('accounts:password_reset_done'), email_template_name='accounts/password_reset_email.html', subject_template_name='accounts/password_reset_subject.txt'),
    #     name='password_reset'),
	# url(r'^reset_password/done/$',
    #     PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
    #     name='password_reset_done'),
	url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html', success_url = reverse_lazy('accounts:password_reset_complete')),
        name='password_reset_confirm'),
	url(r'^reset/done/$',
        PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
        name='password_reset_complete'),
]
