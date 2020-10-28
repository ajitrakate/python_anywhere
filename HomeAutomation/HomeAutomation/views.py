from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from Profile.models import Boards, Button
from Board_handller.models import Boards_required, Button_required
import datetime 
import json


def post_data(request, username, pk):
    if request.method == "POST":
        user = get_object_or_404(User, username=username)
        board = user.boards_set.filter(pk=pk)[0]
        buttons = board.button_set.all()
        for button in buttons:
            button.status = request.POST[f'{button.id}']
            button.last_updated = button.last_updated = datetime.datetime.now()
            button.save()
        board_required = user.boards_required_set.filter(pk=pk)[0]
        buttons_required = board_required.button_required_set.all()
        print(buttons_required)
        output = {}
        for b in buttons_required:
            output[f'{b.name}'] = b.status
        #output = {'board_required': 'buttons_required', 'buttons_required':'buttons_required'}
        json_str = json.dumps(output)
        return HttpResponse(json_str, content_type='text/plain')
        
        
        return HttpResponse("Success")
    try:
        user = get_object_or_404(User, username=username)
        board = user.boards_set.filter(pk=pk)[0]
    except:
        return HttpResponseNotFound("Page not found")

    buttons = board.button_set.all()
    context = {'buttons': buttons}

    return render(request, 'home/post_data.html', context)