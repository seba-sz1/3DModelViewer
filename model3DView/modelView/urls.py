from django.urls import path
from .views import render_3d_model, serve_3d_model_file, home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('model_viewer/<int:model_id>/', render_3d_model, name='render_3d_model'),
    path('model_file/<int:model_id>/', serve_3d_model_file, name='serve_3d_model_file'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
