from .models import ExtraInfo
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
import logging





class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)        
        self.fields['samtykke'].required=True
        #self.fields['email']
        self.fields['employment_status'].error_messages = {
            "required": u"Please tell us your employment status",
            "invalid": u"Enter correct employment status",
            }   

    class Meta(object):
        model = ExtraInfo
        fields = ('samtykke','employment_status',)
        labels = {'samtykke': _("Jeg samtykker til å motta markedsføring og kommunikasjon på e-post fra NTNU"),}
        help_texts = {'samtykke': _('Vennligst svar.'),}
        
