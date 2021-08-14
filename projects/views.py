from django.shortcuts import render
from projects.models import Project

# Create your views here.
def projects(request):
    projects = Project.objects.all().order_by('-pk')
    context = {'projects' : projects}
    return render(request, 'projects.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {'project' : project}
    return render(request, 'project_detail.html', context)

