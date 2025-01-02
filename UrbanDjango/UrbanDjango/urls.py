"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

# from task2.views import class_represent, func_represent
# from task3.views import main_page, games, cart
# from task4.views import main_page, games, cart
from task5.views import sign_up_by_html, sign_up_by_django

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('class', class_represent),
#     path('func/', func_represent),
#     path('platform/', main_page),
#     path('platform/games/', games),
#     path('platform/cart/', cart),
#
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sign_up_by_html),
    path('django_sign_up/', sign_up_by_django),

]