from byrd_backend.libs.exceptions import InvalidSerializer
from byrd_backend.libs.operations.utils import Utils


class OperationManager:

    def __init__(self, **kwargs):
        self.instance = kwargs.get('instance', None)
        self.model = kwargs.get('model', None)
        self.serializer = kwargs.get('serializer', None)
        self.serializer_get = kwargs.get('serializer_get', None)

    def get(self, pk):
        if not self.instance or self.instance.pk != pk:
            self.instance = self.model.objects.get(pk=pk)
        return self.instance

    def get_empty_query_set(self):
        return self.model.objects.none()

    def get_by_kwargs(self, **kwargs):
        try:
            return self.model.objects.get(**kwargs)
        except self.model.DoesNotExist:
            return None

    def filter_by_kwargs(self, **kwargs):
        return self.model.objects.filter(**kwargs)

    def _raise_in_valid_serializer(self, serializer):
        raise InvalidSerializer(f"Unable to validate Serializer: {self.serializer.__name__}", serializer.errors)

    def is_valid(self, data, many=False, throw=True):
        serializer = self.serializer(data=data, many=many)
        _is_valid = serializer.is_valid()
        if not _is_valid and throw:
            self._raise_in_valid_serializer(serializer)
        return True

    def create_or_update(self, data):
        try:
            serializer = self.serializer(data=data)
            if serializer.is_valid():
                _id = data.get('id', None)
                if _id:
                    _instance = self.get(_id)
                    return serializer.update(_instance, serializer.validated_data)
                return serializer.save()
            self._raise_in_valid_serializer(serializer)
        except Exception as ex:
            raise ex

    def _get_serializer(self):
        return self.serializer_get if self.serializer_get else self.serializer

    def get_list(self, query_set=None):
        if query_set is None:
            query_set = self.all()
        return self._get_serializer()(query_set, many=True).data

    def detail(self, pk):
        return self._get_serializer()(self.get(pk), many=False).data

    def detail_by_instance(self, instance):
        return self._get_serializer()(instance, many=False).data

    def all(self):
        return self.model.objects.all()

    def delete(self, pk):
        if pk:
            pk = int(pk)
        return self.get(pk).delete()

    def delete_all(self):
        return self.all().delete()

    def get_instance(self, instance_or_id):
        return self.get(instance_or_id) if type(instance_or_id) == int else instance_or_id

    def get_model_info(self):
        return Utils().get_model_info(self.model)
