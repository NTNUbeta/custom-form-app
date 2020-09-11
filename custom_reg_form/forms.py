from .models import ExtraInfo
from django.forms import ModelForm

class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['samtykke'].error_messages = {
            "required": u"Samtykker du?.. Vennligst svar..",

        }

    class Meta(object):
        model = ExtraInfo
        fields = ('samtykke')
