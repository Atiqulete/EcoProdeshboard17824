from django.urls import path
from adminpanel import views


urlpatterns = [
    path('adminpanel',views.index,name='admin'),
    path('login_page',views.login_page,name='login_page'),
    path('reg_page',views.reg_page,name='reg_page'),
    path('logout_page',views.logout_page,name='logout_page'),
    path('banner_page',views.banner,name='banner_page'),

    

]