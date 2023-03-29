from django.contrib import admin
from .models import Streaming,WatchList,Reviews

# Register your models here.
admin.site.register(WatchList)
admin.site.register(Streaming)
admin.site.register(Reviews)


