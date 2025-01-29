from django.db import models
from django.contrib.auth.models import User

# カテゴリモデル
class Category(models.Model):
    CATEGORY_CHOICES = [
        ("all","すべて"),
        ("books","本"),
        ("electronics","電子機器"),
     ]



    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name

# 商品モデル
class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.name

# 検索履歴モデル
class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Djangoの標準ユーザーモデルを参照
    query = models.CharField(max_length=255)
    searched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.query}"

