from django.conf.urls import url
from . import views
from django.contrib import auth

app_name = 'blog'

urlpatterns = [
    url(r'^$',views.PostList.as_view(),name='post_list'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^post_detail/(?P<pk>\d+)$',views.PostDetail.as_view(),name='post_detail'),
    url(r'^post_create/$',views.PostCreate.as_view(),name='post_create'),
    url(r'^post_edit/(?P<pk>\d+)/$',views.PostUpdate.as_view(),name='post_edit'),
    url(r'^post_delete/(?P<pk>\d+)/$',views.PostDelete.as_view(),name='post_delete'),
    url(r'^post_drafts/$',views.DraftListView.as_view(),name='draft_list'),
    url(r'^comment_create/(?P<pk>\d+)$',views.comment_create,name='comment_create'),
    url(r'^approve_comment/(?P<pk>\d+)$',views.approve_comment,name='approve_comment'),
    url(r'^remove_comment/(?P<pk>\d+)$',views.remove_comment,name='remove_comment'),
    url(r'^publish_post/(?P<pk>\d+)$',views.publish_post,name='publish_post'),
    
    
    

]

