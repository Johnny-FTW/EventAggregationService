from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, DateInput, TimeInput, DateTimeInput
from django.http import request

from EventViewer.models import Event


class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class MyDateInput(DateTimeInput):
    input_type = 'datetime-local'
    def __int__(self,*args, **kwargs):
        # kwargs['format'] = '%d.%m.%Y %H:%M'
        super().__init__(*args, **kwargs)





class EventForm(ModelForm):
    def __init__(self, *args, **kwargs):
        # kwargs["input_formats"]='%d.%m.%Y %H:%M'
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Event
        exclude = ['user_attend','user_creator']
        widgets = {
            'start_at': MyDateInput(),
            'end_at': MyDateInput(),
        }

    # def add_user_creator(self):
    #     user = User.objects.get(user=request.user)
    #     user_creator = user

