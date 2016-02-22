from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from refdata import views as refdata_views

router = DefaultRouter()
router.register(r'channels', refdata_views.ChannelViewSet)

# urlpatterns = [
#     url(r'^channels/$', views.ChannelAPIResponse.channel_list),
#     url(r'^channels/(?P<pk>[0-9a-z-]+)/$', views.ChannelAPIResponse.channel_detail),
# ]