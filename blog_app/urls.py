from django.urls import path
from blog_app import views

urlpatterns=[
    path("",views.PostListView.as_view(), name="post-list"),
    path("content/<int:pk>/", views.PostDetailView.as_view(), name="view-content"),
    path("drafts/", views.DraftListView.as_view(), name="drafts"),
    path("post-create/",views.PostCreateView.as_view(),name="post-create"),
    path("draft-detail/<int:pk>/",views.DraftDetailView.as_view(),name="draft-detail"),
    path("post-update/<int:pk>/", views.PostUpdateView.as_view(), name="post-update"),
    path("post-delete/<int:pk>/", views.PostDeleteView.as_view(), name="post-delete"),
    path("draft-publish/<int:pk>/", views.DraftPublishView.as_view(), name="draft-publish"),


    
]