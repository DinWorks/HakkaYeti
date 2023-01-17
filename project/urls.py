from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),
    path('' , include('meals.urls' , namespace='meals')),  
]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Resturant AdminPanel"
admin.site.site_title = "Resturant App Admin "
admin.site.site_index_title = "Welcome To Resturant Admin Panel"
