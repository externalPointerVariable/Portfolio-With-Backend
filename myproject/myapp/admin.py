from django.contrib import admin
from .models import projectstats, github_stats, leetcode_stats


# Register your models here.
admin.site.register(projectstats)
admin.site.register(github_stats)
admin.site.register(leetcode_stats)