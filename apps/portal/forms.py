from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


User = get_user_model()


class SignupForm(forms.ModelForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        min_length=8,
    )
    password2 = forms.CharField(
        label=" Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        min_length=8,
    )

    # user_type field to select the role
    role = forms.ChoiceField(
        choices=User.ROLE_CHOICES, widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = CustomUser
        fields = ["email", "role"]
        widgets = {
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Enter Your Email"}
            ),
        }
        labels = {"email": "Email Address"}

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email="email").exists():
            raise ValidationError("This email already registered")
        return email

    def clean_password(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password Do Not Match")
        if len(password1) < 8:
            raise ValidationError("Password Must Be at Least 8 Character")
        if password1.isdigit():
            raise ValidationError("Password cannot be entirely numeric")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        # user.username = user.email
        user.username = self.cleaned_data["email"]  # optional
        user.role = self.cleaned_data["role"]  # save role
        if commit:
            user.save()
        return user


# class SignupForm(UserCreationForm):
#     """
#     Custom form for the first step of registration (Sign Up).
#     Inherits from Django's secure UserCreationForm to handle username,
#     password, and confirmation password validation.

#     The 'email' field is added here.
#     """

#     email = forms.EmailField(
#         label="Email Address",
#         max_length=254,
#         required=True,
#         help_text="Required. Used for account recovery and communication.",
#     )

#     class Meta(UserCreationForm.Meta):
#         # UserCreationForm.Meta.fields is ('username', 'password', 'password2')
#         # We explicitly include 'username' and 'email' first, followed by the passwords.
#         fields = ("username", "email") + UserCreationForm.Meta.fields[1:]


# class UserProfileForm(forms.Form):
#     """
#     A simple form for collecting extended user details (e.g., address, phone)
#     after a successful signup. This form is used in the 'user_registration' view.
#     """

#     address = forms.CharField(label="Address Line 1", max_length=100)
#     city = forms.CharField(label="City", max_length=50)
#     phone_number = forms.CharField(
#         label="Phone Number", max_length=15, help_text="e.g., +1-555-123-4567"
#     )

# Note: In a real-world application, this form would typically be a ModelForm
# linked to a UserProfile model.
