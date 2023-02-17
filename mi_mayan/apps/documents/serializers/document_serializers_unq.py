from django.utils.translation import ugettext_lazy as _

from mayan.apps.rest_api import serializers

from ..models.document_models_unq import (Constancia_Examen, Solicitud_Aviso_Ultimo_Examen, 
    Constancia_Aprobacion_Materia, Solicitud_Baja_Propuesta_Guarani, Solicitud_Certificado_Aprobacion,
    Solicitud_Equivalencias_Guarani
)


class Constancia_Examen_Serializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(lookup_url_kwarg='document_id',view_name="rest_api:document-detail")
    
    class Meta:
        extra_kwargs = {
            'url': {
                'lookup_url_kwarg': 'document_id',
                'view_name': 'rest_api:document-detail'
            },
        }
        model = Constancia_Examen
        fields = '__all__'

class Solicitud_Aviso_Ultimo_Examen_Serializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(lookup_url_kwarg='document_id',view_name="rest_api:document-detail")
    
    class Meta:
        extra_kwargs = {
            'url': {
                'lookup_url_kwarg': 'document_id',
                'view_name': 'rest_api:document-detail'
            },
        }
        model = Solicitud_Aviso_Ultimo_Examen
        fields = '__all__'

class Constancia_Aprobacion_Materia_Serializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(lookup_url_kwarg='document_id',view_name="rest_api:document-detail")
    
    class Meta:
        extra_kwargs = {
            'url': {
                'lookup_url_kwarg': 'document_id',
                'view_name': 'rest_api:document-detail'
            },
        }
        model = Constancia_Aprobacion_Materia
        fields = '__all__'

class Solicitud_Baja_Propuesta_Guarani_Serializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(lookup_url_kwarg='document_id',view_name="rest_api:document-detail")
    
    class Meta:
        extra_kwargs = {
            'url': {
                'lookup_url_kwarg': 'document_id',
                'view_name': 'rest_api:document-detail'
            },
        }
        model = Solicitud_Baja_Propuesta_Guarani
        fields = '__all__'

class Solicitud_Certificado_Aprobacion_Serializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(lookup_url_kwarg='document_id',view_name="rest_api:document-detail")
    
    class Meta:
        extra_kwargs = {
            'url': {
                'lookup_url_kwarg': 'document_id',
                'view_name': 'rest_api:document-detail'
            },
        }
        model = Solicitud_Certificado_Aprobacion
        fields = '__all__'

class Solicitud_Equivalencias_Guarani_Serializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(lookup_url_kwarg='document_id',view_name="rest_api:document-detail")
    
    class Meta:
        extra_kwargs = {
            'url': {
                'lookup_url_kwarg': 'document_id',
                'view_name': 'rest_api:document-detail'
            },
        }
        model = Solicitud_Equivalencias_Guarani
        fields = '__all__'