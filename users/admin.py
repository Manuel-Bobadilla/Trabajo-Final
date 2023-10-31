from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import Volunteer


class UserAdmin(ModelAdmin):
    model = Volunteer
    menu_label = "Voluntarios"
    menu_icon = "placeholder"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("user", "address", "phone", "university", "university_file", "validated")
    search_fields = ("user__last_name", "user__first_name", "university", "university_file", "dni")

modeladmin_register(UserAdmin)