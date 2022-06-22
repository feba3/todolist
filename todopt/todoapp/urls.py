from django.urls import path
from todoapp import views

urlpatterns=[
  path('',views.myfun,name='home'),
  path('update/<int:todo_id>/',views.update,name="update"),
  path('delete/<int:todo_id>/',views.deletePage, name='delete'),
 
  
]