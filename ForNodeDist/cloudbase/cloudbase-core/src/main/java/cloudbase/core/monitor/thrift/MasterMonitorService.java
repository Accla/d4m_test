/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 */
package cloudbase.core.monitor.thrift;

import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.HashSet;
import com.facebook.thrift.*;

import com.facebook.thrift.protocol.*;
import com.facebook.thrift.transport.*;

public class MasterMonitorService {

  public interface Iface {

    public MasterMonitorInfo getMasterStats() throws TException;

  }

  public static class Client implements Iface {
    public Client(TProtocol prot)
    {
      this(prot, prot);
    }

    public Client(TProtocol iprot, TProtocol oprot)
    {
      iprot_ = iprot;
      oprot_ = oprot;
    }

    protected TProtocol iprot_;
    protected TProtocol oprot_;

    protected int seqid_;

    public TProtocol getInputProtocol()
    {
      return this.iprot_;
    }

    public TProtocol getOutputProtocol()
    {
      return this.oprot_;
    }

    public MasterMonitorInfo getMasterStats() throws TException
    {
      send_getMasterStats();
      return recv_getMasterStats();
    }

    public void send_getMasterStats() throws TException
    {
      oprot_.writeMessageBegin(new TMessage("getMasterStats", TMessageType.CALL, seqid_));
      getMasterStats_args args = new getMasterStats_args();
      args.write(oprot_);
      oprot_.writeMessageEnd();
      oprot_.getTransport().flush();
    }

    public MasterMonitorInfo recv_getMasterStats() throws TException
    {
      TMessage msg = iprot_.readMessageBegin();
      if (msg.type == TMessageType.EXCEPTION) {
        TApplicationException x = TApplicationException.read(iprot_);
        iprot_.readMessageEnd();
        throw x;
      }
      getMasterStats_result result = new getMasterStats_result();
      result.read(iprot_);
      iprot_.readMessageEnd();
      if (result.__isset.success) {
        return result.success;
      }
      throw new TApplicationException(TApplicationException.MISSING_RESULT, "getMasterStats failed: unknown result");
    }

  }
  public static class Processor implements TProcessor {
    public Processor(Iface iface)
    {
      iface_ = iface;
      processMap_.put("getMasterStats", new getMasterStats());
    }

    protected static interface ProcessFunction {
      public void process(int seqid, TProtocol iprot, TProtocol oprot) throws TException;
    }

    private Iface iface_;
    protected final HashMap<String,ProcessFunction> processMap_ = new HashMap<String,ProcessFunction>();

    public boolean process(TProtocol iprot, TProtocol oprot) throws TException
    {
      TMessage msg = iprot.readMessageBegin();
      ProcessFunction fn = processMap_.get(msg.name);
      if (fn == null) {
        TProtocolUtil.skip(iprot, TType.STRUCT);
        iprot.readMessageEnd();
        TApplicationException x = new TApplicationException(TApplicationException.UNKNOWN_METHOD, "Invalid method name: '"+msg.name+"'");
        oprot.writeMessageBegin(new TMessage(msg.name, TMessageType.EXCEPTION, msg.seqid));
        x.write(oprot);
        oprot.writeMessageEnd();
        oprot.getTransport().flush();
        return true;
      }
      fn.process(msg.seqid, iprot, oprot);
      return true;
    }

    private class getMasterStats implements ProcessFunction {
      public void process(int seqid, TProtocol iprot, TProtocol oprot) throws TException
      {
        getMasterStats_args args = new getMasterStats_args();
        args.read(iprot);
        iprot.readMessageEnd();
        getMasterStats_result result = new getMasterStats_result();
        result.success = iface_.getMasterStats();
        result.__isset.success = true;
        oprot.writeMessageBegin(new TMessage("getMasterStats", TMessageType.REPLY, seqid));
        result.write(oprot);
        oprot.writeMessageEnd();
        oprot.getTransport().flush();
      }

    }

  }

  public static class getMasterStats_args implements TBase, java.io.Serializable   {
    public getMasterStats_args() {
    }

    public boolean equals(Object that) {
      if (that == null)
        return false;
      if (that instanceof getMasterStats_args)
        return this.equals((getMasterStats_args)that);
      return false;
    }

    public boolean equals(getMasterStats_args that) {
      if (that == null)
        return false;

      return true;
    }

    public int hashCode() {
      return 0;
    }

    public void read(TProtocol iprot) throws TException {
      TField field;
      iprot.readStructBegin();
      while (true)
      {
        field = iprot.readFieldBegin();
        if (field.type == TType.STOP) { 
          break;
        }
        switch (field.id)
        {
          default:
            TProtocolUtil.skip(iprot, field.type);
            break;
        }
        iprot.readFieldEnd();
      }
      iprot.readStructEnd();
    }

    public void write(TProtocol oprot) throws TException {
      TStruct struct = new TStruct("getMasterStats_args");
      oprot.writeStructBegin(struct);
      oprot.writeFieldStop();
      oprot.writeStructEnd();
    }

    public String toString() {
      StringBuilder sb = new StringBuilder("getMasterStats_args(");
      sb.append(")");
      return sb.toString();
    }

  }

  public static class getMasterStats_result implements TBase, java.io.Serializable   {
    public MasterMonitorInfo success;

    public final Isset __isset = new Isset();
    public static final class Isset implements java.io.Serializable {
      public boolean success = false;
    }

    public getMasterStats_result() {
    }

    public getMasterStats_result(
      MasterMonitorInfo success)
    {
      this();
      this.success = success;
      this.__isset.success = true;
    }

    public boolean equals(Object that) {
      if (that == null)
        return false;
      if (that instanceof getMasterStats_result)
        return this.equals((getMasterStats_result)that);
      return false;
    }

    public boolean equals(getMasterStats_result that) {
      if (that == null)
        return false;

      boolean this_present_success = true && (this.success != null);
      boolean that_present_success = true && (that.success != null);
      if (this_present_success || that_present_success) {
        if (!(this_present_success && that_present_success))
          return false;
        if (!this.success.equals(that.success))
          return false;
      }

      return true;
    }

    public int hashCode() {
      return 0;
    }

    public void read(TProtocol iprot) throws TException {
      TField field;
      iprot.readStructBegin();
      while (true)
      {
        field = iprot.readFieldBegin();
        if (field.type == TType.STOP) { 
          break;
        }
        switch (field.id)
        {
          case 0:
            if (field.type == TType.STRUCT) {
              this.success = new MasterMonitorInfo();
              this.success.read(iprot);
              this.__isset.success = true;
            } else { 
              TProtocolUtil.skip(iprot, field.type);
            }
            break;
          default:
            TProtocolUtil.skip(iprot, field.type);
            break;
        }
        iprot.readFieldEnd();
      }
      iprot.readStructEnd();
    }

    public void write(TProtocol oprot) throws TException {
      TStruct struct = new TStruct("getMasterStats_result");
      oprot.writeStructBegin(struct);
      TField field = new TField();

      if (this.__isset.success) {
        if (this.success != null) {
          field.name = "success";
          field.type = TType.STRUCT;
          field.id = 0;
          oprot.writeFieldBegin(field);
          this.success.write(oprot);
          oprot.writeFieldEnd();
        }
      }
      oprot.writeFieldStop();
      oprot.writeStructEnd();
    }

    public String toString() {
      StringBuilder sb = new StringBuilder("getMasterStats_result(");
      sb.append("success:");
      sb.append(this.success.toString());
      sb.append(")");
      return sb.toString();
    }

  }

}