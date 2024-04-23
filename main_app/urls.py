
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tasks/', views.tasks_index, name='index'),
    path('tasks/<int:task_id>/', views.tasks_detail, name='detail'),
    path('tasks/create/', views.TaskCreate.as_view(), name='tasks_create'),
    path('tasks/<int:pk>/update/', views.TaskUpdate.as_view(), name='tasks_update'),
    path('tasks/<int:pk>/delete/', views.TaskDelete.as_view(), name='tasks_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('tasks/<int:task_id>/add_photo/', views.add_photo, name='add_photo'),
    path('featured_event/', views.featured_event, name='featured_event'),
    path('tasks/<int:task_id>/add_featured_event/', views.add_featured_event, name='add_featured_event'),
    path('events/', views.featured_event, name='events')
]

