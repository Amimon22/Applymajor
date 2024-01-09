from django import forms
from .models import Academic, Apply, Departure_Major_Code

class MajorForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['first_choice', 'second_choice', 'third_choice', 'fourth_choice']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(MajorForm, self).__init__(*args, **kwargs)
        for field in ['first_choice', 'second_choice', 'third_choice', 'fourth_choice']:
            self.fields[field].choices = [
                (major, major) for major in Departure_Major_Code.departments_majors_codes[Academic.instance.major]
            ]

    def clean(self):
        cleaned_data = super().clean()
        choices = [cleaned_data.get(choice) for choice in ['first_choice', 'second_choice', 'third_choice', 'fourth_choice']]
        if len(choices) != len(set(choices)):
            raise forms.ValidationError("중복된 전공을 선택하셨습니다. 다른 전공을 선택해주세요.")
