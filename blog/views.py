from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Post
from django.http import JsonResponse
from blog.forms import CommentForm
from django.views.generic.edit import FormView
# Create your views here.

class PostView(LoginRequiredMixin,ListView):
	model = Post

class PostDetail(LoginRequiredMixin,DetailView):
	model = Post

class PostCreate(LoginRequiredMixin,CreateView):
	model = Post
	fields = ['title','body','created_date','img']
	success_url = '/blog/'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdate(LoginRequiredMixin,UpdateView):
	model = Post
	fields = ['title','body','created_date','img']
	success_url ='/blog/'

class PostDelete(LoginRequiredMixin,DeleteView):
	model = Post
	fields = ['title','body','created_date','author','img']
	success_url = '/blog/'

def likeView(request):
	if request.method =='GET':

		i=request.GET.get('i',None)
		p=Post.objects.get(id=i)
		p.likes =p.likes + 1
		p.save()
		data={'i':p.likes}
	return JsonResponse(data)


def add_comment_to_post(request,pk):
	post = get_object_or_404(Post,pk = pk)
	if request.method =='Post':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit = False)
			comment.post = post
			comment.save()
			return redirect('blog:post-detail',pk = post.pk)
	else:
		form = CommentForm()
	return render(request,'blog/post_form.html',{'form':form})