from django import forms
from apply.models import User_apply_profile, Academic

class MajorSelectionForm(forms.ModelForm):
    class Meta:
        model = User_apply_profile
        fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        academic_instance = Academic.objects.get(user=self.instance.user)
        related_majors = academic_instance.get_related_majors()

        for i in range(1, 5):
            field_name = f'major_choice{i}'
            self.fields[field_name] = forms.ModelChoiceField(queryset=related_majors, label=f'{i}순위 전공 선택')

    def clean(self):
        cleaned_data = super().clean()

        # 중복된 선택 확인
        selected_majors = [cleaned_data[f'major_choice{i}'] for i in range(1, 5) if cleaned_data.get(f'major_choice{i}')]
        if len(selected_majors) != len(set(selected_majors)):
            raise forms.ValidationError("중복된 전공 선택이 있습니다.")

        return cleaned_data

