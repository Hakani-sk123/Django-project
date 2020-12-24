from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def cookie_data(request):
    name = request.GET.get("na")
    price = request.GET.get("price")

    data = {"total_cookies":len(request.COOKIES)}
    response = render(request,"index.html",data)

    response.set_cookie(key=name,value=price)
    return response


def show_cookies(request):
    data = {"total_cookies": len(request.COOKIES),"cookie":request.COOKIES}
    return render(request,"cokkies.html",data)


def delete_cookie(request):
    cookie_key = request.GET.get("cn")
    response = show_cookies(request)
    response.delete_cookie(cookie_key)
    return response