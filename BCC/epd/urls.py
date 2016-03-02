from rest_framework.routers import DefaultRouter
from epd import views as epd_views


router = DefaultRouter()
router.register(r'entitytypes', epd_views.EntityTypeViewSet)
router.register(r'endpoints', epd_views.EndpointViewSet)
router.register(r'platforms', epd_views.PlatformViewSet)
router.register(r'videorequirements', epd_views.TechnicalVideoRequirementsViewSet)
router.register(r'imagerequirements', epd_views.StaticImageRequirementsViewSet)
router.register(r'schemas', epd_views.MetadataSchemaViewSet)
router.register(r'packages', epd_views.PackageStructureViewSet)
router.register(r'deliveryprocess', epd_views.DeliveryProcessViewSet)
router.register(r'deliverycontexts', epd_views.DeliveryContextViewSet)
router.register(r'codecs', epd_views.CodecViewSet)
router.register(r'specifications', epd_views.SpecificationViewSet)
router.register(r'scantypes', epd_views.ScanTypeViewSet)
