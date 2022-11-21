from django.http import HttpResponse


def about(request):
    return HttpResponse("Приехал из Свердловской области из Серова, люблю учиться и лениться")

def contacts(request):
    return HttpResponse("https://github.com/SemenGyskov/           89961703779    609 комната")
def index(request):
    return HttpResponse("Гуськов Семён Игоревич 17 лет играю на гитаре")
# Create your views here.
