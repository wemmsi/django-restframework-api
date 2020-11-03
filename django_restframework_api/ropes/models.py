import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models


class Ropes(models.Model):
    """High level ropes definition"""
    unique_id = models.UUIDField(
        primary_key=True, default=uuid.uuid1, editable=False, unique=True)
    rope_type = models.CharField(max_length=100, unique=True)

    class Meta:
        app_label = 'ropes'
        ordering = ['rope_type']


class ColorSchemes(models.Model):
    """Model for all color schemes"""
    unique_id = models.UUIDField(
        primary_key=True, default=uuid.uuid1, editable=False, unique=True)
    name = models.CharField(max_length=150)
    base_color = models.CharField(max_length=150)


class ClimbingRopes(models.Model):
    """Basic climbing rope definition"""
    unique_id = models.UUIDField(
        primary_key=True, default=uuid.uuid1, editable=False, unique=True)
    name = models.CharField(max_length=150)
    meters_available = models.FloatField(max_length=15, null=True)
    color_scheme_ref = models.ForeignKey(
        "ColorSchemes", null=True, on_delete=models.PROTECT, blank=True)
    rope_ref = models.ForeignKey(
        "Ropes", null=True, blank=True, on_delete=models.PROTECT)


class OtherRopes(models.Model):
    """Class for all other ropes, which are no official climbing ropes"""
    unique_id = models.UUIDField(
        primary_key=True, default=uuid.uuid1, editable=False, unique=True)
    name = models.CharField(max_length=150)
    meters_available = models.FloatField(max_length=15, null=True)
    color_scheme_ref = models.ForeignKey(
        "ColorSchemes", null=True, on_delete=models.PROTECT, blank=True)
    rope_ref = models.ForeignKey(
        "Ropes", null=True, blank=True, on_delete=models.PROTECT)
