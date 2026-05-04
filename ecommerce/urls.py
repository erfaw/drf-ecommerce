from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ecommerce.product.views import CategoryViewSet, BrandViewSet, ProductViewSet, ProductLineViewSet, ProductImageViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register(r"category", CategoryViewSet)
router.register(r"brand", BrandViewSet)
router.register(r"product", ProductViewSet)
router.register(r"product-line", ProductLineViewSet)
router.register(r"product-image", ProductImageViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
