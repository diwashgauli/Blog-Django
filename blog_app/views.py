from django.shortcuts import render,redirect
from blog_app.models import Post
from blog_app.forms import PostForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


#make sure you make seperate views for each functionalities inside an app
#class based views
class PostListView(ListView):
    model=Post
    template_name="post_list.html"
    context_object_name="posts"

    def get_queryset(self):
        posts= Post.objects.filter(published_at__isnull=False).order_by("-published_at")   #if need to do filter andll
        return posts






class PostDetailView(DetailView):
    model=Post
    template_name="post_detail.html"
    context_object_name="post"

    def get_queryset(self):
        queryset = Post.objects.filter(pk=self.kwargs["pk"],published_at__isnull=False)
        return queryset
    

class DraftListView(ListView):
    model=Post
    template_name="draft_list.html"
    context_object_name="drafts"

    def get_queryset(self):
        drafts= Post.objects.filter(published_at__isnull=True) #if need to do filter andll
        return drafts


@login_required
def draft_list(request):
    draft_posts = Post.objects.filter(published_at__isnull=True).order_by('-id')
    return render(
        request,
        "draft_list.html",
        {"drafts": draft_posts}
        
    )



class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    template_name="post_create.html"
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("draft-detail",kwargs={"pk": self.object.pk})



class DraftDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "draft_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        return Post.objects.filter(published_at__isnull=True)
 
# @login_required
# def draft_detail(request, pk):
#     post = Post.objects.get(pk=pk, published_at__isnull=True)
#     return render(
#         request,
#         "draft_detail.html",
#         {"post": post},
#     )

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model=Post
    template_name="post_create.html"
    form_class = PostForm

    def get_success_url(self):
        post=self.get_object()

        if post.published_at:
            return reverse("view-content",kwargs={"pk":post.pk})
        else:
            return reverse("draft-detail",kwargs={"pk": post.pk})
        




# @login_required
# def post_update(request,pk):
#     if request.method == "GET":
#         post=Post.objects.get(pk=pk)
#         form=PostForm(instance=post)
#         return render(
#             request,
#             "post_create.html",
#             {"form":form},
#         )
#     else:
#         post=Post.objects.get(pk=pk)
#         form=PostForm(request.POST,instance=post)
#         if form.is_valid():
#             post=form.save()
#             if post.published_at:
#                 return redirect("view-content",post.pk) #we give urls name here 
#             else:
#                 return redirect("draft-detail",post.pk)
#         else:
#             return render(
#                 request,
#                 "post_create.html",
#                 {"form":form}
#             )



#making form is remaining of class PostDeleteView refer the video


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=Post

    def get_success_url(self):
        post=self.get_object()
        if post.published_at:
            return reverse("post-list")
        else:
            return reverse("drafts")
        




# @login_required
# def post_delete(request,pk):
#     post=Post.objects.get(pk=pk)
#     post.delete()
#     if post.published_at:
#         return redirect("post-list")
#     else:
#         return redirect("drafts")
    

class DraftPublishView(LoginRequiredMixin,View):
    def get(self,request,pk):
        post = Post.objects.get(pk=pk, published_at__isnull=True)
        post.published_at = timezone.now()
        post.save()
        return redirect("post-list")
    
# @login_required
# def draft_publish(request,pk):
#     post=Post.objects.get(pk=pk, published_at__isnull=True)
#     post.published_at=timezone.now()
#     post.save()
#     return redirect("post-list")
