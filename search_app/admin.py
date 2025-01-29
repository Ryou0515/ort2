# search_app/admin.py

from django.contrib import admin
from django.contrib.auth.models import User  # Django標準のUserモデルをインポート
from .models import Product, Category, SearchHistory

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SearchHistory)
