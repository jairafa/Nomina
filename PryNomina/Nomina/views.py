from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

from Nucleo.models import *
from Nomina.models import *

# Create your views here.

def main (request):
	cargo = NomCargo.objects.all().order_by("-codigo")
	paginator = Paginator (cargo,3)

	try: 
		pagina = int (request.GET.get("page","1"))
	except ValueError:pagina-1

	try:
		cargo = paginator.page(pagina)
	except (InvalidPage, EmptyPage):
		cargo = paginator.page(paginator.num_pages)

	return render_to_response("listados.html", dict(cargo = cargo, usuario = request.user))
