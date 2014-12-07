from django.contrib import admin
from hunts import models

admin.site.register(models.Business)
admin.site.register(models.Hunt)
admin.site.register(models.Follow)
admin.site.register(models.Comment)
