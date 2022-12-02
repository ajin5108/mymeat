from user.models import Category, Customer
from user.models import SubCategory
from user.models import Product
from user.models import HeaderFlash


def main_context(request):
    headerflash = HeaderFlash.objects.last()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    products = Product.objects.all()
    
    if request.user.is_anonymous:
       
        return {
            "headerflash": headerflash,
            "categories": categories,
            "subcategories": subcategories,
            "products": products,
            "status":0
            }
    else:
       
        return {
            "headerflash": headerflash,
            "categories": categories,
            "subcategories": subcategories,
            "products": products,
            "status":1
            }

