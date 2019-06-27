from django.urls import path
from snippets import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #function based views
   # path('snippets/', views.snippet_list),
    #path('snippets/<int:pk>/', views.snippet_detail),
    # CLASS BASED URLS
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
#http://127.0.0.1:8000/snippets/
#http://127.0.0.1:8000/snippets.api/
#http://127.0.0.1:8000/snippets.json/