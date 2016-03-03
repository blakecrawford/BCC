
from rest_framework.routers import DefaultRouter
from refdata import views as refdata_views

router = DefaultRouter()
router.register(r'channels', refdata_views.ChannelViewSet)
router.register(r'countries', refdata_views.CountryViewSet)
router.register(r'country-subdivisions', refdata_views.CountrySubdivisionViewSet)
router.register(r'genre-types', refdata_views.GenreTypeViewSet)
router.register(r'genre-authorities', refdata_views.GenreAuthorityViewSet)
router.register(r'genres', refdata_views.GenreViewSet)
router.register(r'rating-authorities', refdata_views.RatingAuthorityViewSet)
router.register(r'ratings', refdata_views.RatingViewSet)
router.register(r'languages', refdata_views.LanguageViewSet)
router.register(r'scripts', refdata_views.ScriptNameViewSet)
router.register(r'bcp47-languages', refdata_views.BCP47LanguageViewSet)
router.register(r'activity-types', refdata_views.ActivityTypeViewSet)
router.register(r'object-properties', refdata_views.ObjectPropertyViewSet)
router.register(r'activities', refdata_views.ActivityTypeViewSet)
router.register(r'activity-property-relations', refdata_views.ActivityPropertyRelationViewSet)


# urlpatterns = [
#     url(r'^channels/$', views.ChannelAPIResponse.channel_list),
#     url(r'^channels/(?P<pk>[0-9a-z-]+)/$', views.ChannelAPIResponse.channel_detail),
# ]