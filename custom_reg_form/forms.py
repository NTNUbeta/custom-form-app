from .models import ExtraInfo
from django.forms import ModelForm

class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['Jeg_samtykker_til_motta_markedsforing_kommunikasjon_epost_fra_NTNU']
        #self.fields['samtykke'].error_messages = {
            #"required": u"Vennligst velg",
           # "invalid": u"Den felt kan ikke vaare tom",}

    class Meta(object):
        model = ExtraInfo
        fields = ('Jeg_samtykker_til_motta_markedsforing_kommunikasjon_epost_fra_NTNU ')
