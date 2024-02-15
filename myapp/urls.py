from django.urls import path
from myapp import views
urlpatterns = [
    # path('',views.stdreg,name="hi"),
    path('',views.home,name="hi"),
    path('project/',views.project,name="helo"),
    path('clock/',views.clock,name="clock"),
    path('firework/',views.firework, name='firework'),
    path('qrcodemaker/',views.qrcodemaker, name='qrcodemaker'),
    path('home/',views.homea,name="hi"),



    


]