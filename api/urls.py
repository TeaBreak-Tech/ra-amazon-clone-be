from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ip', views.ip),
    path('session', views.new_session),
    path('video/', views.add_video),
    path('video/list', views.get_video_list),
    path('event/', views.new_event),
    path('videos/', views.get_tagged_video_list),
    path('videos/<str:tag_title>/', views.get_video_by_tag),
    path('video_tag/', views.add_video_tag),
]