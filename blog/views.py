from django.views.generic import View,TemplateView,ListView,CreateView,DeleteView,DetailView,UpdateView
from blog import forms
from blog.models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from . import forms

class AboutView(TemplateView):
    template_name= 'about.html'

class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetail(DetailView):
    model = Post

class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = forms.PostForm
    

class PostUpdate(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = forms.PostForm
    model = Post

class PostDelete(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-create_date')


def comment_create(request,pk):
    post = get_object_or_404(Post,pk=pk)
    
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.Post = post
            comment.save()
            return redirect('blog:post_detail',pk=post.pk)
    else:
        form = forms.CommentForm()
    return render(request,'blog/comment_form.html',context={'form':form})

@login_required
def approve_comment(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('blog:post_detail',pk = comment.Post.pk)

@login_required
def remove_comment(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.Post.pk
    comment.delete()
    return redirect('blog:post_detail',pk=post_pk)

@login_required
def publish_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('blog:post_list')

class SignUp(CreateView):
    form_class = forms.UserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'