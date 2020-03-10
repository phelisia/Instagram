from django.conf.urls import url
from . import views 
from .views import ImageCreateView,ImageDeleteView

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^ImageCreate/',views.ImageCreateView,name = 'image_create'),
    url(r'^ImageDelete/',views.ImageDeleteView,name = 'image_delete'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^logout/$', views.login, {"next_page": '/'},name='logout') ,
    url(r'^register/',views.signup,name="register"),
    
    

]