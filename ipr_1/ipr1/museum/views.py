from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models.functions import Lower
from django.shortcuts import render, get_object_or_404, get_list_or_404

from museum.models import Exposition, Exhibit, Excursion, Author, Hall, FormOfArt


# Create your views here.

def base(request):
    return render(request, "museum/base.html")


def contacts(request):
    return render(request, "museum/contacts.html")


def exhibits(request):
    exhibits_list = Exhibit.objects.all()
    paginator = Paginator(exhibits_list, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "museum/exhibits/exhibits.html", {
        'page_obj': page_obj
    })


def exhibit_profile(request, exhibit_id):
    exhibit = get_object_or_404(Exhibit, id=exhibit_id)
    if exhibit.autor is not None:
        author = get_object_or_404(Author, id=exhibit.autor.id)
    else:
        author = Author()

    exposition = get_object_or_404(Exposition, id=exhibit.exposition.id)
    hall = get_object_or_404(Hall, id=exposition.hall.id)
    return render(request, "museum/exhibits/exhibit_profile.html", {
        'exhibit': exhibit,
        'author': author,
        'exposition': exposition,
        'hall': hall
    })


def schedule(request):
    return render(request, "museum/schedule.html")


def expositions(request):
    expositions_list = Exposition.objects.all()

    paginator = Paginator(expositions_list, 9)  # Пагинация: 10 экспонатов на страницу

    page_number = request.GET.get('page')  # Получаем номер страницы из параметров запроса
    page_obj = paginator.get_page(page_number)  # Получаем объекты текущей страницы
    return render(request, "museum/expositions/expositions.html", {
        'page_obj': page_obj,
    })


def exposition_profile(request, exposition_id):
    exposition = get_object_or_404(Exposition, id=exposition_id)

    exhibits_list = Exhibit.objects.filter(exposition__id=exposition_id)
    excursion_list = Excursion.objects.filter(exposition__id=exposition_id)

    return render(request, "museum/expositions/exposition_profile.html", {
        'exposition': exposition,
        'exhibits': exhibits_list,
        'excursions': excursion_list
    })

def authors(request):
    authors_list = Author.objects.all()

    paginator = Paginator(authors_list, 9)  # Пагинация: 10 экспонатов на страницу

    page_number = request.GET.get('page')  # Получаем номер страницы из параметров запроса
    page_obj = paginator.get_page(page_number)  # Получаем объекты текущей страницы

    return render(request, "museum/authors/authors.html", {
        'page_obj': page_obj
    })

def author_profile(request, author_id):
    author = get_object_or_404(Author, id=author_id)

    return render(request, "museum/authors/author_profile.html", {
        'author':author,
    })


def form_profile(request, form_id):
    form = get_object_or_404(FormOfArt, id=form_id)
    return render(request, "museum/forms/form_profile.html",{
        'form':form,

    })


def search(request):
    query = request.GET.get('q')  # Получаем значение из GET-запроса
    if query:
        exposition_results = Exposition.objects.filter(Q(name__icontains=query) | Q(name__icontains=query.capitalize()))
        exhibit_results = Exhibit.objects.filter(Q(name__icontains=query) | Q(name__icontains=query.capitalize()))
        author_results = Author.objects.filter(Q(first_name__icontains=query) | Q(first_name__icontains=query.capitalize()))
    else:
        exposition_results = Exposition.objects.none()
        exhibit_results = Exhibit.objects.none()
        author_results = Author.objects.none()

    return render(request, "search_results.html", {
        'exposition_results': exposition_results,
        'exhibit_results': exhibit_results,
        'author_results': author_results,
        'query': query
    })