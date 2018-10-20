from django.db import models


class File(models.Model):
  file = models.FileField(blank=False, null=False)
  remark = models.CharField(max_length=20)
  timestamp = models.DateTimeField(auto_now_add=True)


class Player(models.Model):
    player_Id = models.BigIntegerField(primary_key=True)
    player_name = models.FileField(blank=False, null=False)

class Device(models.Model):
    device_id = models.BigIntegerField(primary_key=True)


class DeviceWelcomeAudio(models.Model):

    device_Id = models.ForeignKey(Device,related_name='deviceWelcomeAudio',on_delete=models.CASCADE)
    file = models.FileField(blank=False, null=False)
    name = models.CharField(max_length=20, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    isCurrent = models.BooleanField(default=False)


class DeviceLodingAudio(models.Model):

    device_Id = models.ForeignKey(Device,related_name='deviceLodingAudio',on_delete=models.CASCADE)
    file = models.FileField(blank=False, null=False)
    name = models.CharField(max_length=20, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    isCurrent = models.BooleanField(default=False)
