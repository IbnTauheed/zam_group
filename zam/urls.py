from django.urls import path
from . import views
from .views import message_list
from .views import contact_us

urlpatterns = [
    path('', views.home, name='home'),
    path('past-work/', views.past_work, name='past_work'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_us, name='contact'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('messages/', message_list, name='message_list'),
]
