from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("df_api_drf.urls")),
    path("legal/", include("df_documents.urls")),
]
