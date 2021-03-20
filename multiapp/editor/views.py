from django.shortcuts import render

# Create your views here.
def Edit(request, room_name):
    return render(request, "editor/editor_view.html", {"room_name": room_name})
