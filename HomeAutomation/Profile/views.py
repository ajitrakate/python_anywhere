from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Profile.models import Boards, Button
from Board_handller.models import Boards_required, Button_required
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
import datetime
from django.utils import timezone
from django.contrib import messages

# Create your views here.
@login_required()
def dashboard(request):
    user = request.user
    kits = user.boards_set.all()
    # n = len(kits)
    # dev_boards = {}
    # for i in range(n):
    #     j = str(i)
    #     dev_boards[j] = kits[i].button_set.all()
    context = {'kits':kits}
        
    
    return render(request, 'dashboard.html', context)

def buttons(request, pk):
    dev_board = Boards.objects.filter(pk=pk) 
    dev_board1 = dev_board[0]
    # button_list = dev_board.button_set.all()
    button_list = Button.objects.filter(Board=dev_board1)
    #print(button_list)
    context = {'buttons': button_list, 'next':pk }
    return render(request, 'buttons.html', context)


def change_status(request, pk, id):
    board = Boards_required.objects.filter(pk=pk)
    dev_board = board[0]
    button1 = dev_board.button_required_set.filter(id=id)
    button = button1[0]
    new_status =  request.POST[f'{button.name}']
    button.status = new_status
    button.last_updated = datetime.datetime.now()
    button.save()
    board_for_message = Boards.objects.filter(pk=pk)[0] 
    button_for_message = Button.objects.filter(id=id)[0]
    current_status = button_for_message.status
    messages.success(request,f'The status of {button.name} has been requested to change from {current_status} to {button.status}')
    return redirect('dashboard')


