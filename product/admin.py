from django.contrib import admin
from django.utils.html import format_html

from .models import Product, ProductDetail, ProductKeyword, ProductImage, ProductComment


# ProductKeyword Inline
class ProductKeywordInline(admin.TabularInline):
    model = ProductKeyword
    extra = 1  # 默认显示1个空白的form

# 显示图片缩略图的函数
def image_thumbnail(image):
    if image:
        return format_html('<img src="{}" style="width: 100px; height: 100px;" />', image.url)
    return "No Image"

# ProductDetailImage Inline
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # 默认显示1个空白的form
    fields = ('image_thumbnail', 'image')  # 显示缩略图和图片字段
    readonly_fields = ('image_thumbnail',)  # 只读缩略图

    # 自定义方法来显示缩略图
    def image_thumbnail(self, obj):
        return image_thumbnail(obj.image)

    image_thumbnail.short_description = 'Image'  # 设置缩略图列的标题


# ProductDetail Inline
class ProductDetailInline(admin.TabularInline):
    model = ProductDetail

class ProductCommentInline(admin.TabularInline):
    model = ProductComment
    extra = 1

# 自定义Product的Admin界面
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'description')
    search_fields = ('name', 'description')
    list_filter = ('stock',)

    inlines = [ProductImageInline, ProductKeywordInline, ProductDetailInline, ProductCommentInline ]  # 在Product界面中显示ProductDetail Inline

# 自定义ProductDetail的Admin界面
class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ('product', 'detail_description')
    search_fields = ('detail_description',)

# 注册管理界面
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductDetail, ProductDetailAdmin)
admin.site.register(ProductKeyword)
admin.site.register(ProductImage)
