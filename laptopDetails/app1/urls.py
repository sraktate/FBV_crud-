from django.urls import path
from .import views


urlpatterns =[
    path('ho/', views.Homeview , name='home'),
    path('Lp-Reg/',views.laptopRegisterView,name='L-Register'),
    path('Lp-list/', views.laptopListView,name='L-list'),
    path('update-Lp-list/<int:id>',views.updateLpatopDetilas , name='updateList'),
    path('delete-Lp-list/<int:id>',views.deleteLaptopDetails , name='deleteList')

]