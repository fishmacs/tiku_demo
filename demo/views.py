#encoding=utf8

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

import models


@csrf_exempt
def question_list(request):
    if 'submit' in request.POST:
        grade = request.POST.get('grade')
        subject = request.POST.get('subject')
        search = request.POST.get('search')
        return HttpResponseRedirect('/questions?grade=%s&subject=%s&search=%s' % (grade, subject, search))
    else:
        grade = request.GET.get('grade', '1')
        subject = request.GET.get('subject', 'yw')
        search = request.GET.get('search', '')
        question_model = getattr(models, subject.upper() + 'Question')
        # qs = info_model.objects.filter(grade_id=int(grade))
        # qs = question_model.objects.filter(gid__in=[q.gid for q in qs])
        qs = question_model.objects.filter(info__grade_id=int(grade))
        if search:
            qs = qs.filter(info__zh_knowledge__icontains=search)
        return render(request, 'question_list.html', {
            'questions': qs,
            'grade': grade,
            'subject': subject,
            'search': search,
            'grades': [(1, u'一年级'), (2, u'二年级'), (3, u'三年级'),
                       (7, u'初一'), (8, u'初二'), (9, u'初三'),
                       (88, u'高中')],
            'subjects': [('yw', '语文'), ('sx', '数学'), ('yy', '英语'), ('wl', '物理'),
                         ('hx', '化学'), ('sw', '生物'), ('ls', '历史'), ('dl', '地理')]
        })
