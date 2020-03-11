from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views 
from .views import ImageCreateView,ImageDeleteView

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^comment/<image_id>/', views.comment, name='comment'),

    url(r'^ImageCreate/',views.ImageCreateView,name = 'image_create'),
    url(r'^ImageDelete/',views.ImageDeleteView,name = 'image_delete'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^login/$', auth_views.login,name='login') ,
    url(r'^logout/$',auth_views.logout,name='logout'),
    url(r'^register/',views.signup,name="register"),

]