from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField

from streams import blocks
from users.models import User, Volunteer
from volunteerings.models import Volunteering

# Create your models here.
class BulletinListingPage(Page):
    custom_title = models.CharField(max_length=100, blank=False, null=False, help_text="overwrites the default title")
    
    template = "streams/bulletin_page.html"

    content = StreamField(
        [
            ("bulletins", blocks.Bulletin()),
        ],
        null=True, blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
            FieldPanel("custom_title"),
            FieldPanel("content")
        ]
    
    def get_context(self, request, *args, **kwargs):
        #en caso de que el ususario no este logueado, se va a generar un error, no podrá ver la página
        context = super().get_context(request, *args, **kwargs)
        user = User.objects.get(id=request.user.id)
        volunteer = Volunteer.objects.filter(user = user)
        volunteerings = Volunteering.objects.filter(volunteers__in = volunteer)
        context["volunteer"] = volunteer[0]
        context["volunteerings"] = volunteerings
        return context
    