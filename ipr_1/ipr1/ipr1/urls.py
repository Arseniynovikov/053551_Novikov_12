"""
URL configuration for ipr1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from tkinter.font import names

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from museum import views as museum_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('', museum_views.expositions, name='expositions'),
    path('contacts/', museum_views.contacts, name='contacts'),
    path('exhibits/', museum_views.exhibits, name='exhibits'),
    path('schedule/', museum_views.schedule, name='schedule'),
    path('authors/', museum_views.authors, name='authors'),
    path('search/', museum_views.search, name='search'),
    path('authors/author_profile/<int:author_id>', museum_views.author_profile, name='author_profile'),
    path('form_profile/<int:form_id>', museum_views.form_profile, name='form_profile'),
    path('exposition_profile/<int:exposition_id>/', museum_views.exposition_profile, name='exposition_profile'),
    path('exhibits/exhibit_profile/<int:exhibit_id>/', museum_views.exhibit_profile, name='exhibit_profile')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
