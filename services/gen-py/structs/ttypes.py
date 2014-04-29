#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:utf8strings,dynamic
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.protocol.TBase import TBase, TExceptionBase



class Interval(TBase):
  """
  Attributes:
   - upper
   - lower
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'upper', None, None, ), # 1
    (2, TType.I32, 'lower', None, None, ), # 2
  )

  def __init__(self, upper=None, lower=None,):
    self.upper = upper
    self.lower = lower

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TextNode(TBase):
  """
  Attributes:
   - pageIndex
   - interval
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'pageIndex', None, None, ), # 1
    (2, TType.STRUCT, 'interval', (Interval, Interval.thrift_spec), None, ), # 2
  )

  def __init__(self, pageIndex=None, interval=None,):
    self.pageIndex = pageIndex
    self.interval = interval

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class MetaReference(TBase):
  """
  Attributes:
   - field
   - idx
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'field', None, None, ), # 1
    (2, TType.I32, 'idx', None, None, ), # 2
  )

  def __init__(self, field=None, idx=None,):
    self.field = field
    self.idx = idx

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Annotation(TBase):
  """
  Attributes:
   - uuid
   - label
   - meta
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'uuid', None, None, ), # 1
    (2, TType.I32, 'label', None, None, ), # 2
    (3, TType.STRUCT, 'meta', (MetaReference, MetaReference.thrift_spec), None, ), # 3
  )

  def __init__(self, uuid=None, label=None, meta=None,):
    self.uuid = uuid
    self.label = label
    self.meta = meta

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Marginalis(TBase):
  """
  Attributes:
   - id
   - title
   - description
   - annotations
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'id', None, None, ), # 1
    (2, TType.STRING, 'title', None, None, ), # 2
    (3, TType.STRING, 'description', None, None, ), # 3
    (4, TType.LIST, 'annotations', (TType.STRUCT,(Annotation, Annotation.thrift_spec)), None, ), # 4
  )

  def __init__(self, id=None, title=None, description=None, annotations=None,):
    self.id = id
    self.title = title
    self.description = description
    self.annotations = annotations

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Mapping(TBase):
  """
  Attributes:
   - textNodes
   - ranges
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'textNodes', (TType.I32,None), None, ), # 1
    (2, TType.LIST, 'ranges', (TType.STRUCT,(Interval, Interval.thrift_spec)), None, ), # 2
  )

  def __init__(self, textNodes=None, ranges=None,):
    self.textNodes = textNodes
    self.ranges = ranges

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Document(TBase):
  """
  Attributes:
   - text
   - textNodes
   - marginalia
   - meta
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'text', None, None, ), # 1
    (2, TType.LIST, 'textNodes', (TType.STRUCT,(TextNode, TextNode.thrift_spec)), None, ), # 2
    (3, TType.LIST, 'marginalia', (TType.STRUCT,(Marginalis, Marginalis.thrift_spec)), None, ), # 3
    (4, TType.MAP, 'meta', (TType.STRING,None,TType.STRUCT,(Mapping, Mapping.thrift_spec)), None, ), # 4
  )

  def __init__(self, text=None, textNodes=None, marginalia=None, meta=None,):
    self.text = text
    self.textNodes = textNodes
    self.marginalia = marginalia
    self.meta = meta

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
