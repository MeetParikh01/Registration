from django.urls import path
from users.views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    path('', Index.as_view(), name='index'),
    path('registration/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': 'login'}, name='logout'),
    
]