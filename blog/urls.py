from django.urls import path
from blog.views import PostView,PostDetail,PostCreate,PostUpdate,PostDelete,likeView,add_comment_to_post

app_name = 'blog'

urlpatterns = [
	path('',PostView.as_view(), name = 'post-list'),
	path('detail/<int:pk>/',PostDetail.as_view(), name = 'post-detail'),
	path('create/',PostCreate.as_view(), name = 'post-create'),
	path('update/<int:pk>/',PostUpdate.as_view(), name = 'post-update'),
	path('delete/<int:pk>/',PostDelete.as_view(), name = 'post-delete'),
	path('ajax/likes/',likeView,name='like'),
	path('detail/<int:pk>/comment/',add_comment_to_post,name = 'post-comment'),
	]
