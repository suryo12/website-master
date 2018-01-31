# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

class NodeID(models.Model):
    node_name = models.CharField(max_length=250)
    alamat = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('smart:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.node_name + '-' + self.alamat

class Data(models.Model):
    node_id = models.ForeignKey(NodeID, on_delete=models.CASCADE)
    tegangan = models.CharField(max_length=1000)
    arus = models.FloatField(null=True, blank=True, default=None)
    daya = models.CharField(max_length=1000)
    tanggal = models.DateField(db_index=True, null=True, default=None)
    waktu = models.TimeField(db_index=True, null=True, default=None)

    def __str__(self):
        return str(self.node_id) + " - " + self.tegangan + " - " + str(self.tanggal) + " - " + str(self.waktu)

class input(models.Model):
    start_date=models.DateField(auto_now=False, auto_now_add=False)
