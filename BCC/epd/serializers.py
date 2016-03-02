from rest_framework import serializers
from epd.models import EntityType
from epd.models import Endpoint
from epd.models import Platform
from epd.models import TechnicalVideoRequirements
from epd.models import StaticImageRequirements
from epd.models import MetadataSchema
from epd.models import PackageStructure
from epd.models import DeliveryProcess
from epd.models import DeliveryContext
from epd.models import Codec
from epd.models import Specification
from epd.models import ScanType
from epd.models import ImageType


class CodecSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codec
        fields = ('name',)


class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = ('name',)


class ScanTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScanType
        fields = ('name',)


class ImageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=ImageType
        fields = ('name',)


class EntityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityType
        fields = ('name',)


class EndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endpoint
        fields = ('name',)


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ('name',)


class TechnicalVideoRequirementsSerializer(serializers.ModelSerializer):
    codec = CodecSerializer(many=False, read_only=True)
    specification = SpecificationSerializer(many=False, read_only=True)
    scan_type = ScanTypeSerializer(many=False, read_only=True)

    class Meta:
        model = TechnicalVideoRequirements
        fields = ('description', 'codec',
                  'specification', 'scan_type',
                  'video_average_bitrate', 'frame_rate',
                  'audio_sample_rate', 'audio_bit_depth',
                  'audio_channels', 'audio_channel_configuration',
                  'x_pixels_per_inch', 'y_pixels_per_inch',
                  'audio_track_configuration')


class StaticImageRequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaticImageRequirements
        fields = ('description', 'image_content_relationship', 'image_type',)


class MetadataSchemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetadataSchema
        fields = ('schema', 'xform',)


class PackageStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageStructure
        fields = ('structure_template',)


class DeliveryProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryProcess
        fields = ('bpmn',)


class DeliveryContextSerializer(serializers.ModelSerializer):
    endpoint = EndpointSerializer(many=False, read_only=True)
    # endpoint = serializers.HyperlinkedRelatedField(view_name='endpoint-detail',
    #                                                many=False,
    #                                                read_only=True)
    platform = PlatformSerializer(many=False, read_only=True)
    # platform = serializers.HyperlinkedRelatedField(view_name='platform-detail',
    #                                                many=False,
    #                                                read_only=True)
    entity_type = EntityTypeSerializer(many=False, read_only=True)
    # entity_type = serializers.HyperlinkedRelatedField(view_name='entitytype-detail',
    #                                                   many=False,
    #                                                   read_only=True)
    technical_requirements = TechnicalVideoRequirementsSerializer(many=False, read_only=True)
    image_requirements = StaticImageRequirementsSerializer(many=False, read_only=True)
    # image_requirements = serializers.HyperlinkedRelatedField(view_name='staticimagerequirements-detail',
    #                                                          many=False,
    #                                                          read_only=True)
    metadata_schema = MetadataSchemaSerializer(many=False, read_only=True)
    # metadata_schema = serializers.HyperlinkedRelatedField(view_name='metadataschema-detail',
    #                                                       many=False,
    #                                                       read_only=True)
    package_structure = PackageStructureSerializer(many=False, read_only=True)
    # package_structure = serializers.HyperlinkedRelatedField(view_name='packagestructure-detail',
    #                                                         many=False,
    #                                                         read_only=True)
    delivery_process = DeliveryProcessSerializer(many=False, read_only=True)
    # delivery_process = serializers.HyperlinkedRelatedField(view_name='deliveryprocess-detail',
    #                                                        many=False,
    #                                                        read_only=True)

    class Meta:
        model = DeliveryContext
        fields = ('endpoint', 'platform', 'entity_type', 'technical_requirements',
                  'image_requirements', 'metadata_schema', 'package_structure',
                  'delivery_process',)