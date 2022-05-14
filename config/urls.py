"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

import board.views

# app_name = 'board'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', board.views.home2),
    path('costomer_service/', board.views.notice),
    path('board/', include('board.urls')),
    path('cart/', include('cart.urls')),
    path('coupon/', include('coupon.urls')),
    path('order/', include('order.urls')),
    path('shop/', include('shop.urls')),
    path('home/', board.views.home2),

    # path('question/', board.views.q_index, name='q_index'),
    # path('question/<int:question_id>', board.views.detail, name='detail'),
    # path('answer/create/<int:question_id>', board.views.answer_create, name='answer_create'),


]
