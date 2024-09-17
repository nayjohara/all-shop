from django.forms import ModelForm
from main.models import AllShop

class ProductEntryForm(ModelForm):
    class Meta:
        model = AllShop
        fields = ["name", "price", "description"]