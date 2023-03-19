from django.db import models
import uuid


class Sender(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=100)
    isocountry = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    phone = models.IntegerField()
    contact = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    instructions = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Receiver(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=100)
    isocountry = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    phone = models.IntegerField()
    contact = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    instructions = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Label(models.Model):
    LabelTypes = (
        ("zpl", "zpl"),
        ("Zebra", "Zebra"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    printertype = models.CharField(
        max_length=400, choices=LabelTypes, default="Zebra")
    weight = models.FloatField(default=0.00)
    externalUnitId = models.CharField(max_length=80, null=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    service = models.CharField(max_length=100)
    shipmentReference = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    pickupDate = models.DateField(max_length=100)
    item = models.CharField(max_length=100)
    unitNumber = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)
    trackingId = models.CharField(max_length=80, null=True, default="")
    sender = models.ForeignKey('core.Sender',
                               on_delete=models.CASCADE, related_name="label_sender", null=True)
    receiver = models.ForeignKey('core.Receiver',
                               on_delete=models.CASCADE, related_name="label_receiver", null=True)
