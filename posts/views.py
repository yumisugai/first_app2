from django.shortcuts import render,redirect
from django.views import View
from posts.models import Post
from .forms  import PostForm

class IndexView(View):
    def get(self,request,*args,**kwargs):
        posts =  Post.objects.all()  # すべてのレコードをpostsに代入
        return render(request, 'posts/index.html',{'posts':posts})

class CreateView(View):
  def get(self, request, *args, **kwargs):
    form = PostForm()
    return render(request, 'posts/create.html', {'form': form})
  
  # 投稿内容を保存する
  def post(self, request, *args, **kwargs):
    form = PostForm(request.POST)
    # バリデーションのチェック
    if form.is_valid():
      # 投稿に問題がなければ保存する
      form.save()
      # redirectで一覧画面に移動する
      return redirect('posts:index')