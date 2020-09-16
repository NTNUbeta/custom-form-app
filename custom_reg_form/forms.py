from .models import ExtraInfo
from django.forms import ModelForm

class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['employment_status'].error_messages = {
            "required": u"Please tell us your employment status",
            "invalid": u"Enter correct employment status",
            },

    class Meta(object):
        model = ExtraInfo
        fields = ('employment_status','email_gdpr_consent',)
