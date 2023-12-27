from django.db import models
import datetime

class Restart(models.Model):
    date = models.DateField(blank=False, null=False, default=datetime.date.today)
    
