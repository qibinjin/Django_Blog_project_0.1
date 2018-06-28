from django.shortcuts import render, redirect
from article.models import Article, Comment, User
from django.contrib.auth.models import User as Admin, Group
from django.http import Http404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.contenttypes.models import ContentType
import re


# Create your views here.

def home(request):
    user = request.user
    if user.is_authenticated():
        post_list = Article.objects.all()[:2]
        return render(request, "home.html", {'post_list': post_list, 'username': user})
    else:
        post_list = Article.objects.all()[:2]
        return render(request, "home.html", {'post_list': post_list})


def detail(request, id):
    user=request.user
    if user.is_authenticated():
        if request.method == 'POST':
            if re.match(r'<p><br></p>', request.POST['text2']):
                return HttpResponse("<script>alert('评论框为空');window.location.href='/%s'</script>" % id)
            Comment.objects.create(author=user, content=request.POST['text2'],
                                   article_id=Article.objects.get(id=str(id)))
            return redirect('/%s' % id)
        else:
            try:
                post = Article.objects.get(id=str(id))
                comment_list = Comment.objects.filter(article_id=str(id))
            except Article.DoesNotExist:
                raise Http404
            return render(request, 'post_with_comment.html', {'post': post, 'comment_list': comment_list, 'username': user})
    else:
        try:
            post = Article.objects.get(id=str(id))
            comment_list = Comment.objects.filter(article_id=str(id))
        except Article.DoesNotExist:
            raise Http404
        return render(request, 'post_without_comment.html', {'post': post, 'comment_list': comment_list})


def pages(request):
    user = request.user
    if user.is_authenticated():
        post_list = Article.objects.all()

        return render(request, "home.html", {'post_list': post_list, 'username': user})
    else:
        post_list = Article.objects.all()

        return render(request, "home.html", {'post_list': post_list})


def log(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['passwd'])
        if user is not None:
        # 用户通过验证
            if user.is_active:
                login(request, user)
                return HttpResponse("<script>alert('登陆成功');window.location.href='/';</script>")
            else:
                return HttpResponse("<script>alert('用户名或密码无效，请重新登陆');\
                window.history.back();</script>")
        else:
            return HttpResponse("<script>alert('用户名或密码无效，请重新登陆');window.history.back()</script>")


def user_info(request):
    user = request.user
    if user.is_authenticated():
        return render(request, 'user_info.html',{'username': user, 'last_name':user.last_name, 'first_name': user.first_name, 'email': user.email})
    else:
        pass

def log_out(request):
    user = request.user
    if user.is_authenticated():
        logout(request)
        return HttpResponse("<script>alert('登出成功');window.history.back();</script>")
    else:
        return HttpResponse("<script>alert('登出成功');window.history.back();</script>")

def regist(request):
    user = request.user
    if user.is_authenticated():
        return HttpResponse("<script>alert('请先退出登陆状态');window.history.back();</script>")
    else:
        if request.method == 'POST':
            try:
                user = Admin.objects.create_user(request.POST['username'], request.POST['email_add'],
                                                 request.POST['passwd'], first_name=request.POST['first_name'],
                                                 last_name=request.POST['last_name'])
                user.save()
                normal_group = Group.objects.all()[0]
                print(normal_group)
                user.groups.add(normal_group)
                # content_type = ContentType.objects.get_for_model(Comment)
                # permission = Permission.objects.create(
                #     codename='can_publish',
                #     name='Can Publish Posts',
                #     content_type=content_type,
                # )

            except Exception as e:
                print(e)
                return HttpResponse("<script>alert('用户名已存在');window.location.href='/regist';</script>")

            else:
                return HttpResponse("<script>alert('注册成功');window.location.href='/accounts/login/';</script>")
        else:
            return render(request, 'regist.html')

def date(request, date):
    article_list = Article.objects.filter(date_time__startswith=date.split(' ')[0])

    return render(request,'home.html', {'post_list':article_list})

