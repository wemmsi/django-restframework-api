from rest_framework import serializers

from ropes.models import ClimbingRopes, ColorSchemes, OtherRopes, Ropes


class RopesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ropes
        fields = ['unique_id', 'rope_type']
        read_only_fields = ['unique_id']


class ColorSchemesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ColorSchemes
        fields = ['unique_id', 'name', 'base_color']
        read_only_fields = ['unique_id']


class ClimbingRopesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClimbingRopes
        fields = ['unique_id', 'name', 'meters_available',
                  'color_scheme_ref', 'rope_ref']
        read_only_fields = ['unique_id']


class OtherRopesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OtherRopes
        fields = ['unique_id', 'name', 'meters_available',
                  'color_scheme_ref', 'rope_ref']
        read_only_fields = ['unique_id']
