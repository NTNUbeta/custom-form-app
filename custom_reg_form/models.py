from django.conf import settings
from django.db import models



# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    user = models.OneToOneField(USER_MODEL, null=True, on_delete=models.CASCADE)
    samtykke = models.BooleanField(default=True)
    #baretest = models.TextField()
    #VALG = (('JA','Samtykker'),('NEI','Samtykker IKKE'),)
    #velge = models.CharField(blank=False,verbose_name='Jeg godtar NTNUs betingelser om marketsforing ', choices=VALG, max_length=64)
