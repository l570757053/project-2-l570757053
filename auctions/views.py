from pickle import FALSE
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User
from .models import shangpin
from .models import shoucang
from .models import pinglun



def index(request):
    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create(request):
    return render(request,"auctions/createsp.html")

#创建商品
def createsp(request):
    name=request.POST["name"]
    content=request.POST["content"]
    price=request.POST["price"]
    type=request.POST["kind"]
    pic=request.FILES.get("pic")
    master=request.user
    user=request.user.username
    sp=shangpin.objects.create(name=name,content=content,price=price,kind=type,pic=pic,master=master,user=user)
    sp.save()
    return render(request, "auctions/put.html",{"content":"创建商品成功"})


#创建评论
def createpl(request,id):
    user=request.user.username
    sps=shangpin.objects.get(ID=id)
    content=request.POST["text"]
    pl=pinglun.objects.create(user=user,sp=sps,text=content)
    pl.save()
    pls=pinglun.objects.filter(sp=sps)
    return render(request, "auctions/inf.html",{"shangpin":sps ,"pingluns":pls})


#出价
def chujia(request,id):
    user=request.user.username
    sps=shangpin.objects.get(ID=id)
    price=request.POST["price"]
    price=float(price)
    if price>sps.price:
        sps.price=price
        sps.user=user
        sps.save()
        return render(request, "auctions/put.html",{"content":"出价成功"})
    else:
        return render(request, "auctions/put.html",{"content":"出价失败，你的出价低于最高价"})

#进入商品页面
def inf(request,id):
    sps=shangpin.objects.get(ID=id)
    pl=pinglun.objects.filter(sp=sps)
    return render(request, "auctions/inf.html",{"shangpin":sps ,"pingluns":pl})

#收藏
def scsp(request,id):
    user=request.user
    sps=shangpin.objects.get(ID=id)
    
    if shoucang.objects.filter(id=id,user=user):
        return render(request, "auctions/put.html",{"content":"商品已经收藏过"})
    else:
        scs=shoucang.objects.create(user=user,sp=sps)
        scs.save()
        return render(request, "auctions/put.html",{"content":"收藏商品成功"})


#进入收藏夹
def scj(request):
    user=request.user
    scs=shoucang.objects.filter(user=user)
    sc=[ i.sp for i in scs]

    return render(request, "auctions/index.html",{"shangpins":sc ,"content":"收藏夹"})
#结束拍卖
def endsp(request,id):
    sps=shangpin.objects.get(ID=id)
    user=request.user
    if sps.master==user:
        sps.start=0
        sps.save()
        return render(request, "auctions/put.html",{"content":"结束拍卖商品成功"})
    else:
        return render(request, "auctions/put.html",{"content":"你无权结束拍卖"})


#显示全部商品
def listsp(request):
    sps=shangpin.objects.filter(start=1)
    return render(request, "auctions/index.html",{"shangpins":sps ,"content":"商品列表"})

#显示卖出商品
def listsp1(request):
    user=request.user
    sps=shangpin.objects.filter(master=user)
    return render(request, "auctions/index.html",{"shangpins":sps ,"content":"已卖出"})
