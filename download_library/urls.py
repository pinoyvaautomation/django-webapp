from django.urls import path # type: ignore
from . import views

from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('library/', views.library_home, name='library_home'),
    path('category/<int:category_id>/', views.category_files, name='category_files'),
    path('', views.customer_list, name='customer_list'),

    path('customers/<int:customer_id>/', views.customer_files, name='customer_files'),

    
]

# Add this line to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


