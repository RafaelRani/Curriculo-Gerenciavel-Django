from django.contrib import admin
from .models import Sobre
from .models import Experiencia
from .models import Escolaridade
from .models import Skill
from .models import Objetivo
from .models import Curso
from .models import Complementar

admin.site.register(Sobre)
admin.site.register(Experiencia)
admin.site.register(Escolaridade)
admin.site.register(Skill)
admin.site.register(Objetivo)
admin.site.register(Curso)
admin.site.register(Complementar)