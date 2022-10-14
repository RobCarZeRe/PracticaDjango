from django.contrib import admin
from .models import Persona
admin.site.register(Persona)

from .models import Doctor
admin.site.register(Doctor)

from .models import Paciente
admin.site.register(Paciente)