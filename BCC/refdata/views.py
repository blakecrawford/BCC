from rest_framework import viewsets
import refdata.serializers
import refdata.models


class ChannelViewSet(viewsets.ModelViewSet):
    queryset = refdata.models.Channel.objects.all()
    serializer_class = refdata.serializers.ChannelSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = refdata.models.Country.objects.all()
    serializer_class = refdata.serializers.CountrySerializer


class CountrySubdivisionViewSet(viewsets.ModelViewSet):
    queryset = refdata.models.CountrySubdivision.objects.all()
    serializer_class = refdata.serializers.CountrySubdivisionSerializer


class GenreTypeViewSet(viewsets.ModelViewSet):
    queryset = refdata.models.GenreType.objects.all()
    serializer_class = refdata.serializers.GenreTypeSerializer


class GenreAuthorityViewSet(viewsets.ModelViewSet):
    queryset = refdata.models.GenreAuthority.objects.all()
    serializer_class = refdata.serializers.GenreAuthoritySerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = refdata.models.Genre.objects.all()
    serializer_class = refdata.serializers.GenreSerializer


class RatingAuthorityViewSet(viewsets.ModelViewSet):
    queryset = refdata.models.RatingAuthority.objects.all()
    serializer_class = refdata.serializers.RatingAuthoritySerializer


class RatingContentDescriptorViewSet(viewsets.ModelViewSet):
    queryset = refdata.models.RatingContentDescriptor.objects.all()
    serializer_class = refdata.serializers.RatingContentDescriptorSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = refdata.models.Rating.objects.all()
    serializer_class = refdata.serializers.RatingSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = refdata.models.Language.objects.all()
    serializer_class = refdata.serializers.LanguageSerializer


class ScriptNameViewSet(viewsets.ModelViewSet):
    queryset = refdata.models.ScriptName.objects.all()
    serializer_class = refdata.serializers.ScriptNameSerializer


class BCP47LanguageViewSet(viewsets.ModelViewSet):
    queryset = refdata.models.BCP47Language.objects.all()
    serializer_class = refdata.serializers.BCP47LanguageSerializer


class ActivityTypeViewSet(viewsets.ModelViewSet):
    queryset = refdata.models.ActivityType.objects.all()
    serializer_class = refdata.serializers.ActivityTypeSerializer


class ObjectPropertyViewSet(viewsets.ModelViewSet):
    queryset = refdata.models.ObjectProperty.objects.all()
    serializer_class = refdata.serializers.ObjectPropertySerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = refdata.models.Activity.objects.all()
    serializer_class = refdata.serializers.ActivitySerializer


class ActivityPropertyRelationViewSet(viewsets.ModelViewSet):
    queryset = refdata.models.ActivityPropertyRelation.objects.all()
    serializer_class = refdata.serializers.ActivityPropertyRelationSerializer


class ThirdPartyIdentificationAuthorityViewSet(viewsets.ModelViewSet):
    queryset = refdata.models.ThirdPartyIdentificationAuthority.objects.all()
    serializer_class = refdata.serializers.ThirdPartyIdentificationAuthoritySerializer




