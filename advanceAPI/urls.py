
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
# for auth
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('snippets.urls')),
    #Adding login to the Browsable API
    path('api-auth/', include('rest_framework.urls')),
]