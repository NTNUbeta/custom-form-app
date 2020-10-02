from .models import ExtraInfo
from django.forms import ModelForm

class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['email_gdpr_consent']

    class Meta(object):
        model = ExtraInfo
        fields = ('employment_status','email_gdpr_consent', 'andreas')
        labels = {'email_gdpr_consent':('Subscribe me to NTNU Beta')}
