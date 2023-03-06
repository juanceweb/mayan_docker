from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import ArrayField, HStoreField

# 1 crear el modelo
# 2 asignarselo como parametro al Documento
# 3 crear el serializer del modelo nuevo
# 4 agregar el campo en el serializer del Documento
# 5 agregar en el serializer en el Meta
# 6 agregar en el agregar y modificar de api_functions
# 7 crear el nuevo document type


##################################################################################
# Constancia Examen
##################################################################################

class Constancia_Examen(models.Model):

    codigo_propuesta = models.CharField(
        max_length=255,
        help_text=_(
            'codigo de la propuesta.'
        ),
        verbose_name=_('codigo propuesta'))
    
    descripcion_propuesta = models.CharField(
        max_length=255,
        help_text=_(
            'descripcion de la propuesta.'
        ),
        verbose_name=_('descripcion propuesta'))
    
    nombres = models.CharField(
        max_length=255,
        help_text=_(
            'nombres del estudiante.'
        ),
        verbose_name=_('nombres'))
    
    apellido = models.CharField(
        max_length=255,
        help_text=_(
            'apellido del estudiante.'
        ),
        verbose_name=_('apellido'))
    
    tipo_documento = models.CharField(
        max_length=255,
        help_text=_(
            'tipo de documento'
        ),
        verbose_name=_('tipo documento'))
    
    nro_documento = models.CharField(
        max_length=255,
        help_text=_(
            'numero de documento.'
        ),
        verbose_name=_('numero documento'))
    
    # tutores = ArrayField(HStoreField(),
    #    db_index=True, max_length=255,
    #    help_text=_(
    #        'lista de tutores.'
    #    ),
    #    verbose_name=_('lista de tutores'))
    
    # domicilio = ArrayField(models.CharField(max_length=255),
    #    db_index=True, max_length=255,
    #    help_text=_(
    #        'lista de domicilios.'
    #    ),
    #    verbose_name=_('lista de domicilios'))

    agente_presentacion = models.CharField(
        max_length=255,
        help_text=_(
            'agente de presentacion.'
        ),
        verbose_name=_('agente presentacion'))
    
    descripcion_actividad = models.CharField(
        max_length=255,
        help_text=_(
            'descripcion de la actividad.'
        ),
        verbose_name=_('descripcion actividad'))
    
    fecha = models.DateField(
        help_text=_(
            'fecha.'
        ),
        verbose_name=_('fecha'))
    
    proyecto = models.CharField(
        max_length=255,
        help_text=_(
            'proyecto.'
        ),
        verbose_name=_('proyecto'))

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Constancia Examen'
        verbose_name_plural = 'Constancia Examen'


##################################################################################
# Solicitud Aviso Ultimo Examen
##################################################################################  
class Solicitud_Aviso_Ultimo_Examen(models.Model):
    
    codigo_propuesta = models.CharField(
        max_length=255,
        help_text=_(
            'codigo de la propuesta.'
        ),
        verbose_name=_('codigo propuesta'))
    
    descripcion_propuesta = models.CharField(
        max_length=255,
        help_text=_(
            'descripcion de la propuesta.'
        ),
        verbose_name=_('descripcion propuesta'))
    
    nombres = models.CharField(
        max_length=255,
        help_text=_(
            'nombres del estudiante.'
        ),
        verbose_name=_('nombres'))
    
    apellido = models.CharField(
        max_length=255,
        help_text=_(
            'apellido del estudiante.'
        ),
        verbose_name=_('apellido'))
    
    tipo_documento = models.CharField(
        max_length=255,
        help_text=_(
            'tipo de documento'
        ),
        verbose_name=_('tipo documento'))
    
    nro_documento = models.CharField(
        max_length=255,
        help_text=_(
            'numero de documento.'
        ),
        verbose_name=_('numero documento'))
    
    # tutores = ArrayField(HStoreField(),
    #    db_index=True, max_length=255,
    #    help_text=_(
    #        'lista de tutores.'
    #    ),
    #    verbose_name=_('lista de tutores'))
    
    orientaciones = ArrayField(models.CharField(max_length=255),
       max_length=255,
       help_text=_(
           'lista de orientaciones.'
       ),
       verbose_name=_('lista de orientaciones'))
    
    actividad = models.CharField(
        max_length=255,
        help_text=_(
            'aactividad.'
        ),
        verbose_name=_('actividad'))
    
    fecha_ultimo_examen = models.DateField(
        help_text=_(
            'fecha ultimo examen.'
        ),
        verbose_name=_('fecha ultimo examen'))
    
    email_alternativo = models.EmailField(
        max_length=255,
        help_text=_(
            'email_alternativo.'
        ),
        verbose_name=_('email_alternativo'))

    tel_contacto = models.IntegerField(
        help_text=_(
            'telefono contacto.'
        ),
        verbose_name=_('telefono contacto'))

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Solicitud Aviso Ultimo Examen'
        verbose_name_plural = 'Solicitud Aviso Ultimo Examen'

    
##################################################################################
# Constancia Aprobacion Materia
##################################################################################
class Constancia_Aprobacion_Materia(models.Model):
    
    codigo_propuesta = models.CharField(
        max_length=255,
        help_text=_(
            'codigo de la propuesta.'
        ),
        verbose_name=_('codigo propuesta'))
    
    descripcion_propuesta = models.CharField(
        max_length=255,
        help_text=_(
            'descripcion de la propuesta.'
        ),
        verbose_name=_('descripcion propuesta'))
    
    nombres = models.CharField(
        max_length=255,
        help_text=_(
            'nombres del estudiante.'
        ),
        verbose_name=_('nombres'))
    
    apellido = models.CharField(
        max_length=255,
        help_text=_(
            'apellido del estudiante.'
        ),
        verbose_name=_('apellido'))
    
    tipo_documento = models.CharField(
        max_length=255,
        help_text=_(
            'tipo de documento'
        ),
        verbose_name=_('tipo documento'))
    
    nro_documento = models.CharField(
        max_length=255,
        help_text=_(
            'numero de documento.'
        ),
        verbose_name=_('numero documento'))
    
    # tutores = ArrayField(HStoreField(),
    #    db_index=True, max_length=255,
    #    help_text=_(
    #        'lista de tutores.'
    #    ),
    #    verbose_name=_('lista de tutores'))
    
    # domicilio = ArrayField(models.CharField(max_length=255),
    #    db_index=True, max_length=255,
    #    help_text=_(
    #        'lista de domicilios.'
    #    ),
    #    verbose_name=_('lista de domicilios'))

    agente_presentacion = models.CharField(
        max_length=255,
        help_text=_(
            'agente de presentacion.'
        ),
        verbose_name=_('agente presentacion'))
    
    descripcion_actividad = models.CharField(
        max_length=255,
        help_text=_(
            'descripcion de la actividad.'
        ),
        verbose_name=_('descripcion actividad'))

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Constancia Aprobacion Materia'
        verbose_name_plural = 'Constancia Aprobacion Materia'


##################################################################################
# Solicitud Baja Propuesta Guarani
##################################################################################  
class Solicitud_Baja_Propuesta_Guarani(models.Model):

    plan_personal = models.CharField(
        max_length=255,
        help_text=_(
            'plan personal.'
        ),
        verbose_name=_('plan personal'))
    
    plan = models.CharField(
        max_length=255,
        help_text=_(
            'plan.'
        ),
        verbose_name=_('plan'))
    
    codigo_propuesta = models.CharField(
        max_length=255,
        help_text=_(
            'codigo de la propuesta.'
        ),
        verbose_name=_('codigo propuesta'))
    
    descripcion_propuesta = models.CharField(
        max_length=255,
        help_text=_(
            'descripcion de la propuesta.'
        ),
        verbose_name=_('descripcion propuesta'))

    motivos = ArrayField(models.IntegerField(),
       help_text=_(
           'motivos.'
       ),
       verbose_name=_('lista de motivos'))

    otros_motivos = models.CharField(
        max_length=255,
        help_text=_(
            'otros motivos.'
        ),
        verbose_name=_('otros motivos'))  

    nombres = models.CharField(
        max_length=255,
        help_text=_(
            'nombres del estudiante.'
        ),
        verbose_name=_('nombres'))
    
    apellido = models.CharField(
        max_length=255,
        help_text=_(
            'apellido del estudiante.'
        ),
        verbose_name=_('apellido'))
    
    tipo_documento = models.CharField(
        max_length=255,
        help_text=_(
            'tipo de documento'
        ),
        verbose_name=_('tipo documento'))
    
    nro_documento = models.CharField(
        max_length=255,
        help_text=_(
            'numero de documento.'
        ),
        verbose_name=_('numero documento'))
    
    # tutores = ArrayField(HStoreField(),
    #    db_index=True, max_length=255,
    #    help_text=_(
    #        'lista de tutores.'
    #    ),
    #    verbose_name=_('lista de tutores'))
    
    email_alternativo = models.EmailField(
        max_length=255,
        help_text=_(
            'email_alternativo.'
        ),
        verbose_name=_('email_alternativo'))

    tel_contacto = models.IntegerField(
        help_text=_(
            'telefono contacto.'
        ),
        verbose_name=_('telefono contacto'))
    
    fecha_inscripcion = models.DateField(
        help_text=_(
            'fecha inscripcion.'
        ),
        verbose_name=_('fecha inscripcion'))

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Solicitud Baja Propuesta Guarani'
        verbose_name_plural = 'Solicitud Baja Propuesta Guarani'
    

##################################################################################
# Solicitud Certificado Aprobacion
##################################################################################  
class Solicitud_Certificado_Aprobacion(models.Model):
    
    codigo_propuesta = models.CharField(
        max_length=255,
        help_text=_(
            'codigo de la propuesta.'
        ),
        verbose_name=_('codigo propuesta'))
    
    descripcion_propuesta = models.CharField(
        max_length=255,
        help_text=_(
            'descripcion de la propuesta.'
        ),
        verbose_name=_('descripcion propuesta'))

    nombres = models.CharField(
        max_length=255,
        help_text=_(
            'nombres del estudiante.'
        ),
        verbose_name=_('nombres'))
    
    apellido = models.CharField(
        max_length=255,
        help_text=_(
            'apellido del estudiante.'
        ),
        verbose_name=_('apellido'))
    
    tipo_documento = models.CharField(
        max_length=255,
        help_text=_(
            'tipo de documento'
        ),
        verbose_name=_('tipo documento'))
    
    nro_documento = models.CharField(
        max_length=255,
        help_text=_(
            'numero de documento.'
        ),
        verbose_name=_('numero documento'))
    
    comision = models.CharField(
        max_length=255,
        help_text=_(
            'comision.'
        ),
        verbose_name=_('comision'))

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Solicitud Certificado Aprobacion'
        verbose_name_plural = 'Solicitud Certificado Aprobacion'
    

##################################################################################
# Solicitud Equivalencias Guarani
##################################################################################  
class Solicitud_Equivalencias_Guarani(models.Model):
    
    codigo_propuesta = models.CharField(
        max_length=255,
        help_text=_(
            'codigo de la propuesta.'
        ),
        verbose_name=_('codigo propuesta'))
    
    descripcion_propuesta = models.CharField(
        max_length=255,
        help_text=_(
            'descripcion de la propuesta.'
        ),
        verbose_name=_('descripcion propuesta'))

    nombres = models.CharField(
        max_length=255,
        help_text=_(
            'nombres del estudiante.'
        ),
        verbose_name=_('nombres'))
    
    apellido = models.CharField(
        max_length=255,
        help_text=_(
            'apellido del estudiante.'
        ),
        verbose_name=_('apellido'))
    
    tipo_documento = models.CharField(
        max_length=255,
        help_text=_(
            'tipo de documento'
        ),
        verbose_name=_('tipo documento'))
    
    nro_documento = models.CharField(
        max_length=255,
        help_text=_(
            'numero de documento.'
        ),
        verbose_name=_('numero documento'))
    
    # tutores = ArrayField(HStoreField(),
    #    db_index=True, max_length=255,
    #    help_text=_(
    #        'lista de tutores.'
    #    ),
    #    verbose_name=_('lista de tutores'))


    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Solicitud Equivalencias Guarani'
        verbose_name_plural = 'Solicitud Equivalencias Guarani'
    