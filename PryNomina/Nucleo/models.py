from django.db import models

# Create your models here.

#Uso: Lista de Empresas
#Autor: Jairo Vega/Sonia Cruz
#Fecha de Creacion: 24/11/2013
#Modificaciones
##Fecha de Modificacion
##Descripcion
##Autor

class NucEmpresa(models.Model):
    empresa = models.CharField(max_length=250)

    def __str__(self):
        return self.empresa
#Uso: Meses
#Autor: Jairo Vega/Sonia Cruz
#Fecha de Creacion: 24/11/2013
#Modificaciones
##Fecha de Modificacion
##Descripcion
##Autor

class NucMes(models.Model):
    idEmpresa = models.ForeignKey(NucEmpresa)
    codMes = models.IntegerField()
    mes = models.CharField(max_length=20)

#Uso: Tipos de periodo
#Autor: Jairo Vega/Sonia Cruz
#Fecha de Creacion: 24/11/2013
#Modificaciones
##Fecha de Modificacion
##Descripcion
##Autor

class NucTipoPeriodo(models.Model):
    idEmpresa = models.ForeignKey(NucEmpresa)
    codTipoPeriodo = models.CharField(max_length=12)
    tipoPeriodo = models.CharField(max_length=50)



#Uso: Tipos de periodo
#Autor: Jairo Vega/Sonia Cruz
#Fecha de Creacion: 24/11/2013
#Modificaciones
##Fecha de Modificacion
##Descripcion
##Autor

class NucPeriodos(models.Model):
    idEmpresa = models.ForeignKey(NucEmpresa)
    idTipoPeriodo = models.ForeignKey(NucTipoPeriodo)
    idMes = models.ForeignKey(NucMes)
    anno = models.IntegerField()
    tipoPeriodo = models.CharField(max_length=50)
    fInicio = models.DateTimeField('Fecha Inicio')
    fFin = models.DateTimeField('Fecha Final')


#Uso: Tipos de identificacion de terceros
#Autor: Jairo Vega/Sonia Cruz
#Fecha de Creacion: 24/11/2013
#Modificaciones
##Fecha de Modificacion
##Descripcion
##Autor

class NucTipoIdentificacion(models.Model):
    idEmpresa = models.ForeignKey(NucEmpresa)
    codigo = models.CharField(max_length=1)
    Tipoidentificacion = models.CharField(max_length=100)

#Uso: Tipos de persona para terceros
#Autor: Jairo Vega/Sonia Cruz
#Fecha de Creacion: 24/11/2013
#Modificaciones
##Fecha de Modificacion
##Descripcion
##Autor

class NucTipoPersona(models.Model):
    idEmpresa = models.ForeignKey(NucEmpresa)
    PERSONAS = (
    ('N', 'Persona Natural'),
    ('J', 'Persona Juridica'),
    )
    codigo = models.CharField(max_length=1, choices=PERSONAS)
    TipoPersona = models.CharField(max_length=50)
    
#Uso: Detalle de los terceros
#Autor: Jairo Vega/Sonia Cruz
#Fecha de Creacion: 24/11/2013
#Modificaciones
##Fecha de Modificacion
##Descripcion
##Autor

class NucTerceros(models.Model):
    GENEROS = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('N', 'No Aplica'),
    )
    idEmpresa = models.ForeignKey(NucEmpresa)
    idTipoIdentificacion = models.ForeignKey(NucTipoIdentificacion)
    idTipoPersona = models.ForeignKey(NucTipoPersona)
    identificacion = models.CharField(max_length=20)
    digVerificacion = models.IntegerField()
    primerNombre = models.CharField(max_length=100)
    otrosNombres = models.CharField(max_length=100)
    primerApellido = models.CharField(max_length=100)
    otrosApellidos = models.CharField(max_length=100)
    genero = models.CharField(max_length=1, choices=GENEROS)
    fNacimiento = models.DateTimeField('Fecha de nacimiento')
    
    
