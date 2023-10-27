from django.urls import path
from django.conf import settings
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.product_list , name='product_list'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]