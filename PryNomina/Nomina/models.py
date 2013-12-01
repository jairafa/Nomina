from django.db import models
from Nucleo.models import NucEmpresa
from Nucleo.models import NucTerceros
from Nucleo.models import NucPeriodos

# Create your models here.

#Uso: Tipos de identificacion de terceros
#Autor: Jairo Vega/Sonia Cruz
#Fecha de Creacion: 24/11/2013
#Modificaciones
##Fecha de Modificacion
##Descripcion
##Autor

class NomTipoContrato (models.Model):
    idEmpresa = models.ForeignKey (NucEmpresa)
    codigo = models.CharField(max_length=12)
    descripcion = models.CharField(max_length=150)

    def __str__(self):
        return self.descripcion
    
class NomEstadosTrabajador (models.Model):
    idEmpresa = models.ForeignKey (NucEmpresa)
    codigo = models.CharField(max_length=12)
    descripcion = models.CharField(max_length=150)
    
class NomCargo (models.Model):
    idEmpresa = models.ForeignKey (NucEmpresa)
    codigo = models.CharField(max_length=12)
    descripcion = models.CharField(max_length=150)

class NomTrabajador (models.Model):
    idEmpresa = models.ForeignKey (NucEmpresa)
    idTercero = models.ForeignKey (NucTerceros)
    correlativo = models.IntegerField()
    codigoTrabajador = models.CharField(max_length=150)
    idTipoContrato = models.ForeignKey (NomTipoContrato)
    fIngresoTrabajador = models.DateTimeField('Fecha Ingreso')
    fRetiroTrabajador = models.DateTimeField('Fecha Retiro')
    idEstadoTrabajador = models.ForeignKey (NomEstadosTrabajador)
    idCargo = models.ForeignKey (NomCargo)
    observaciones = models.CharField(max_length=250)
    sueldoBasico = models.DecimalField(max_digits = 14,  decimal_places = 2)
    FInicioSueldoBasico = models.DateTimeField('F. Inicio Sueldo Básico')
    diasFaltantes = models.IntegerField()
    diasSalario = models.IntegerField()
    salarioDebengado = models.DecimalField( max_digits = 14,  decimal_places = 2)
    TotalPago = models.DecimalField(max_digits = 14,  decimal_places = 2)
    TotalDescuentos = models.DecimalField(max_digits = 14,  decimal_places = 2)

class NomCondiciones (models.Model):
    idEmpresa = models.ForeignKey (NucEmpresa)
    condicion = models.CharField(max_length=150)

class NomCondicionesTrabajador (models.Model):
    idTrabajador = models.ForeignKey (NomTrabajador)
    idCondicion = models.ForeignKey (NomCondiciones)
    Activo = models.BooleanField(max_length=150)


