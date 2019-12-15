from django.db.models.base import ModelBase


class Utils:

    def get_model_info(self, model):
        props = {}
        if type(model) == ModelBase:
            for field in model._meta.fields + model._meta.many_to_many:
                filed_name = field.name
                if filed_name not in ['created', 'modified']:
                    field_type = field.get_internal_type()
                    if field_type == 'ManyToManyField':
                        value = [self.get_model_info(field.related_model)]
                    else:
                        value = f'Type: {field_type}, Mandatory: {not (field.blank or field.null)}'
                    if filed_name == 'stock':
                        filed_name = 'quantity'
                    props[filed_name] = value
        return props
