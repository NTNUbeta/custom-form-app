from .models import ExtraInfo
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        #self.fields['samtykke']
        self.fields['samtykke'].error_messages = {
            "required": u"Vennligst velg",
            "invalid": u"Den felt kan ikke vaare tom",}
        self.fields['velge']    

    class Meta(object):
        model = ExtraInfo
        fields = ('samtykke','velge',)
        labels = {'samtykke': _('Andreas her du kan plasere text hva du vil'),}
        help_texts = {'samtykke': _('Vennligst svar.'),}
