from django import forms
from ..models.document_models_unq import (
     Solicitud_Equivalencias_Guarani, Constancia_Examen, Solicitud_Aviso_Ultimo_Examen,
     Constancia_Aprobacion_Materia, Solicitud_Baja_Propuesta_Guarani, Solicitud_Certificado_Aprobacion
     )

##################################################################################
# Constancia Examen
##################################################################################
class Constancia_Examen_Form(forms.ModelForm):
    id_alumno = forms.CharField()
    email_alumno = forms.EmailField()
    document_type_id = forms.IntegerField(widget=forms.HiddenInput())
    file = forms.FileField()

    class Meta:
        fields = ('codigo_propuesta', 'descripcion_propuesta', 'nombres', 'apellido',
                   'tipo_documento', 'nro_documento', 'agente_presentacion', 'descripcion_actividad',
                   'fecha', 'proyecto')
        exclude = ['document_type_id']
        model = Constancia_Examen
        help_texts = {k:'' for k in fields}

    def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
           self.fields['document_type_id'].widget.attrs.update({'class': 'form-control'})

##################################################################################
# Solicitud Aviso Ultimo Examen
##################################################################################
class Solicitud_Aviso_Ultimo_Examen_Form(forms.ModelForm):
    id_alumno = forms.CharField()
    email_alumno = forms.EmailField()
    document_type_id = forms.IntegerField(widget=forms.HiddenInput())
    file = forms.FileField()

    class Meta:
        fields = ('codigo_propuesta', 'descripcion_propuesta', 'nombres', 'apellido', 
                  'tipo_documento', 'nro_documento', 'orientaciones', 'actividad', 'fecha_ultimo_examen',
                  'email_alternativo', 'tel_contacto')
        exclude = ['document_type_id']
        model = Solicitud_Aviso_Ultimo_Examen
        help_texts = {k:'' for k in fields}

    def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
           self.fields['document_type_id'].widget.attrs.update({'class': 'form-control'})

##################################################################################
# Constancia Aprobacion Materia
##################################################################################
class Constancia_Aprobacion_Materia_Form(forms.ModelForm):
    id_alumno = forms.CharField()
    email_alumno = forms.EmailField()
    document_type_id = forms.IntegerField(widget=forms.HiddenInput())
    file = forms.FileField()

    class Meta:
        fields = ('codigo_propuesta', 'descripcion_propuesta', 'nombres', 'apellido', 
                  'tipo_documento', 'nro_documento', 'agente_presentacion', 'descripcion_actividad')
        exclude = ['document_type_id']
        model = Constancia_Aprobacion_Materia
        help_texts = {k:'' for k in fields}

    def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
           self.fields['document_type_id'].widget.attrs.update({'class': 'form-control'})

##################################################################################
# Solicitud Baja Propuesta Guarani
##################################################################################
class Solicitud_Baja_Propuesta_Guarani_Form(forms.ModelForm):
    id_alumno = forms.CharField()
    email_alumno = forms.EmailField()
    document_type_id = forms.IntegerField(widget=forms.HiddenInput())
    file = forms.FileField()

    class Meta:
        fields = ('plan_personal', 'plan', 'codigo_propuesta', 'descripcion_propuesta', 'nombres', 
                  'apellido', 'motivos', 'otros_motivos', 'tipo_documento', 'nro_documento', 
                  'email_alternativo', 'tel_contacto', 'fecha_inscripcion')
        exclude = ['document_type_id']
        model = Solicitud_Baja_Propuesta_Guarani
        help_texts = {k:'' for k in fields}

    def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
           self.fields['document_type_id'].widget.attrs.update({'class': 'form-control'})

##################################################################################
# Solicitud Certificado Aprobacion
##################################################################################  
class Solicitud_Certificado_Aprobacion_Form(forms.ModelForm):
    id_alumno = forms.CharField()
    email_alumno = forms.EmailField()
    document_type_id = forms.IntegerField(widget=forms.HiddenInput())
    file = forms.FileField()

    class Meta:
        fields = ('codigo_propuesta', 'descripcion_propuesta', 'nombres', 'apellido', 
                  'tipo_documento', 'nro_documento', 'comision')
        exclude = ['document_type_id']
        model = Solicitud_Certificado_Aprobacion
        help_texts = {k:'' for k in fields}

    def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
           self.fields['document_type_id'].widget.attrs.update({'class': 'form-control'})

##################################################################################
# Solicitud Equivalencias
##################################################################################
class Solicitud_Equivalencias_Guarani_Form(forms.ModelForm):
    id_alumno = forms.CharField()
    email_alumno = forms.EmailField()
    document_type_id = forms.IntegerField(widget=forms.HiddenInput())
    file = forms.FileField()

    class Meta:
        fields = ('codigo_propuesta', 'descripcion_propuesta', 'nombres', 'apellido', 
                  'tipo_documento', 'nro_documento')
        exclude = ['document_type_id']
        model = Solicitud_Equivalencias_Guarani
        help_texts = {k:'' for k in fields}

    def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
           self.fields['document_type_id'].widget.attrs.update({'class': 'form-control'})