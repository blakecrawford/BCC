from rest_framework import viewsets
import epd.serializers
import epd.models

# class ChannelViewSet(viewsets.ModelViewSet):
#     queryset = refdata.models.Channel.objects.all()
#     serializer_class = refdata.serializers.ChannelSerializer


class CodecViewSet(viewsets.ModelViewSet):
    queryset = epd.models.Codec.objects.all()
    serializer_class = epd.serializers.CodecSerializer


class SpecificationViewSet(viewsets.ModelViewSet):
    queryset = epd.models.Specification.objects.all()
    serializer_class = epd.serializers.SpecificationSerializer


class ScanTypeViewSet(viewsets.ModelViewSet):
    queryset = epd.models.ScanType.objects.all()
    serializer_class = epd.serializers.ScanTypeSerializer


class ImageTypeViewSet(viewsets.ModelViewSet):
    queryset = epd.models.ImageType.objects.all()
    serializer_class = epd.serializers.ImageTypeSerializer


class EntityTypeViewSet(viewsets.ModelViewSet):
    queryset = epd.models.EntityType.objects.all()
    serializer_class = epd.serializers.EntityTypeSerializer


class EndpointViewSet(viewsets.ModelViewSet):
    queryset = epd.models.Endpoint.objects.all()
    serializer_class = epd.serializers.EndpointSerializer


class PlatformViewSet(viewsets.ModelViewSet):
    queryset = epd.models.Platform.objects.all()
    serializer_class = epd.serializers.PlatformSerializer


class TechnicalVideoRequirementsViewSet(viewsets.ModelViewSet):
    queryset = epd.models.TechnicalVideoRequirements.objects.all()
    serializer_class = epd.serializers.TechnicalVideoRequirementsSerializer


class StaticImageRequirementsViewSet(viewsets.ModelViewSet):
    queryset = epd.models.StaticImageRequirements.objects.all()
    serializer_class = epd.serializers.StaticImageRequirementsSerializer


class MetadataSchemaViewSet(viewsets.ModelViewSet):
    queryset = epd.models.MetadataSchema.objects.all()
    serializer_class = epd.serializers.MetadataSchemaSerializer


class PackageStructureViewSet(viewsets.ModelViewSet):
    queryset = epd.models.PackageStructure.objects.all()
    serializer_class = epd.serializers.PackageStructureSerializer


class DeliveryProcessViewSet(viewsets.ModelViewSet):
    queryset = epd.models.DeliveryProcess.objects.all()
    serializer_class = epd.serializers.DeliveryProcessSerializer


class DeliveryContextViewSet(viewsets.ModelViewSet):
    queryset = epd.models.DeliveryContext.objects.all()
    serializer_class = epd.serializers.DeliveryContextSerializer

