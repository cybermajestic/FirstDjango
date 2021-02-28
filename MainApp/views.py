from django.shortcuts import render, HttpResponse, Http404
from MainApp.models import Item

# Create your views here.
"""
Имя: Иван
Отчество: Петрович
Фамилия: Иванов
телефон: 8-923-600-01-02
email: vasya@mail.ru
"""
name = "Павел"
middlename = "Михайлович"
secondname = "Алимпиев"
phone = "+7123456789"
email = "email@email.com"


# items = [
#    {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
#    {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
#    {"id": 3, "name": "Coca-cola 1 литр" ,"quantity":12},
#    {"id": 4, "name": "Картофель фри" ,"quantity":0},
#    {"id": 5, "name": "Кепка" ,"quantity":124},
# ]






def main(request):
    return render(request, 'index.html')


def about(request):
    text = f"""
    Имя: <b>{name}</b>
    Отчество: <b>{middlename}</b><br>
    Фамилия: <b>{secondname}</b><br>
    Телефон: <b>{phone}</b><br>
    email: <b>{email}</b><br>
    """
    return HttpResponse(text)


def item(request, item=1):
    try:
        items_all = Item.objects.get(id=item)
    except:
        raise Http404
    context = {
        "item": items_all
    }
    return render(request, "item.html", context)

def items_list(request):
    item = Item.objects.all()
    context = {
        "items": item
    }
    return render(request, "items.html", context)