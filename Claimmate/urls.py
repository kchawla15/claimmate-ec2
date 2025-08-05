from django.contrib import admin
from django.urls import path
from core import views as core_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('dashboard/', core_views.dashboard, name='dashboard'),
    path('register/', core_views.register, name='register'),
    path('logout/', core_views.force_logout, name='logout'),
    path('upload/', core_views.upload_warranty, name='upload_warranty'),
    path('delete-warranty/<int:item_id>/', core_views.delete_warranty, name='delete_warranty'),

    # Admin panel URLs
    path('admin-panel/', core_views.admin_dashboard, name='admin_dashboard'),
    path('admin-panel/items/', core_views.admin_items, name='admin_items'),
    path('admin-panel/delete/<int:pk>/', core_views.admin_delete_item, name='admin_delete_item'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
