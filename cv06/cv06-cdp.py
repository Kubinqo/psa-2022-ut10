#!/user/bin/env python3
import struct
from scapy.all import *

def macToBytes(mac):
   return bytes.fromhex(mac.replace(":", ""))

class ethFrame():
    def __init__(self, smac):
        self._dmac = "01:00:0C:CC:CC:CC"
        self._smac = smac
        self._length = 0
    
    def addPayLoad(self, payload):
        self._payload = payload

    def toBytes(self):
        payloadBytes = self._payload.toBytes()
        self._length = len(payloadBytes)

        return macToBytes(self._dmac) + macToBytes(self._smac) + struct.pack("!H", self._length)  + payloadBytes


class LLC():
    def __init__(self):
        self._dsap = 0xAA
        self._ssap = 0XAA
        self._ctrl = 0x03
        self._oui = "00000C"
        self._pid = 0x2000      #CDP

    def addPayLoad(self, payload):
        self._payload = payload

    def toBytes(self):
        return struct.pack("!3B", self._dsap, self._ssap, self._ctrl) + macToBytes(self._oui) + struct.pack("!H", self._pid) + self._payload.toBytes()


class CDP():
    def __init__(self):
        self._version = 1
        self._ttl = 180
        self._checksum = 0
        self._payload = list()
    
    def addPayload(self, payload):
        self._payload.append(payload)

    def toBytes(self):
        bajty = struct.pack("!BBH", self._version, self._ttl, self._checksum)

        for tlv in self._payload:
            bajty += tlv.toBytes()

        return bajty

class TLV():
    def __init__(self, type):
        self._type = type
        self._length = 4
    
    def toBytes(self):
        return struct.pack("!2H", self._type, self._length)

class TLVDeviceID(TLV):
    def __init__(self, hostname):
        TLV.__init__(self, 0X0001)     #0X0001 je DevideID hodnota -> obrazok na nete
        self._hostname = hostname

    def toBytes(self):
        hostname_bajty = self._hostname.encode()
        self._length += len(hostname_bajty)

        return TLV.toBytes(self) + hostname_bajty

class TLVPlatform(TLVDeviceID):
    def __init__(self, platform):
        super().__init__(platform)
        self._type = 0x0006

class TLVSoftware(TLVDeviceID):
    def __init__(self, software):
        super().__init__(software)
        self._type = 0x0005


if __name__ == "__main__":

    device = TLVDeviceID("kubinkovPC")
    platform = TLVPlatform("Python")
    software = TLVSoftware("Python 3.10.7 on Windows 10 Pro x64")

    cdp = CDP()
    cdp.addPayload(device)
    cdp.addPayload(platform)
    cdp.addPayload(software)

    llc = LLC()
    llc.addPayLoad(cdp)

    ramec = ethFrame("01:02:03:04:05:06")
    ramec.addPayLoad(llc)
    bajty = ramec.toBytes()

    #IFACES.show()

    rozhranie = IFACES.dev_from_index(22)
    sock = conf.L2socket(iface=rozhranie)

    sock.send(bajty)
    sock.close()