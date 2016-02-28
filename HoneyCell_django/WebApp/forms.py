from django import forms

from WebApp.models import *

class FooModelForm(forms.ModelForm):
    class Meta:
        model = Foo

        fields = ['foo_name', 'foo_description',]

        widgets = {'foo_name': forms.TextInput,
                   'foo_description': forms.Textarea}

    def clean(self):
        cleaned_data = super(FooModelForm, self).clean()

        print(cleaned_data.get('foo_name'))
        print(cleaned_data.get('foo_description'))

        return cleaned_data

    def clean_foo_name(self):
        foo_name = self.cleaned_data.get('foo_name')

        if not foo_name:
            print("Please type in the foo_name.")
            raise forms.ValidationError("Please type in the foo_name.")

        return foo_name

    def clean_foo_description(self):
        foo_description = self.cleaned_data.get('foo_description')

        if not foo_description:
            print("Please type in the foo_description.")
            raise forms.ValidationError("Please type in the foo_description.")

        return foo_description