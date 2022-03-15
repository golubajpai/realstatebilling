from django.shortcuts import render
from django.views.generic import TemplateView
from .permission import IsMapperMixin,IsAutnticated
from django.views.generic.base import View
# Create your views here.


def get_id(request):
	return render(request,'new_index.html')


class Home(IsMapperMixin,View):
	template_name="map_creation.html"

	def get(self,request):

		return render(request,self.template_name,{'image':request.user.image.all()[0].image.url})


	def Post(self,request):
		pass



def add_data(request):
	import pdb;pdb.set_trace()
	if request.is_authenticated:
		pass




