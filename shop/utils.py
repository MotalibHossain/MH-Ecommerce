from shop.models import Catagory, Product


def CatagoryWiseProduct(all_catagory):
    for cat in all_catagory:
        if str(cat) == 'Man':
            all_man = Product.objects.filter(catagory=cat)
        if str(cat) == 'Women':
            all_women = Product.objects.filter(catagory=cat)
    context1 = {
        "all_man": all_man,
        "all_women": all_women,
    }
    return context1