from django.shortcuts import render,get_object_or_404, redirect #힘수들을 다 처리한 후 url로 넘기셈
from .models import Blog
from django.utils import timezone

def index(request):
    blogs=Blog.objects #쿼리셋
    return render(request,'index.html',{'blogs':blogs})

def detail(request,blog_id):
    details=get_object_or_404(Blog,pk = blog_id)
    return render(request,'detail.html',{'details':details})

def new(request): #그냥 화면 띄어죽;
    return render(request,'new.html')

def create(request):
    blog=Blog()
    blog.title=request.GET['title'] #입력받은 함수를 데이터베이스에 넣어주는 함수
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save() #데이터베이스에 저장
    return redirect('/blog/'+str(blog.id)) #여기로 이동해


# Create your views here.
