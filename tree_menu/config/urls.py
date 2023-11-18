from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(
        template_name='base.html',
    ), name='main'),
    path('<slug:slug>/', TemplateView.as_view(
        template_name='base.html',
    ), name='menu'),
]
