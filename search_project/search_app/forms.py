from django import forms
from .models import Product

# 検索フォーム
class SearchForm(forms.Form):
    query = forms.CharField(
        label='検索キーワード',
        max_length=100,  # CharField で max_length が有効です
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '検索したいキーワードを入力'})  # widgetのインデントを修正
    )

# 商品フォーム
class ProductForm(forms.ModelForm):
    class Meta:  # Mera → Meta に修正
        model = Product
        fields = ['name', 'description', 'price']
