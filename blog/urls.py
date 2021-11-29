from django.urls import path
from . import views

urlpatterns = [
    #post_list se utiliza para obtener la vista a renderizar
    #el namee parameter: nombre de la URL
    path('',views.post_list,name="post_list"), 
    path('post/<int:pk>/', views.post_detail, name='post_detail') 
]
