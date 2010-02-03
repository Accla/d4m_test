#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

from thrift.Thrift import *
import data.ttypes
import master.ttypes
import tabletserver.ttypes
import security.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class NoSuchTableException(Exception):

  thrift_spec = (
  )

  def __init__(self, d=None):
    pass

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('NoSuchTableException')
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __str__(self): 
    return str(self.__dict__)

  def __repr__(self): 
    return repr(self.__dict__)

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Column:

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'columnFamily', None, None, ), # 1
    (2, TType.STRING, 'columnQualifier', None, None, ), # 2
    (3, TType.LIST, 'columnVisibility', (TType.LIST,(TType.I16,None)), None, ), # 3
  )

  def __init__(self, d=None):
    self.columnFamily = None
    self.columnQualifier = None
    self.columnVisibility = None
    if isinstance(d, dict):
      if 'columnFamily' in d:
        self.columnFamily = d['columnFamily']
      if 'columnQualifier' in d:
        self.columnQualifier = d['columnQualifier']
      if 'columnVisibility' in d:
        self.columnVisibility = d['columnVisibility']

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.columnFamily = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.columnQualifier = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.columnVisibility = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = []
            (_etype9, _size6) = iprot.readListBegin()
            for _i10 in xrange(_size6):
              _elem11 = iprot.readI16();
              _elem5.append(_elem11)
            iprot.readListEnd()
            self.columnVisibility.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Column')
    if self.columnFamily != None:
      oprot.writeFieldBegin('columnFamily', TType.STRING, 1)
      oprot.writeString(self.columnFamily)
      oprot.writeFieldEnd()
    if self.columnQualifier != None:
      oprot.writeFieldBegin('columnQualifier', TType.STRING, 2)
      oprot.writeString(self.columnQualifier)
      oprot.writeFieldEnd()
    if self.columnVisibility != None:
      oprot.writeFieldBegin('columnVisibility', TType.LIST, 3)
      oprot.writeListBegin(TType.LIST, len(self.columnVisibility))
      for iter12 in self.columnVisibility:
        oprot.writeListBegin(TType.I16, len(iter12))
        for iter13 in iter12:
          oprot.writeI16(iter13)
        oprot.writeListEnd()
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __str__(self): 
    return str(self.__dict__)

  def __repr__(self): 
    return repr(self.__dict__)

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ColumnUpdate:

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'column', (Column, Column.thrift_spec), None, ), # 1
    (2, TType.I64, 'timestamp', None, None, ), # 2
    (3, TType.STRING, 'value', None, None, ), # 3
    (4, TType.BOOL, 'deleted', None, None, ), # 4
  )

  def __init__(self, d=None):
    self.column = None
    self.timestamp = None
    self.value = None
    self.deleted = None
    if isinstance(d, dict):
      if 'column' in d:
        self.column = d['column']
      if 'timestamp' in d:
        self.timestamp = d['timestamp']
      if 'value' in d:
        self.value = d['value']
      if 'deleted' in d:
        self.deleted = d['deleted']

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.column = Column()
          self.column.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.timestamp = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.value = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.BOOL:
          self.deleted = iprot.readBool();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ColumnUpdate')
    if self.column != None:
      oprot.writeFieldBegin('column', TType.STRUCT, 1)
      self.column.write(oprot)
      oprot.writeFieldEnd()
    if self.timestamp != None:
      oprot.writeFieldBegin('timestamp', TType.I64, 2)
      oprot.writeI64(self.timestamp)
      oprot.writeFieldEnd()
    if self.value != None:
      oprot.writeFieldBegin('value', TType.STRING, 3)
      oprot.writeString(self.value)
      oprot.writeFieldEnd()
    if self.deleted != None:
      oprot.writeFieldBegin('deleted', TType.BOOL, 4)
      oprot.writeBool(self.deleted)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __str__(self): 
    return str(self.__dict__)

  def __repr__(self): 
    return repr(self.__dict__)

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Mutation:

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'row', None, None, ), # 1
    (2, TType.LIST, 'updates', (TType.STRUCT,(ColumnUpdate, ColumnUpdate.thrift_spec)), None, ), # 2
  )

  def __init__(self, d=None):
    self.row = None
    self.updates = None
    if isinstance(d, dict):
      if 'row' in d:
        self.row = d['row']
      if 'updates' in d:
        self.updates = d['updates']

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.row = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.updates = []
          (_etype17, _size14) = iprot.readListBegin()
          for _i18 in xrange(_size14):
            _elem19 = ColumnUpdate()
            _elem19.read(iprot)
            self.updates.append(_elem19)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Mutation')
    if self.row != None:
      oprot.writeFieldBegin('row', TType.STRING, 1)
      oprot.writeString(self.row)
      oprot.writeFieldEnd()
    if self.updates != None:
      oprot.writeFieldBegin('updates', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.updates))
      for iter20 in self.updates:
        iter20.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __str__(self): 
    return str(self.__dict__)

  def __repr__(self): 
    return repr(self.__dict__)

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Key:

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'row', None, None, ), # 1
    (2, TType.STRUCT, 'column', (Column, Column.thrift_spec), None, ), # 2
    (3, TType.I64, 'timestamp', None, None, ), # 3
  )

  def __init__(self, d=None):
    self.row = None
    self.column = None
    self.timestamp = None
    if isinstance(d, dict):
      if 'row' in d:
        self.row = d['row']
      if 'column' in d:
        self.column = d['column']
      if 'timestamp' in d:
        self.timestamp = d['timestamp']

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.row = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.column = Column()
          self.column.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.timestamp = iprot.readI64();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Key')
    if self.row != None:
      oprot.writeFieldBegin('row', TType.STRING, 1)
      oprot.writeString(self.row)
      oprot.writeFieldEnd()
    if self.column != None:
      oprot.writeFieldBegin('column', TType.STRUCT, 2)
      self.column.write(oprot)
      oprot.writeFieldEnd()
    if self.timestamp != None:
      oprot.writeFieldBegin('timestamp', TType.I64, 3)
      oprot.writeI64(self.timestamp)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __str__(self): 
    return str(self.__dict__)

  def __repr__(self): 
    return repr(self.__dict__)

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Range:

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'start', (Key, Key.thrift_spec), None, ), # 1
    (2, TType.BOOL, 'startInclusive', None, None, ), # 2
    (3, TType.STRUCT, 'stop', (Key, Key.thrift_spec), None, ), # 3
    (4, TType.BOOL, 'stopInclusive', None, None, ), # 4
  )

  def __init__(self, d=None):
    self.start = None
    self.startInclusive = None
    self.stop = None
    self.stopInclusive = None
    if isinstance(d, dict):
      if 'start' in d:
        self.start = d['start']
      if 'startInclusive' in d:
        self.startInclusive = d['startInclusive']
      if 'stop' in d:
        self.stop = d['stop']
      if 'stopInclusive' in d:
        self.stopInclusive = d['stopInclusive']

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.start = Key()
          self.start.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.BOOL:
          self.startInclusive = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.stop = Key()
          self.stop.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.BOOL:
          self.stopInclusive = iprot.readBool();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Range')
    if self.start != None:
      oprot.writeFieldBegin('start', TType.STRUCT, 1)
      self.start.write(oprot)
      oprot.writeFieldEnd()
    if self.startInclusive != None:
      oprot.writeFieldBegin('startInclusive', TType.BOOL, 2)
      oprot.writeBool(self.startInclusive)
      oprot.writeFieldEnd()
    if self.stop != None:
      oprot.writeFieldBegin('stop', TType.STRUCT, 3)
      self.stop.write(oprot)
      oprot.writeFieldEnd()
    if self.stopInclusive != None:
      oprot.writeFieldBegin('stopInclusive', TType.BOOL, 4)
      oprot.writeBool(self.stopInclusive)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __str__(self): 
    return str(self.__dict__)

  def __repr__(self): 
    return repr(self.__dict__)

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class KeyValue:

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'key', (Key, Key.thrift_spec), None, ), # 1
    (2, TType.STRING, 'value', None, None, ), # 2
  )

  def __init__(self, d=None):
    self.key = None
    self.value = None
    if isinstance(d, dict):
      if 'key' in d:
        self.key = d['key']
      if 'value' in d:
        self.value = d['value']

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.key = Key()
          self.key.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.value = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('KeyValue')
    if self.key != None:
      oprot.writeFieldBegin('key', TType.STRUCT, 1)
      self.key.write(oprot)
      oprot.writeFieldEnd()
    if self.value != None:
      oprot.writeFieldBegin('value', TType.STRING, 2)
      oprot.writeString(self.value)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __str__(self): 
    return str(self.__dict__)

  def __repr__(self): 
    return repr(self.__dict__)

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ScanResult:

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'data', (TType.STRUCT,(KeyValue, KeyValue.thrift_spec)), None, ), # 1
    (2, TType.BOOL, 'more', None, None, ), # 2
  )

  def __init__(self, d=None):
    self.data = None
    self.more = None
    if isinstance(d, dict):
      if 'data' in d:
        self.data = d['data']
      if 'more' in d:
        self.more = d['more']

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.data = []
          (_etype24, _size21) = iprot.readListBegin()
          for _i25 in xrange(_size21):
            _elem26 = KeyValue()
            _elem26.read(iprot)
            self.data.append(_elem26)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.BOOL:
          self.more = iprot.readBool();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ScanResult')
    if self.data != None:
      oprot.writeFieldBegin('data', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.data))
      for iter27 in self.data:
        iter27.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.more != None:
      oprot.writeFieldBegin('more', TType.BOOL, 2)
      oprot.writeBool(self.more)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __str__(self): 
    return str(self.__dict__)

  def __repr__(self): 
    return repr(self.__dict__)

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class InitialScan:

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'scanID', None, None, ), # 1
    (2, TType.STRUCT, 'result', (ScanResult, ScanResult.thrift_spec), None, ), # 2
  )

  def __init__(self, d=None):
    self.scanID = None
    self.result = None
    if isinstance(d, dict):
      if 'scanID' in d:
        self.scanID = d['scanID']
      if 'result' in d:
        self.result = d['result']

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.scanID = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.result = ScanResult()
          self.result.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('InitialScan')
    if self.scanID != None:
      oprot.writeFieldBegin('scanID', TType.I64, 1)
      oprot.writeI64(self.scanID)
      oprot.writeFieldEnd()
    if self.result != None:
      oprot.writeFieldBegin('result', TType.STRUCT, 2)
      self.result.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __str__(self): 
    return str(self.__dict__)

  def __repr__(self): 
    return repr(self.__dict__)

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
