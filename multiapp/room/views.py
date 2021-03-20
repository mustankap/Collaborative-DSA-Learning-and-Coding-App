from django.shortcuts import render

# Create your views here.
def preroomView(request):
    return render(request, "room/preroom_view.html")


def roomView(request, room_name):
    return render(request, "room/room_view.html", {"room_name": room_name})