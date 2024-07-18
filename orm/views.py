from django.shortcuts import render
from .models import Student
from .forms import StudentSearchForm

def search_students(request):
    form = StudentSearchForm()
    students = None
    if 'query' in request.GET:
        form = StudentSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            students = Student.objects.filter(first_name__icontains=query)
    return render(request, 'search.html', {'form': form, 'students': students})
