from django.db import models


# Create your models here.

class NodeID(models.Model):
    node_name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)


    def __str__(self):
        return self.node_name + '-' + self.location


class Data(models.Model):
    node_id = models.ForeignKey(NodeID, on_delete=models.CASCADE)
    vibration = models.FloatField(null=True, blank=True, default=None)
    coordinate_x = models.FloatField(null=True, blank=True, default=None)
    coordinate_y = models.FloatField(null=True, blank=True, default=None)
    coordinate_z = models.FloatField(null=True, blank=True, default=None)
    timestamp = models.DateTimeField(db_index=True, null=True, default=None)
    tanggal = models.DateField(db_index=True, null=True, default=None)
    waktu = models.TimeField(db_index=True, null=True, default=None)

    def __str__(self):
        return  self.vibration
