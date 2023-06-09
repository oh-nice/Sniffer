from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def _missing_(cls, value: object):
        return cls.UNKNOWN  # type: ignore


# 以太网类型字段部分含义
class EthernetType(BaseEnum):
    IPv4 = 0x0800
    ARP = 0x0806
    # SNMP = 0x814C
    # IPv6 = 0x86DD
    # LLDP = 0x86DD
    UNKNOWN = 'UNKNOWN'


# ARP类型字段含义
class ARPType(BaseEnum):
    request = 1
    reply = 2
    r_request = 3
    r_reply = 4
    UNKNOWN = 'UNKNOWN'


# IPv4协议类型字段部分含义
class IPProtocol(BaseEnum):
    ICMPv4 = 1
    # IGMP = 2
    IPv4 = 4
    TCP = 6
    UDP = 17
    # IPv6 = 41
    # ICMPv6 = 58
    UNKNOWN = 'UNKNOWN'


# IPv6协议类型字段部分含义
class IP6Protocol(BaseEnum):
    UNKNOWN = 'UNKNOWN'


# ICMP协议类型字段部分含义
class ICMPv4Type(BaseEnum):
    reply = 0
    request = 8
    UNKNOWN = 'UNKNOWN'


if __name__ == "__main__":
    print(IPProtocol['TCP'])
