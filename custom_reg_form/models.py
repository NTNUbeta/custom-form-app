from django.conf import settings
from django.db import models



# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):

    user = models.OneToOneField(USER_MODEL, null=True, on_delete=models.CASCADE)
    Jeg samtykker til motta markedsforing kommunikasjon epost fra NTNU  = models.BooleanField(blank=True, null=True)
    #SAMTYKKE = (('JA','Samtykker'),
               # ('NEI','Samtykker IKKE'),)

    #samtykke =  models.CharField(blank=False, 
                     #  verbose_name='Jeg godtar NTNUs betingelser om marketsforing ',
                        # choices=SAMTYKKE, max_length=150)
