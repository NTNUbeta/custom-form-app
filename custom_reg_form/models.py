from django.conf import settings
from django.db import models


# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """
    user = models.OneToOneField(USER_MODEL, null=True, on_delete=models.CASCADE)
    SAMTYKKE = (('JA','Samtykker'),
                ('NEI', 'Samtykker IKKE'),)

    samtykke =  models.CharField(blank=True, verbose_name="Jeg samtykker til å motta markedsføring og kommunikasjon på e-post fra NTNU",
                                               choices=SAMTYKKE, max_length=64,)
