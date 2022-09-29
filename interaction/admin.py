from django.contrib import admin
from .models import Messenger, Participant, InteractionConnection


admin.site.register(Participant)
admin.site.register(InteractionConnection)
admin.site.register(Messenger)