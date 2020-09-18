from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.translation import ugettext_noop


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
                ('samtykke',models.BooleanField(default=True)), 
                ('employment_status', models.CharField(verbose_name=b"Employment Status", blank=True, null=True, max_length=20, db_index=True,
                choices= [ (b'efw', ugettext_noop(b'Employed for wages')),
                        (b'selfemployed', ugettext_noop(b'Self-employed')),
                        (b'student', ugettext_noop(b'Student')),
                        (b'homemaker', ugettext_noop(b'Homemaker')),
                        (b'oowlfw', ugettext_noop(b'Out of work and looking for work')),
                        (b'oownclfw', ugettext_noop(b'Out of work but not currently looking for work')),
                        (b'military', ugettext_noop(b'Military')),
                        (b'retired', ugettext_noop(b'Retired')),
                        (b'utw', ugettext_noop(b'Unable to work')),
                        (b'other', ugettext_noop(b'Other')),]
                )),
                #('email', models.EmailField(max_length=100,verbose_name=b"Please confirm your e-mail")),
                ('email', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL,related_name='email+',on_delete=models.CASCADE)),
                                
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL, related_name='user+', on_delete=models.CASCADE)),
            ],
        ),
    ]
