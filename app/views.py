import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from django.shortcuts import render, redirect
from app.models import Post, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import datetime
from account.models import Profile, Lecture, PLR

# Create your views here.
def board(request):
    posts = Post.objects.all()

    return render(request, '3_community/board.html', { 'posts': posts })



@login_required(login_url='account/login')
def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            author = request.user.profile,
            title = request.POST['title'],
            content = request.POST['content'],
            created_at = datetime.datetime.now(),
        )
        return redirect('detail', new_post.pk)
    return render(request, '3_community/new.html')

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if (request.method == 'POST'):
        Comment.objects.create(
            post = post, 
            content = request.POST['content'],
            author = request.user
        )
        return redirect('detail', post_pk)

    return render(request, '3_community/detail.html', {'post': post})

def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Post.objects.filter(pk=post_pk).update(
          title = request.POST['title'],
          content = request.POST['content']
        )
        return redirect('detail', post_pk)

    return render(request, '3_community/edit.html', {'post': post}) 

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('board')

def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', post_pk)


############### chatting ##############

def friends(request, lecture_pk):
    lecture = Lecture.objects.get(subnum=lecture_pk)
    plrs = PLR.objects.filter(lecture=lecture)

    return render(request, '4_chat/friends.html', {'friends': plrs})


#######################################