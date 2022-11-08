from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from App.models import SRList
from .forms import SRCreateForm
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def index(request):

    qs = SRList.objects.all().order_by('-create_date')

    page = request.GET.get('page', '1')
    paginator = Paginator(qs, 10)
    page_obj = paginator.get_page(page)

    return render(request, 'SRList.html', {'qs': page_obj})

## SR 등록하기
def SRCreate(request):

    if request.method == 'POST':
        form = SRCreateForm(request.POST)
        if form.is_valid():
            SRList = form.save(commit=False)
            SRList.create_date = timezone.now()
            SRList.save()
            return redirect('App:index')
    else:
        form = SRCreateForm()

    return render(request, 'SRCreate.html', {'form': form})

## SR 삭제하기
def SRDelete(request, qs_id):

    qs = get_object_or_404(SRList, pk=qs_id)

    qs.delete()

    return redirect('App:index')

## SR 수정하기
def SRUpdate(request, qs_id):

    qs = get_object_or_404(SRList, pk=qs_id)

    if request.method == 'POST':
        form = SRCreateForm(request.POST, instance=qs)
        if form.is_valid():
            qs = form.save(commit=False)
            qs.update_date = timezone.now()
            qs.save()
            return redirect('App:index')

    else:
        form = SRCreateForm(instance=qs)
        return render(request, 'SRCreate.html', {'form': form})