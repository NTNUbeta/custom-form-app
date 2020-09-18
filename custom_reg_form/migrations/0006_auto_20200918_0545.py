# Generated by Django 2.2.15 on 2020-09-18 05:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_reg_form', '0005_auto_20200918_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='email',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='++ExtraInfo.email++', related_query_name='User.email', to=settings.AUTH_USER_MODEL),
        ),
    ]