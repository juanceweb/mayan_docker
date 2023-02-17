from ..models.document_models_unq import (
    Constancia_Examen, Solicitud_Aviso_Ultimo_Examen, Constancia_Aprobacion_Materia,
    Solicitud_Baja_Propuesta_Guarani, Solicitud_Certificado_Aprobacion, Solicitud_Equivalencias_Guarani
)
from ..serializers.document_serializers import (
    Constancia_Examen_Serializer, Solicitud_Aviso_Ultimo_Examen_Serializer, 
    Constancia_Aprobacion_Materia_Serializer, Solicitud_Baja_Propuesta_Guarani_Serializer,
    Solicitud_Certificado_Aprobacion_Serializer, Solicitud_Equivalencias_Guarani_Serializer
)

def cargar_modelo_extra(document_type_id, serializer):

    models_array = ['constancia_examen', 
                    'solicitud_aviso_ultimo_examen',
                    'constancia_aprobacion_materia',
                    'solicitud_baja_propuesta_guarani',
                    'solicitud_certificado_aprobacion',
                    'solicitud_equivalencias_guarani'
                    ]

    if 1 == document_type_id:
        form = Constancia_Examen_Serializer
        value = 'constancia_examen'

    elif 2 == document_type_id:
        form = Solicitud_Aviso_Ultimo_Examen_Serializer
        value = 'solicitud_aviso_ultimo_examen'

    elif 3 == document_type_id:
        form = Constancia_Aprobacion_Materia_Serializer
        value = 'constancia_aprobacion_materia'        

    elif 4 == document_type_id:
        form = Solicitud_Baja_Propuesta_Guarani_Serializer
        value = 'solicitud_baja_propuesta_guarani'

    elif 5 == document_type_id:
        form = Solicitud_Certificado_Aprobacion_Serializer
        value = 'solicitud_certificado_aprobacion'

    elif 6 == document_type_id:
        form = Solicitud_Equivalencias_Guarani_Serializer
        value = 'solicitud_equivalencias_guarani'

    form = form(data=serializer.validated_data['_instance_extra_data']['extras'])
    form.is_valid(raise_exception=True)
    objeto = form.save()

    for model in models_array:
        if model == value:
            serializer.validated_data[model] = objeto
        else:
            serializer.validated_data[model] = None


def update_modelo_extra(document, new_data):
    if 1 == document.document_type.id:
        objeto = Constancia_Examen.objects.get(id = document.constancia_examen.id)
        form = Constancia_Examen_Serializer     

    elif 2 == document.document_type.id:
        objeto = Solicitud_Aviso_Ultimo_Examen.objects.get(id = document.solicitud_aviso_ultimo_examen.id)
        form = Solicitud_Aviso_Ultimo_Examen_Serializer 

    elif 3 == document.document_type.id:
        objeto = Constancia_Aprobacion_Materia.objects.get(id = document.constancia_aprobacion_materia.id)
        form = Constancia_Aprobacion_Materia_Serializer
    
    elif 4 == document.document_type.id:
        objeto = Solicitud_Baja_Propuesta_Guarani.objects.get(id = document.solicitud_baja_propuesta_guarani.id)
        form = Solicitud_Baja_Propuesta_Guarani_Serializer

    elif 5 == document.document_type.id:
        objeto = Solicitud_Certificado_Aprobacion.objects.get(id = document.solicitud_certificado_aprobacion.id)
        form = Solicitud_Certificado_Aprobacion_Serializer
    
    elif 6 == document.document_type.id:
        objeto = Solicitud_Equivalencias_Guarani.objects.get(id = document.solicitud_equivalencias_guarani.id)
        form = Solicitud_Equivalencias_Guarani_Serializer
    
    form = form(objeto, data=new_data, partial=True)
    form.is_valid(raise_exception=True)
    form.save()