from django.urls import path
from blog_app import views

urlpatterns=[
    path("",views.post_list, name="post-list"),
    path("content/<int:id>/",views.view_content, name="view-content"),
    path("drafts/", views.draft_list, name="drafts"),
    path("post-create/",views.post_create,name="post-create"),
    path("draft-detail/<int:pk>/",views.draft_detail,name="draft-detail"),
    path("post-update/<int:pk>/", views.post_update, name="post-update"),
    path("post-delete/<int:pk>/", views.post_delete, name="post-delete"),
    path("draft-publish/<int:pk>/", views.draft_publish, name="draft-publish"),


    
]