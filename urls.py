from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_view, name='search_view'),  # デフォルトで検索ページへ
    path('search/', views.search_view, name='search_view'),

    path('product/', views.product_list, name='product_list'),  # 商品一覧
    path('product/new/', views.product_create, name='product_create'),  # 商品作成
    path('product/<int:pk>/', views.product_detail, name='product_detail'),  # 商品詳細
    path('product/<int:pk>/edit/', views.product_update, name='product_update'),  # 商品編集
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),  # 商品削除
]
