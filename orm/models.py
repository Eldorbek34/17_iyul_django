from django.db import models
from django import forms
from .forms import StudentSearchForm
from django.shortcuts import render
def search_students(request):
    form = StudentSearchForm()
    students = None
    if 'query' in request.GET:
        form = StudentSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            students = Student.objects.filter(first_name__icontains=query)
    return render(request, 'search.html', {'form': form, 'students': students})


class StudentSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)


class Region(models.Model):
    name = models.CharField("Viloyat", max_length=67)

    def __str__(self):
        return self.name



class Student(models.Model):
    first_name = models.CharField("Ism", max_length=155)
    last_name = models.CharField("Familiya", max_length=155, null=True, blank=True)
    passport = models.CharField("Pasport", max_length=9, null=True, blank=True)
    phone = models.CharField("Telefon raqami", max_length=14)
    age = models.PositiveIntegerField(default=0)
    is_paid_for_year = models.BooleanField(default=0)

    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)

    joined_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"{self.first_name} - {self.phone}"