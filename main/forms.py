from django.forms import ModelForm
from main.models import AllShop
from django.utils.html import strip_tags

class ProductEntryForm(ModelForm):
    class Meta:
        model = AllShop
        fields = ["name", "price", "description"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)
    
    def cleand_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)