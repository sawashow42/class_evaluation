from django.shortcuts import render
from .models import SystemAppModel

# Create your views here.
def class_list(request):
	data = SystemAppModel.objects.all()
	return render(request, 'class_eval/eval_list.html', {'data' : data})