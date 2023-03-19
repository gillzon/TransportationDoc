from rest_framework.viewsets import ModelViewSet
from core.serializers.label import LabelSerializer

from core.models import Label

from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.core.exceptions import ObjectDoesNotExist
from drf_yasg.utils import swagger_auto_schema


class LabelViewSet(ModelViewSet):
    queryset = Label.objects.order_by('pk')
    serializer_class = LabelSerializer

    @swagger_auto_schema(auto_schema=None)
    def partial_update(self, request, pk=None):
        pass

    @swagger_auto_schema(auto_schema=None)
    def update(self, request, pk=None):
        pass

    @swagger_auto_schema(auto_schema=None)
    def list(self, request):
        pass

    def create(self, instance):
        data = self.request.data
      
        serializer = LabelSerializer(data=data, context={
            'sender': self.request.data.get('sender'),
            'receiver': self.request.data.get('receiver'),
        })
        if serializer.is_valid():
            # MAGIC HAPPENS HERE
            # ... Here you do the routine you do when the data is valid
            # You can use the serializer as an object of you Assets Model
            # Save it
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # @action(detail=True, methods=['get'])
    # def get_label(self, request, pk=None):
    #     data = {}
    #     try:
    #         prc = Unit.objects.get(id=pk)
    #         data = UnitSerializer(prc).data
    #     except ObjectDoesNotExist:
    #         data = {
    #             'Did not find any parcel with that id'
    #         }
    #     return Response(data, status=status.HTTP_200_OK)
