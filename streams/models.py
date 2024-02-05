from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField

from streams import blocks
from users.models import User, Volunteer
from volunteerings.models import Volunteering
from restart.models import Restart

import datetime

# Create your models here.
class BulletinListingPage(Page):    
    template = "streams/bulletin_page.html"

    content = StreamField(
        [
            ("bulletins", blocks.Bulletin()),
        ],
        null=True, blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
            FieldPanel("content", heading="Boletines")
        ]
    
    def get_context(self, request, *args, **kwargs):
        #en caso de que el ususario no este logueado, se va a generar un error, no podrá ver la página
        context = super().get_context(request, *args, **kwargs)
        user = User.objects.get(id=request.user.id)
        volunteer = Volunteer.objects.filter(user = user)
        volunteerings = Volunteering.objects.filter(volunteers__in = volunteer)
        restartAvailable = (datetime.date.today() >= datetime.date(datetime.date.today().year, 2, 1) 
        and not Restart.objects.filter(date__year = datetime.date.today().year) 
        and user.is_superuser)

        context["restartAvailable"] = restartAvailable
        context["volunteer"] = volunteer[0]
        context["volunteerings"] = volunteerings
        return context
    
    class Meta:
        verbose_name = "Página boletines"
        verbose_name_plural = "Páginas boletines"
    
BulletinListingPage._meta.get_field("title").help_text = "Nombre de la sección, no visto por el público. Para facilitar la organización interna de las páginas"