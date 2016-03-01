from django.db import models
from django.contrib import admin


# Create your models here.
class InterfacePost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()


class WebPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')


admin.site.register(InterfacePost, WebPostAdmin)
