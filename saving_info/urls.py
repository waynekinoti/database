"""
URL configuration for saving_info project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path

from my_app import views
from saving_info import settings

urlpatterns = [
    path('signin',views.signin,name='signin-page'),
    path('',views.home,name='home'),
    path('show',views.show, name='show-page'),
    path('delete/<int:id>',views.delete, name='delete-page'),
    path('details/<int:id>', views.details, name='details-page'),
    path('add',views.add, name='add-page'),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
