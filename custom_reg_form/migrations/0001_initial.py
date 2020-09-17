from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                #('velge', models.CharField(blank=False, choices=[(b'JA',b'Samtykker'), (b'NEI', b'Samtykker IKKE'),],
                       #verbose_name=b'Jeg godtar NTNUs betingelser om marketsforing ', max_length=64 )),
                ('samtykke',models.BooleanField(default=True)), 
                #('baretest',models.TextField()),                  
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE)),
            ],
        ),
    ]
