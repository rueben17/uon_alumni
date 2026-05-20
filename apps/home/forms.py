from django import forms
from apps.home.models import AlumniProfile, Faculty, MembershipTier
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class HelpTextStyledMixin:
    help_text_class = "text-xs font-light text-gray-500 "

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            if field.help_text:
                field.help_text = mark_safe(f'<span class="{self.help_text_class}">{field.help_text}</span>')


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    confirm_email = forms.EmailField(label="Confirm email address", required=True)
    

    class Meta:
        model = User
        fields = ['username', 'email', 'confirm_email', 'password1', 'password2',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply your custom CSS classes
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'w-full px-3 text-sm  py-1 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 
            })

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        confirm_email = cleaned_data.get('confirm_email')
        
        if email and confirm_email and email != confirm_email:
            raise forms.ValidationError("Emails do not match")
        
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user



# class AlumniRegistrationForm(forms.ModelForm):
#     agree_terms = forms.BooleanField(label='I confirm that the information provided is correct')

#     class Meta:
#         model = AlumniProfile
#         fields = [
#             'title', 'surname', 'first_name', 'middle_name', 'maiden_name',
#             'gender', 'date_of_birth', 'id_passport_no', 'nationality',
#             'postal_address', 'postal_code', 'city', 'phone_mobile', 'phone_alt', 'email',
#             'graduation_year', 'faculty', 'student_reg_no',
#             'receive_newsletter', 'receive_sms_alerts'
#         ]
#         widgets = {
#             'title': forms.Select(attrs={'class': 'w-full px-3 text-sm py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
#             'surname': forms.TextInput(attrs={'class': 'w-full px-3 text-sm  py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Surname'}),
#             'first_name': forms.TextInput(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'First Name'}),
#             'middle_name': forms.TextInput(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Middle Name'}),
#             'maiden_name': forms.TextInput(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Maiden Name'}),
#             'gender': forms.Select(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
#             'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
#             'id_passport_no': forms.TextInput(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'ID/Passport Number'}),
#             'nationality': forms.TextInput(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Nationality'}),
#             'postal_address': forms.TextInput(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
#             'postal_code': forms.TextInput(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
#             'city': forms.TextInput(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
#             'phone_mobile': forms.TextInput(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
#             'phone_alt': forms.TextInput(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
#             'email': forms.EmailInput(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
#             'graduation_year': forms.NumberInput(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
#             'faculty': forms.Select(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
#             'student_reg_no': forms.TextInput(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
#             'receive_newsletter': forms.CheckboxInput(attrs={'class': 'rounded border-gray-300 text-blue-600 focus:ring-blue-500'}),
#             'receive_sms_alerts': forms.CheckboxInput(attrs={'class': 'rounded border-gray-300 text-blue-600 focus:ring-blue-500'}),
#         }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         # Add placeholders and help texts
#         placeholders = {
#             'surname': 'e.g., Doe',
#             'first_name': 'e.g., John',
#             'email': 'your.email@example.com',
#             'phone_mobile': '+1234567890',
#             'student_reg_no': 'e.g., S12345',
#         }
#         for field, placeholder in placeholders.items():
#             if field in self.fields:
#                 self.fields[field].widget.attrs['placeholder'] = placeholder

#         help_texts = {
#             'email': 'We will send your alumni ID to this address.',
#             'student_reg_no': 'Your student registration number (if you remember it).',
#         }
#         for field, text in help_texts.items():
#             self.fields[field].help_text = text

#         # Make some fields optional
#         self.fields['middle_name'].required = False
#         self.fields['maiden_name'].required = False
#         self.fields['phone_alt'].required = False

class AlumniRegistrationForm(forms.ModelForm):
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
            'title': forms.Select(attrs={'class': 'w-full px-3 text-sm py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'surname': forms.TextInput(attrs={'class': 'w-full px-3 text-sm py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Surname'}),
            'first_name': forms.TextInput(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'First Name'}),
            'middle_name': forms.TextInput(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Middle Name'}),
            'maiden_name': forms.TextInput(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Maiden Name'}),
            'gender': forms.Select(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'id_passport_no': forms.TextInput(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'ID/Passport Number'}),
            'nationality': forms.TextInput(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Nationality'}),
            'postal_address': forms.TextInput(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'postal_code': forms.TextInput(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'city': forms.TextInput(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'phone_mobile': forms.TextInput(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'phone_alt': forms.TextInput(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'graduation_year': forms.NumberInput(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'faculty': forms.Select(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'student_reg_no': forms.TextInput(attrs={'class': 'w-full px-3 py-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'receive_newsletter': forms.CheckboxInput(attrs={'class': 'rounded border-gray-300 text-blue-600 focus:ring-blue-500'}),
            'receive_sms_alerts': forms.CheckboxInput(attrs={'class': 'rounded border-gray-300 text-blue-600 focus:ring-blue-500'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Apply model validators to form fields
        self.fields['phone_mobile'].validators = AlumniProfile._meta.get_field('phone_mobile').validators

        # Set placeholders
        placeholders = {
            'surname': 'e.g., Doe',
            'first_name': 'e.g., John',
            'email': 'your.email@example.com',
            'phone_mobile': '254712345678',
            'student_reg_no': 'e.g., S12345',
        }
        for field, placeholder in placeholders.items():
            if field in self.fields:
                self.fields[field].widget.attrs['placeholder'] = placeholder

        # Set help texts
        help_texts = {
            'email': 'We will send your alumni ID to this address.',
            'student_reg_no': 'Your student registration number (if you remember it).',
            'phone_mobile': 'Enter Kenyan phone number (e.g., 254712345678)',
        }
        for field, text in help_texts.items():
            self.fields[field].help_text = text

        # Make fields optional (matching model's blank=True)
        optional_fields = ['middle_name', 'maiden_name', 'phone_alt', 'postal_address', 
                          'postal_code', 'city', 'graduation_year', 'student_reg_no']
        for field in optional_fields:
            self.fields[field].required = False

    # def clean_email(self):
    #     """Ensure email is unique across both User and AlumniProfile"""
    #     email = self.cleaned_data.get('email')
        
    #     # Check User model
    #     if User.objects.filter(email=email).exists():
    #         raise ValidationError('A user with this email already exists.')
        
    #     # Check AlumniProfile but exclude profiles linked to the current user
    #     # Since user doesn't exist yet, we can't check this during registration
    #     # Only check when updating an existing profile
    #     if self.instance and self.instance.pk:
    #         if AlumniProfile.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
    #             raise ValidationError('An alumni profile with this email already exists.')
        
    #     return email

    def clean_id_passport_no(self):
        """Ensure ID/Passport is unique"""
        id_no = self.cleaned_data.get('id_passport_no')
        if AlumniProfile.objects.filter(id_passport_no=id_no).exclude(pk=self.instance.pk).exists():
            raise ValidationError('An alumni profile with this ID/Passport number already exists.')
        return id_no


class MembershipPaymentForm(forms.Form):
    membership_tier = forms.ModelChoiceField(
        queryset=MembershipTier.objects.filter(is_active=True),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'hx-get': reverse_lazy('home:get_tier_details'),
            'hx-target': '#tier-details'
        }),
        error_messages={'required': 'Please select a membership tier.'}
    )
    payment_method = forms.ChoiceField(
        choices=[
            ('mpesa', 'M-Pesa'),
            ('credit_card', 'Credit/Debit Card'),
            ('bank_transfer', 'Bank Transfer')
        ],
        widget=forms.RadioSelect(attrs={'class': 'payment-method-radio'}),
        required=True
    )
    # M-Pesa
    mpesa_number = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0712345678'}))
    # Credit card
    card_number = forms.CharField(max_length=19, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1234 5678 9012 3456'}))
    expiry = forms.CharField(max_length=5, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MM/YY'}))
    cvv = forms.CharField(max_length=4, required=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '123'}))
    # Bank transfer
    transaction_ref = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'TRX-123456'}))
    bank_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'KCB'}))

    def clean(self):
        cleaned = super().clean()
        method = cleaned.get('payment_method')
        if method == 'mpesa' and not cleaned.get('mpesa_number'):
            self.add_error('mpesa_number', 'M-Pesa number required.')
        elif method == 'credit_card':
            if not cleaned.get('card_number'):
                self.add_error('card_number', 'Card number required.')
            if not cleaned.get('expiry'):
                self.add_error('expiry', 'Expiry date required.')
            if not cleaned.get('cvv'):
                self.add_error('cvv', 'CVV required.')
        elif method == 'bank_transfer' and not cleaned.get('transaction_ref'):
            self.add_error('transaction_ref', 'Transaction reference required.')
        return cleaned