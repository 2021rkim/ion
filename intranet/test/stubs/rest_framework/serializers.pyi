class Serializer:
  # FIXME: actually figure out args
  def __init__(self, *args, **kwargs): ...
class ModelSerializer(Serializer): ...
class HyperlinkedModelSerializer(Serializer): ...
class Field:
  # FIXME: actually figure out args
  def __init__(self, *args, **kwargs): ...
  def get_url(self, *args, **kwargs): ...  # FIXME: figure out args
class StringRelatedField(Field): ...
class CharField(Field): ...
class ListField(Field): ...
class IntegerField(Field): ...
class EmailField(Field): ...
class DateTimeField(Field): ...
class BooleanField(Field): ...
class DateField(Field): ...
class ReadOnlyField(Field): ...
class HyperlinkedIdentityField(Field): ...
class PrimaryKeyRelatedField(Field): ...
class SerializerMethodField(Field): ...
