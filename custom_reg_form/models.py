from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_noop


# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    user = models.OneToOneField(USER_MODEL, null=True, on_delete=models.CASCADE)
    samtykke = models.BooleanField(default=True)
    EMPLOYMENT_STATUS_CHOICES = (
        ('efw', ugettext_noop('Employed for wages')),
        ('selfemployed', ugettext_noop('Self-employed')),
        ('student', ugettext_noop('Student')),
        ('homemaker', ugettext_noop('Homemaker')),
        ('oowlfw', ugettext_noop('Out of work and looking for work')),
        ('oownclfw', ugettext_noop('Out of work but not currently looking for work')),
        ('military', ugettext_noop('Military')),
        ('retired', ugettext_noop('Retired')),
        ('utw', ugettext_noop('Unable to work')),
        ('other', ugettext_noop('Other')),
    )
    employment_status = models.CharField(
        verbose_name="Employment Status",
        blank=True, null=True, max_length=20, db_index=True,
        choices=EMPLOYMENT_STATUS_CHOICES
    )
    email = models.EmailField(max_length=100,verbose_name="Please confirm your e-mail")
    # user = models.BooleanField(USER_MODEL,default=True)
    # EMAIL_GDPR_CONSENT = (
    # )
    # email_gdpr_consent = models.BooleanField(
    #     verbose_name="Subscribe me to the newsletter from NTNU Videre",
    #     blank=True, db_index=True, default=False,
    #     choices=EMAIL_GDPR_CONSENT
    # )
    #baretest = models.TextField()
    #VALG = (('JA','Samtykker'),('NEI','Samtykker IKKE'),)
    #velge = models.CharField(blank=False,verbose_name='Jeg godtar NTNUs betingelser om marketsforing ', choices=VALG, max_length=64)
