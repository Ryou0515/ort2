from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import ProductForm, SearchForm
from django.core.paginator import Paginator
from django.http import Http404

# 商品作成ビュー
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # 商品一覧ページにリダイレクト
    else:
        form = ProductForm()

    return render(request, 'search_app/product_form.html', {'form': form})

# 商品編集ビュー
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)

    return render(request, 'search_app/product_form.html', {'form': form, 'product': product})

# 商品検索ビュー
def search_view(request):
    form = SearchForm(request.GET or None)
    results = Product.objects.all()
    selected_category = None
    sort_by = request.GET.get('sort', 'name')

    if form.is_valid():
        query = form.cleaned_data.get('query', '')
        if query:
            results = results.filter(name__icontains=query)

        category_id = request.GET.get('category')
        if category_id:
            selected_category = get_object_or_404(Category, id=category_id)
            results = results.filter(category=selected_category)

        # 価格フィルタリング
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        try:
            if min_price:
                results = results.filter(price__gte=float(min_price))
            if max_price:
                results = results.filter(price__lte=float(max_price))
        except ValueError:
            pass  # 無効な価格フィルタは無視

        # 並び替え
        if sort_by == 'price_asc':
            results = results.order_by('price')
        elif sort_by == 'price_desc':
            results = results.order_by('-price')
        else:
            results = results.order_by('name')

    # ページネーション
    paginator = Paginator(results, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'search_app/search.html', {
        'form': form,
        'page_obj': page_obj,
        'sort_by': sort_by,
        'selected_category': selected_category,
        'categories': Category.objects.all(),
    })

# 商品詳細ビュー
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'search_app/product_detail.html', {'product': product})

# 商品削除ビュー
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')

    return render(request, 'search_app/product_confirm_delete.html', {'product': product})

# 商品一覧ビュー（ページネーション付き）
def product_list(request):
    products = Product.objects.all()

    # ページネーション
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'search_app/product_list.html', {
        'page_obj': page_obj,
        'categories': Category.objects.all(),  # サイドバーにカテゴリを表示する場合に使用
    })
