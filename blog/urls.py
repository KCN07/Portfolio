

from django.urls import path
from . import views

urlpatterns = [

    path('',views.allblogs, name='allblogs'),
    path('<int:blog_id>/',views.detail, name='detail'),
    path('addblog/',views.addblog,name='addblog'),
    path('editblog/',views.addblog,name='editblog'),

]
