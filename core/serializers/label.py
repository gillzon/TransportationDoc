from rest_framework.serializers import ModelSerializer, SerializerMethodField
from core.models import Sender, Receiver, Label
from core.utils.label import generate_label
import base64
class SenderSerializer(ModelSerializer):
    class Meta:
        model = Sender
        fields = '__all__'


class ReceiverSerializer(ModelSerializer):
    class Meta:
        model = Receiver
        fields = '__all__'


class LabelSerializer(ModelSerializer):
    sender = SenderSerializer(read_only=False, many=False)
    receiver = ReceiverSerializer(read_only=False, many=False)
    base64labeldata = SerializerMethodField('get_labeldata')
    class Meta:
        model = Label
        fields = '__all__'

    def create(self, validated_data):
        sender_data = self.context['sender']
        receiver_data = self.context['receiver']
        validated_data_copy = validated_data.copy()
        print(sender_data['name'])

        sender = Sender.objects.create(name=sender_data['name'],
                                       city=sender_data['city'],
                                       address1=sender_data['address1'],
                                       isocountry=sender_data['isocountry'],
                                       zipcode=sender_data['zipcode'],
                                       phone=sender_data['phone'],
                                       contact=sender_data['contact'])
        receiver = Receiver.objects.create(name=receiver_data['name'],
                                           city=receiver_data['city'],
                                           address1=receiver_data['address1'],
                                           isocountry=receiver_data['isocountry'],
                                           zipcode=receiver_data['zipcode'],
                                           phone=receiver_data['phone'],
                                           contact=receiver_data['contact'],)
        validated_data_copy['sender'] = sender
        validated_data_copy['receiver'] = receiver
        label = Label.objects.create(**validated_data_copy)
        return label
    
    def get_labeldata(self, obj):
        label = generate_label(obj)
        data_bytes = label.encode("utf-8")
        base64_bytes = base64.b64encode(data_bytes)
        return base64_bytes

