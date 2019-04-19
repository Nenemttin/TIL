from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),

    path('users/<str:username>/', views.user_detail, name='user_detail'),
    path('follow/<str:username>/', views.toggle_follow, name='toggle_follow'),
]