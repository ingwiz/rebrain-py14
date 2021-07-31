from django.db import models

# Create your models here.

class Server(models.Model):

    name = models.CharField('name', max_length=255, default=None)
    ip_address = models.GenericIPAddressField('IP', max_length=16, default='0.0.0.0')
    description = models.TextField('description', max_length=255)
    server_is_active = models.BooleanField('server_is_active', default = False)

    class Meta:
        managed = True
        verbose_name = 'Server'

