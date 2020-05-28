from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('display/', include('myapp.urls')),
    path('admin/', admin.site.urls),
]
