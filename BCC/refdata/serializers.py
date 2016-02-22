from rest_framework import serializers
from refdata.models import Channel
from refdata.models import Country
from refdata.models import CountrySubdivision
from refdata.models import GenreType
from refdata.models import GenreAuthority
from refdata.models import Genre
from refdata.models import RatingAuthority
from refdata.models import RatingContentDescriptor
from refdata.models import Rating
from refdata.models import Language
from refdata.models import ScriptName
from refdata.models import BCP47Language
from refdata.models import ActivityType
from refdata.models import ObjectProperty
from refdata.models import Activity
from refdata.models import ActivityPropertyRelation


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('pk', 'vmid', 'short_name', 'name', 'description', 'status')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('pk', 'vmid', 'name', 'code2', 'code3', 'codeN')


class CountrySubdivisionSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=False, read_only=True)

    class Meta:
        model = CountrySubdivision
        fields = ('pk', 'vmid', 'name', 'country', 'subcode')


class GenreTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenreType
        fields = ('pk', 'vmid', 'name')


class GenreAuthoritySerializer(serializers.ModelSerializer):
    class Meta:
        model = GenreAuthority
        fields = ('pk', 'vmid', 'description', 'ref_link')


class GenreSerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(read_only=True)
    authority = GenreAuthoritySerializer(many=False, read_only=True)
    type = GenreTypeSerializer(many=False, read_only=True)

    class Meta:
        model = Genre
        fields = ('pk', 'vmid', 'name', 'parent', 'authority', 'type')


class RatingAuthoritySerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingAuthority
        fields = ('pk', 'vmid', 'name', 'description', 'ref_link')


class RatingContentDescriptorSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingContentDescriptor
        fields = ('pk', 'descriptor')


class RatingSerializer(serializers.ModelSerializer):
    authority = RatingAuthoritySerializer(many=False, read_only=True)
    descriptors = RatingContentDescriptorSerializer(many=True, read_only=False)

    class Meta:
        model = Rating
        fields = ('pk', 'vmid', 'name', 'description', 'authority', 'descriptors')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('pk', 'vmid', 'name', 'code2', 'code3')


class ScriptNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScriptName
        fields = ('pk', 'vmid', 'name', 'code', 'number')


class BCP47LanguageSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(many=False, read_only=True)
    script = ScriptNameSerializer(many=False, read_only=True)
    country = CountrySerializer(many=False, read_only=True)

    class Meta:
        model = BCP47Language
        fields = ('language', 'script', 'country')


class ActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityType
        fields = ('vmid', 'name')


class ObjectPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectProperty
        fields = ('vmid', 'name', 'object_type')


class ActivitySerializer(serializers.ModelSerializer):
    parent = serializers.HyperlinkedIdentityField
    type = ActivityTypeSerializer(many=False, read_only=True)

    class Meta:
        model = Activity
        fields = ('vmid', 'type', 'name', 'parent')


class ActivityPropertyRelationSerializer(serializers.ModelSerializer):
    activity = ActivitySerializer(many=False, read_only=True)
    object_property = ObjectPropertySerializer(many=False, read_only=True)

    class Meta:
        model = ActivityPropertyRelation
        fields = ('activity', 'object_property', 'required')