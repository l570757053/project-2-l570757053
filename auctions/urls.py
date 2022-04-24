from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("chujia/<str:id>", views.chujia, name="chujia"),
    path("createsp", views.createsp, name="createsp"),
    path("createpl/<str:id>", views.createpl, name="createpl"),
    path("inf/<str:id>", views.inf, name="inf"),
    path("scsp/<str:id>", views.scsp, name="scsp"),
    path("endsp/<str:id>", views.endsp, name="endsp"),
    path("listsp", views.listsp, name="listsp"),
    path("listsp1", views.listsp1, name="listsp1"),
    path("create", views.create, name="create"),
    path("scj", views.scj, name="scj"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

