from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view),
    path('create/',views.product_create_view,),
    path('read/',views.product_list_view),
    path('update/<int:product_id>/',views.product_update_view),
    path('delete/<int:id>/',views.product_del_view),
]
