from django.db import models

# Create your models here.

class Attendance(models.Model):
	timestamp = models.DateTimeField(db_index=True,null=True,default=None)
	name = models.CharField(max_length=250)
	student_id = models.CharField(max_length=64)
	university_id = models.CharField(max_length=64)

	def __str__(self):
		return self.name
		#return self.name + ' - ' + self.student_id
