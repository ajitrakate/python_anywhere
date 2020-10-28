# from django.db.models.signals import post_save
# from django.dispatch import receiver
# # from HomeAutomation.Profile.models import Boards
# # from HomeAutomation.Profile.models import Button
# from Profile.models import Boards, Button
# from .models import Boards_required, Button_required


# @receiver(post_save, sender=Boards)
# def create_board(sender,instance,created,**kwargs):
#     if created:
#         Boards_required.objects.create(owner=instance.owner, name=instance.name, desc=instance.desc ,manufacturer_name=instance.manufacturer_name,last_updated=instance.last_updated)

# @receiver(post_save, sender=Boards)
# def save_board(sender,instance,**kwargs):
#     #instance.Boards_required.save()
#     Boards_required.save(instance)



# @receiver(post_save, sender=Button)
# def create_button(sender, instance, created, **kwargs):
#     if created:
#         Button_required.objects.create(Board=instance.Board, name=instance.name, desc=instance.desc, status=instance.status, pin_no=instance.pin_no, last_updated=instance.last_updated)

# @receiver(post_save, sender=Button)
# def save_button(sender, instance, **kwargs):
#     instance.Button_required.save()