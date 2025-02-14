from django.urls import path
from . import views
urlpatterns = [
    path('signup', views.signup, name='accounts.signup'),
    path('login/', views.login, name='accounts.login'),
    path('logout/', views.logout, name='accounts.logout'),
    path('orders/', views.orders, name='accounts.orders'),
    path('changepassword', views.changepassword, name='accounts.changepassword'),
    path('changepasswordcomplete', views.changepasswordcomplete, name='accounts.changepasswordcomplete'),
]