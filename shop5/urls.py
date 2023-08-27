from django.urls import  path,include
from . import views
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name='index')
]  + static(settings.MEDIA_URL,
							document_root=settings.MEDIA_ROOT)



