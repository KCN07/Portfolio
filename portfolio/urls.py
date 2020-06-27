

from django.contrib import admin
from django.urls import path ,  include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',jobs.views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('login/', jobs.views.user_login, name='login'),
    path('logout/', jobs.views.user_logout, name='logout'),
    path('education/',jobs.views.education,name='education'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
