from django.shortcuts import render
from .models import Sobre, Experiencia, Escolaridade, Skill, Objetivo, Curso, Complementar
from datetime import datetime

def curriculo(request):
    sobre = Sobre.objects.all()
    experiencia = Experiencia.objects.all()
    escolaridade = Escolaridade.objects.all()
    skill = Skill.objects.all()
    objetivo = Objetivo.objects.all()
    curso = Curso.objects.all()
    complementar = Complementar.objects.all()

    # calculando a idade
    now = datetime.now() #obtendo a data atual
    for sb in sobre:
        idade = now.year - sb.nascimento.year #idade = data atual - ano de nascimento
        #se o mês de nascimento for menor que o mês atual e o dia de nascimetno menor que o dia atual, subtrai 1 da idade
        if now.month < sb.nascimento.month and now.day < sb.nascimento.day:
            idade = idade - 1

    info = {
        'sobre': sobre,
        'experiencia': experiencia, 
        'escolaridade': escolaridade,
        'skill': skill,
        'objetivo': objetivo,
        'curso': curso,
        'complementar': complementar,
        'idade': idade
    }

    return render(request, 'index.html', info)