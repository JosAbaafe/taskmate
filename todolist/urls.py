from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.todolist,name='todolist'),
    path('complete/<int:id>', views.CompleteTask,name='complete_task'),
    path('pending/<int:id>', views.PendingTask,name='pending_task'),
    path('edit/<int:id>/',views.EditTask,name='edittask'),
    path('delete/<int:id>/',views.DeleteTask,name='deletetask'),
]
