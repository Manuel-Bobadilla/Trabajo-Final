from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import Users


class UserAdmin(ModelAdmin):
    model = Users
    menu_label = "Users"
    menu_icon = "placeholder"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name", "address", "phone", "email",)
    search_fields = ("name",)

modeladmin_register(UserAdmin)