from django.contrib import admin
from .models import User, Lead, Agent, UserProfile, Category
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class UserResource(resources.ModelResource):
   class Meta:
      model = User
class UserAdmin(ImportExportModelAdmin):
   resource_class = UserResource

class AgentResource(resources.ModelResource):
   class Meta:
      model = Agent
class AgentAdmin(ImportExportModelAdmin):
   resource_class = AgentResource


class LeadResource(resources.ModelResource):
   class Meta:
      model = Lead
class LeadAdmin(ImportExportModelAdmin):
   resource_class = LeadResource

class UserProfileResource(resources.ModelResource):
   class Meta:
      model = UserProfile
class UserProfileAdmin(ImportExportModelAdmin):
   resource_class = UserResource

class CategoryResource(resources.ModelResource):
   class Meta:
      model = Category
class CategoryAdmin(ImportExportModelAdmin):
   resource_class = UserResource


admin.site.register(User,UserAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Lead,LeadAdmin)
admin.site.register(Agent,AgentAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
