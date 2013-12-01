from Nomina.models import NomTipoContrato
from Nomina.models import NomEstadosTrabajador
from Nomina.models import NomCargo
from Nomina.models import NomCondiciones
from django.contrib import admin


# Register your models here.
admin.site.register(NomTipoContrato)
admin.site.register(NomEstadosTrabajador)
admin.site.register(NomCargo)
admin.site.register(NomCondiciones)



