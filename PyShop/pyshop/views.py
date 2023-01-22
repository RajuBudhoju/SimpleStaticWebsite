from django.shortcuts import render


# def home(request):
#     return render(request, 'home.html')


def home(request):
    # pyshop = Pyshop.objects.all()
    # return render(request, 'home.html', {'pyshop': pyshop})
    # return HttpResponse("Fruits")
    return render(request, 'home.html')
