from django.urls import path
from app import views 

urlpatterns = [
    path('board/', views.board, name="board"),
    path('new/', views.new, name="new"),
    path('detail/<int:post_pk>', views.detail, name="detail"),
    path('edit/<int:post_pk>', views.edit, name="edit"),
    path('delete/<int:post_pk>', views.delete, name="delete"),
    path('delete_comment/<int:post_pk>/<int:comment_pk>', views.delete_comment, name="delete_comment"),

    #chatting
    path('friends/<str:lecture_pk>', views.friends, name="friends"),
]