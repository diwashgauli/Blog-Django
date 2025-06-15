from django.shortcuts import render
from blog_app.models import Post

def post_list(request):
    published_posts = Post.objects.filter(published_at__isnull=False)
    draft_posts = Post.objects.filter(published_at__isnull=True)

    if published_posts.exists():
        return render(
            request,
            "post_list.html",
            {"posts": published_posts} 
        )
    else:
        return render(
            request,
            "drafts.html",
            {"drafts": draft_posts} 
        )



def view_content(request,id):
    post=(Post.objects.get(id=id))
    return render(
        request,
        "content.html",
        {"post":post}
    )

def draft_list(request):
    draft_posts = Post.objects.filter(published_at__isnull=True)
    return render(
        request,
        "drafts.html",
        {"drafts": draft_posts}
    )

