from django import forms
from apps.home.models import AlumniProfile, Faculty, MembershipTier
from django.utils.safestring import mark_safe
class HelpTextStyledMixin:
    help_text_class = "text-xs font-light text-gray-500 "

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            if field.help_text:
                field.help_text = mark_safe(f'<span class="{self.help_text_class}">{field.help_text}</span>')


class TailwindFormMixin:
    """Apply login_input class to all fields by default"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            # Skip checkboxes/radios - they need different styling
            if not isinstance(field.widget, (forms.CheckboxInput, forms.RadioSelect)):
                current_class = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f'login_input {current_class}'.strip()
                

class AlumniRegistrationForm(HelpTextStyledMixin, TailwindFormMixin, forms.ModelForm):
    confirm_email = forms.EmailField()
    agree_terms = forms.BooleanField(label='I confirm that the information provided is correct')

    class Meta:
        model = AlumniProfile
        fields = [
            'title', 'surname', 'first_name', 'middle_name', 'maiden_name',
            'gender', 'date_of_birth', 'id_passport_no', 'nationality',
            'postal_address', 'postal_code', 'city', 'phone_mobile', 'phone_alt', 'email',
            'graduation_year', 'faculty', 'student_reg_no',
            'receive_newsletter', 'receive_sms_alerts'
        ]
        widgets = {
            'title': forms.Select(attrs={'class': ''}),
            'surname': forms.TextInput(attrs={'class': ''}),
            'first_name': forms.TextInput(attrs={'class': ''}),
            'middle_name': forms.TextInput(attrs={'class': ''}),
            'maiden_name': forms.TextInput(attrs={'class': ''}),
            'gender': forms.Select(attrs={'class': ''}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': ''}),
            'id_passport_no': forms.TextInput(attrs={'class': ''}),
            'nationality': forms.TextInput(attrs={'class': ''}),
            'postal_address': forms.TextInput(attrs={'class': ''}),
            'postal_code': forms.TextInput(attrs={'class': ''}),
            'city': forms.TextInput(attrs={'class': ''}),
            'phone_mobile': forms.TextInput(attrs={'class': ''}),
            'phone_alt': forms.TextInput(attrs={'class': ''}),
            'email': forms.EmailInput(attrs={'class': ''}),
            'graduation_year': forms.NumberInput(attrs={'class': ''}),
            'faculty': forms.Select(attrs={'class': ''}),
            'student_reg_no': forms.TextInput(attrs={'class': ''}),
            'receive_newsletter': forms.CheckboxInput(attrs={'class': 'rounded border-gray-300 text-blue-600 focus:ring-blue-500'}),
            'receive_sms_alerts': forms.CheckboxInput(attrs={'class': 'rounded border-gray-300 text-blue-600 focus:ring-blue-500'}),
        }

class AlumniRegistrationForm(forms.ModelForm):
    confirm_email = forms.EmailField()
    agree_terms = forms.BooleanField(label='I confirm that the information provided is correct')

    class Meta:
        model = AlumniProfile
        fields = [
            'title', 'surname', 'first_name', 'middle_name', 'maiden_name',
            'gender', 'date_of_birth', 'id_passport_no', 'nationality',
            'postal_address', 'postal_code', 'city', 'phone_mobile', 'phone_alt', 'email',
            'graduation_year', 'faculty', 'student_reg_no',
            'receive_newsletter', 'receive_sms_alerts'
        ]
        widgets = {
            'title': forms.Select(attrs={'class': ''}),
            'surname': forms.TextInput(attrs={'class': ''}),
            'first_name': forms.TextInput(attrs={'class': ''}),
            'middle_name': forms.TextInput(attrs={'class': ''}),
            'maiden_name': forms.TextInput(attrs={'class': ''}),
            'gender': forms.Select(attrs={'class': ''}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': ''}),
            'id_passport_no': forms.TextInput(attrs={'class': ''}),
            'nationality': forms.TextInput(attrs={'class': ''}),
            'postal_address': forms.TextInput(attrs={'class': ''}),
            'postal_code': forms.TextInput(attrs={'class': ''}),
            'city': forms.TextInput(attrs={'class': ''}),
            'phone_mobile': forms.TextInput(attrs={'class': ''}),
            'phone_alt': forms.TextInput(attrs={'class': ''}),
            'email': forms.EmailInput(attrs={'class': ''}),
            'graduation_year': forms.NumberInput(attrs={'class': ''}),
            'faculty': forms.Select(attrs={'class': ''}),
            'student_reg_no': forms.TextInput(attrs={'class': ''}),
            'receive_newsletter': forms.CheckboxInput(attrs={'class': 'rounded border-gray-300 text-blue-600 focus:ring-blue-500'}),
            'receive_sms_alerts': forms.CheckboxInput(attrs={'class': 'rounded border-gray-300 text-blue-600 focus:ring-blue-500'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        confirm = cleaned_data.get('confirm_email')
        if email and confirm and email != confirm:
            raise forms.ValidationError("Email addresses do not match.")
        return cleaned_data