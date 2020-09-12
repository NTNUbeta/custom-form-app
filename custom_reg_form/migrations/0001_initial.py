# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('samtykke', models.CharField(blank=True, verbose_name="Jeg samtykker til å motta markedsføring og kommunikasjon på e-post fra NTNU",
                                                           choices=[('JA','Samtykker'),
                                                                       ('NEI', 'Samtykker IKKE')], max_length=64, error_messages={b'required': 'Samtykker du?.. Vennligst svar..'})),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
            ],
        ),
    ]
