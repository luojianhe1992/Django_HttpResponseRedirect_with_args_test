from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Foo(models.Model):
    foo_name = models.CharField(max_length=100)
    foo_description = models.TextField(max_length=1000)
    foo_time_created = models.DateTimeField(auto_now_add=True)
    foo_time_changed = models.DateTimeField(auto_now=True)
    