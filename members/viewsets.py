from rest_framework import viewsets
from . import models
from . import serializers


class MemberViewset(viewsets.ModelViewSet):
    queryset = models.Member.objects.all()
    serializer_class = serializers.MemberSerializer
