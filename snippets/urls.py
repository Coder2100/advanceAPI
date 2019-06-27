"""
from django.urls import path
from snippets import views

from rest_framework.urlpatterns import format_suffix_patterns
"""


#Making sure our URL patterns are named
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

"""
urlpatterns = [
    #function based views
   # path('snippets/', views.snippet_list),
    #path('snippets/<int:pk>/', views.snippet_detail),
    
    # CLASS BASED URLS
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),

    #class based urls views with authentication
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    #Creating an endpoint for the root of our API
    path('', views.api_root),
    #url pattern for the snippet highlights:
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
"""
# API endpoints, Hyperlinks
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('snippets/',
        views.SnippetList.as_view(),
        name='snippet-list'),
    path('snippets/<int:pk>/',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),
    path('snippets/<int:pk>/highlight/',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    path('users/',
        views.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/',
        views.UserDetail.as_view(),
        name='user-detail')
])




#http://127.0.0.1:8000/snippets/
#http://127.0.0.1:8000/snippets.api/
#http://127.0.0.1:8000/snippets.json/