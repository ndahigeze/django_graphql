from django.apps import apps
from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from accounts.models import Users

admin.site.register(Users,UserAdmin)
app = apps.get_app_config('graphql_auth')

for model_name, model in app.models.items():
    admin.site.register(model)