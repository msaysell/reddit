from django.contrib import admin

# Register your models here.
from reddit.models import Submission

admin.site.register(Submission)
