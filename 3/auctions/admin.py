from django.contrib import admin
from .models import pinglun
from .models import shangpin
from .models import shoucang
from . import models

# Register your models here.
admin.site.register(models.pinglun)
admin.site.register(models.shangpin)
admin.site.register(models.shoucang)

