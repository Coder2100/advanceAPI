
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
# for auth
from django.conf.urls import include

#Schemas & client libraries
from rest_framework.schemas import get_schema_view
schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    path('schema/', schema_view),
    path('admin/', admin.site.urls),
    path('', include('snippets.urls')),
    #Adding login to the Browsable API
    path('api-auth/', include('rest_framework.urls')),
]