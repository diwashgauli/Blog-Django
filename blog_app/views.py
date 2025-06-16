from django.shortcuts import render,redirect
from blog_app.models import Post
from blog_app.forms import PostForm
def post_list(request):
    published_posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')

    return render(
            request,
            "post_list.html",
            {"posts": published_posts} 
        )
   


def view_content(request,id):
    post=(Post.objects.get(id=id))
    return render(
        request,
        "content.html",
        {"post":post}
    )

def draft_list(request):
    draft_posts = Post.objects.filter(published_at__isnull=True).order_by('-id')
    return render(
        request,
        "drafts.html",
        {"drafts": draft_posts}
        
    )


def post_create(request):
    if request.method== "GET":
        form = PostForm()
        return render(
            request,
            "post_create.html",
            {"form":form}
                    
        )
    else:
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author =request.user #logged in user will be author
            post.save()
            return redirect("draft-detail",pk=post.pk)
        else:
            return render(
                request,
                "post_create.html",
                {"form":form}
            )

