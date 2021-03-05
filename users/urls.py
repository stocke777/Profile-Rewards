
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.profile, name = "home"),
    path('profile/', views.profile, name = "profile"),
    path('profile_update/', views.profile_update, name = "profile_update"),
    path("register/", views.register, name = "register"),
    path('login/', auth_views.LoginView.as_view(template_name = "users/login.html"), name = "login"),
    path('logout/', auth_views.LogoutView.as_view(template_name = "users/logout.html"), name = "logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
