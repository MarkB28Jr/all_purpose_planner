
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
<<<<<<< HEAD
    path('featured_event/', views.featured_event, name='featured_event'),
    path('tasks/<int:task_id>/add_featured_event/', views.add_featured_event, name='add_featured_event'),
    path('events/', views.featured_event, name='events')
=======

    path('featuredevents/', views.FeaturedEventList.as_view(), name='featuredevents_index'),
    path('featuredevents/<int:pk>/', views.FeaturedEventDetail.as_view(), name='featuredevents_detail'),
    path('featuredevents/create/', views.FeaturedEventCreate.as_view(), name='featuredevents_create'),
    path('featuredevents/<int:pk>/update/', views.FeaturedEventUpdate.as_view(), name='featuredevents_update'),
    path('featuredevents/<int:pk>/delete/', views.FeaturedEventDelete.as_view(), name='featuredevents_delete'),
    path('tasks/<int:task_id>/assoc_featured_event/<int:featuredevent_id>/', views.assoc_featuredevent, name='assoc_featuredevents'),
    path('tasks/<int:task_id>/remove_featured_event/<int:featuredevent_id>/', views.remove_featuredevent, name='remove_featuredevents'),
>>>>>>> 372375b4f0b8757d12303634bf3b7c0da0899f4a
]

