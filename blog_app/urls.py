from django.urls import path
from blog_app import views

urlpatterns=[
    path("",views.post_list, name="post-list"),
    path("content/<int:id>/",views.view_content, name="view-content"),
    path("drafts/", views.draft_list, name="drafts"),
    
]