from django.urls import path
from .views import TaskList, TaskDetails, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView
from .views import temp

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('tasks/', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetails.as_view(), name='task'),
    path('task/create/', temp, name='create'),
    path('task/update/<int:pk>/', TaskUpdate.as_view(), name='update'),
    path('task/delete/<int:pk>/', TaskDelete.as_view(), name='delete'),
]
