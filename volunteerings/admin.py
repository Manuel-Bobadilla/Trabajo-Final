from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import Volunteering

class VolunteeringAdmin(ModelAdmin):
    model = Volunteering
    menu_label = "Voluntariados"
    menu_icon = "placeholder"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name",)
    search_fields = ("name",)

modeladmin_register(VolunteeringAdmin)
