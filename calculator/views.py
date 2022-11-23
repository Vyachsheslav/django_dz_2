from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }



def omlet(request):
    count = int(request.GET.get('servings', 1))
    context = {'omlet': {
        'яйца, шт': 2*count,
        'молоко, л': round(0.1*count,2),
        'соль, ч.л.': 0.5*count
    }}

    return render(request, 'calculator/omlet.html', context)


def pasta(request):
    count = int(request.GET.get('servings', 1))
    context = {'pasta': {
        'макароны, г': round(0.3*count,2),
        'сыр, г': round(0.05*count,2)
    }}

    return render(request, 'calculator/pasta.html', context)

def buter(request):
    count = int(request.GET.get('servings', 1))
    context = {'buter': {
        'хлеб, ломтик': 1*count,
        'колбаса, ломтик': 1*count,
        'сыр, ломтик': 1*count,
        'помидор, ломтик': 1*count,
    }}

    return render(request, 'calculator/buter.html', context)



