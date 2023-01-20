from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
      title       = forms.CharField()
      #email       = forms.EmailField()
      description = forms.CharField(required=False, widget=forms.Textarea(attrs={
            "cols":20,
            "rows":10
      }))
      price       = forms.DecimalField(initial=199.99)
      class Meta:
            model = Product
            fields = [
                  "title",
                  "description",
                  "price"
            ]
      # def clean_title(self,*args, **kwargs):
      #       title = self.cleaned_data.get("title")
      #       if not "Nehemiah" in title:
      #             raise forms.ValidationError("This is not a valid title")
      #       if not "Bosire" in title:
      #             raise forms.ValidationError("This is not a valid title")
      #       else:
      #             return title
      # def clean_email(self, *args, **kwargs):
      #       email = self.cleaned_data.get("email")
      #       if not email.endswith(".com"):
      #             raise forms.ValidationError("This is not a valid email")
      #       else:
      #             return email



class RawForm(forms.Form):
      title       = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Your BestLaptop"}))
      description = forms.CharField(widget=forms.Textarea(attrs={
            "cols":20,
            "rows":10
      }))
      price       = forms.DecimalField()

