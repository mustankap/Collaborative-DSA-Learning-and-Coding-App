from django.shortcuts import render


def chatRoom(request, room_name):
    return render(request, "chat/chat_view.html", {"room_name": room_name})
