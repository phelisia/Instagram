from django.conf.urls import url
from . import views 
# from .views import PostCreateView, PostDeleteView

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    # url(r'^new',PostCreateView.as_view(),name = 'post_create'),
    # url(r'^delete/(?P<int>)\d+',PostDeleteView.as_view(),name='post_delete'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^search/', views.search_results, name='search_results'),
    

]