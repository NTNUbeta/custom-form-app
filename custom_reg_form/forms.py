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
        #self.fields['velge'].error_messages = {
            #"required": u"Vennligst velg",
            #"invalid": u"Den felt kan ikke vaare tom",}
        self.fields['samtykke'].required=True   

    class Meta(object):
        model = ExtraInfo
        fields = ('samtykke',)
        labels = {'samtykke': _("Jeg samtykker til å motta markedsføring og kommunikasjon på e-post fra NTNU"),}
        help_texts = {'samtykke': _('Vennligst svar.'),}
        
