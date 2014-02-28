#autogenerated by sqlautocode

import sqlalchemy.ext.declarative
import sqlalchemy.orm
from sqlalchemy import *

# generated with https://github.com/lclementi/sqlautocode
# using command line:
#  sqlautocode mysql://root:zzzzzzz@localhost/cluster -o base.py -d -g
# Then edited manually a lot


Base = sqlalchemy.ext.declarative.declarative_base()


 
class RocksBase(object):
	"""Additional base class of Rocks ORM hierarchy which includes some
	helper methods for all classes"""

	@property
	def session(self):
		"""Singelton which return the session of the object"""
		return object_session(self)


	def delete(self):
		"""instance method to autodelete the instance which calls it

		so you can use
		node.delete()"""
		self.session.delete(self)

	@classmethod
	def loadOne(cls, session, **kwargs):
		"""this method allow us to run query on all the mapping objects

		e.g.:
		node = Nodes.load(session, Name='compute-0-0', Cpus=2)

		taken from:
		http://petrushev.wordpress.com/2010/06/22/sqlalchemy-base-model/"""
		q = session.query(cls)
		filters = [getattr(cls, field_name)==kwargs[field_name] \
				for field_name in kwargs]
		return q.filter(and_(*filters)).one()



class Alias(RocksBase, Base):
    __tablename__ = 'aliases'

    __table_args__ = {}

    #column definitions
    ID = Column('ID', Integer, primary_key=True, nullable=False)
    Name = Column('Name', String(32))
    Node = Column('Node', Integer, nullable=False, default=0)

    #relation definitions


class AppGlobal(RocksBase, Base):
    __tablename__ = 'app_globals'

    __table_args__ = {}

    #column definitions
    Component = Column('Component', String(64))
    ID = Column('ID', Integer, primary_key=True, nullable=False)
    Membership = Column('Membership', Integer, nullable=False)
    Service = Column('Service', String(64))
    Value = Column('Value', TEXT())

    #relation definitions


class Appliance(RocksBase, Base):
    __tablename__ = 'appliances'

    __table_args__ = {}

    #column definitions
    ID = Column('ID', Integer, primary_key=True, nullable=False)
    Name = Column('Name', String(32), nullable=False, default='')
    Graph = Column('Graph', String(64), nullable=False, default='default')
    Node = Column('Node', String(64), nullable=False, default='')
    OS = Column('OS', Enum(u'linux', u'sunos'), nullable=False, default=u'linux')

    #relation definitions


class ApplianceAttribute(RocksBase, Base):
    __tablename__ = 'appliance_attributes'

    __table_args__ = {}

    #column definitions
    Appliance = Column('Appliance', Integer, primary_key=True, nullable=False, default=0)
    Attr = Column('Attr', String(128), primary_key=True, nullable=False)
    Value = Column('Value', TEXT())

    #relation definitions


class ApplianceRoute(RocksBase, Base):
    __tablename__ = 'appliance_routes'

    __table_args__ = {}

    #column definitions
    Appliance = Column('Appliance', Integer, primary_key=True, nullable=False)
    Gateway = Column('Gateway', String(32), nullable=False)
    Netmask = Column('Netmask', String(32), primary_key=True, nullable=False)
    Network = Column('Network', String(32), primary_key=True, nullable=False)
    Subnet = Column('Subnet', Integer, ForeignKey('subnets.ID'))

    #relation definitions


class Attribute(RocksBase, Base):
    __tablename__ = 'attributes'

    __table_args__ = {}

    #column definitions
    Attr = Column('Attr', String(128), nullable=False)
    Category = Column('Category', Integer, nullable=False)
    Catindex = Column('Catindex', Integer, ForeignKey('catindex.ID'), nullable=False)
    ID = Column('ID', Integer, primary_key=True, nullable=False)
    Shadow = Column('Shadow', TEXT())
    Value = Column('Value', TEXT())

    #relation definitions


class Boot(RocksBase, Base):
    __tablename__ = 'boot'

    __table_args__ = {}

    #column definitions
    ID = Column('ID', Integer, primary_key=True, nullable=False)
    Node = Column('Node', Integer, nullable=False, default=0)
    Action = Column('Action', Enum(u'install', u'os', u'run'))

    #relation definitions


class Bootaction(RocksBase, Base):
    __tablename__ = 'bootaction'

    __table_args__ = {}

    #column definitions
    Action = Column('Action', String(256))
    Args = Column('Args', String(1024))
    ID = Column('ID', Integer, primary_key=True, nullable=False)
    Kernel = Column('Kernel', String(256))
    Ramdisk = Column('Ramdisk', String(256))

    #relation definitions


class Bootflag(RocksBase, Base):
    __tablename__ = 'bootflags'

    __table_args__ = {}

    #column definitions
    Flags = Column('Flags', String(256))
    ID = Column('ID', Integer, primary_key=True, nullable=False)
    Node = Column('Node', Integer, nullable=False)

    #relation definitions


class Category(RocksBase, Base):
    __tablename__ = 'categories'

    __table_args__ = {}

    #column definitions
    ID = Column('ID', Integer, primary_key=True, nullable=False)
    Name = Column('Name', String(64), nullable=False)
    Description = Column('Description', String(512))

    #relation definitions


class Catindex(RocksBase, Base):
    __tablename__ = 'catindex'

    __table_args__ = {}

    #column definitions
    ID = Column('ID', Integer, primary_key=True, nullable=False)
    Name = Column('Name', String(64), nullable=False)
    Category = Column('Category', Integer, ForeignKey('categories.ID'), nullable=False)

    #relation definitions


class Distribution(RocksBase, Base):
    __tablename__ = 'distributions'

    __table_args__ = {}

    #column definitions
    ID = Column('ID', Integer, primary_key=True, nullable=False)
    Lang = Column('Lang', String(32), nullable=False, default='')
    Name = Column('Name', String(32), nullable=False, default='')
    OS_Release = Column('OS_Release', String(32), nullable=False, default='')

    #relation definitions


class Firewall(RocksBase, Base):
    __tablename__ = 'firewalls'

    __table_args__ = {}

    #column definitions
    ID = Column('ID', Integer, primary_key=True, nullable=False)
    Rulename = Column('Rulename', String(128), nullable=False)
    Rulesrc = Column('Rulesrc', Enum(u'system', u'custom'), nullable=False, default=u'custom')
    InSubnet = Column('InSubnet', Integer)
    OutSubnet = Column('OutSubnet', Integer)
    Service = Column('Service', String(256))
    Protocol = Column('Protocol', String(256))
    Action = Column('Action', String(256))
    Chain = Column('Chain', String(256))
    Flags = Column('Flags', String(256))
    Comment = Column('Comment', String(256))
    Category = Column('Category', Integer, nullable=False)
    Catindex = Column('Catindex', Integer, ForeignKey('catindex.ID'), nullable=False)

    #relation definitions


class GlobalAttribute(RocksBase, Base):
    __tablename__ = 'global_attributes'

    __table_args__ = {}

    #column definitions
    Attr = Column('Attr', String(128), primary_key=True, nullable=False)
    Value = Column('Value', TEXT())

    #relation definitions


class GlobalRoute(RocksBase, Base):
    __tablename__ = 'global_routes'

    __table_args__ = {}

    #column definitions
    Gateway = Column('Gateway', String(32), nullable=False)
    Netmask = Column('Netmask', String(32), primary_key=True, nullable=False)
    Network = Column('Network', String(32), primary_key=True, nullable=False)
    Subnet = Column('Subnet', Integer, ForeignKey('subnets.ID'))

    #relation definitions


class Hostselection(RocksBase, Base):
    __tablename__ = 'hostselections'

    __table_args__ = {}

    #column definitions
    Category = Column('Category', Integer, ForeignKey('categories.ID'), nullable=False)
    Host = Column('Host', Integer, ForeignKey('catindex.ID'), nullable=False)
    ID = Column('ID', Integer, primary_key=True, nullable=False)
    Selection = Column('Selection', Integer, ForeignKey('catindex.ID'), nullable=False)

    #relation definitions


class Membership(RocksBase, Base):
    __tablename__ = 'memberships'

    __table_args__ = {}

    #column definitions
    ID = Column('ID', Integer, primary_key=True, nullable=False)
    Name = Column('Name', String(64), nullable=False)
    Appliance = Column('Appliance', Integer, ForeignKey('appliances.ID'), default=0)
    Distribution = Column('Distribution', Integer, ForeignKey('distributions.ID'), default=1)
    Public = Column('Public', Enum(u'yes', u'no'), nullable=False, default=u'no')

    #relation definitions


class Network(RocksBase, Base):
    __tablename__ = 'networks'

    __table_args__ = {}

    #column definitions
    Channel = Column('Channel', String(128))
    Device = Column('Device', String(32))
    Gateway = Column('Gateway', String(32))
    ID = Column('ID', Integer, primary_key=True, nullable=False)
    IP = Column('IP', String(32))
    MAC = Column('MAC', String(64))
    Module = Column('Module', String(128))
    Name = Column('Name', String(128))
    Netmask = Column('Netmask', String(32))
    Node = Column('Node', Integer, ForeignKey('nodes.ID'))
    Options = Column('Options', String(128))
    Subnet = Column('Subnet', Integer, ForeignKey('subnets.ID'))
    VlanID = Column('VlanID', Integer)

    #relation definitions


class Node(RocksBase, Base):
    __tablename__ = 'nodes'

    __table_args__ = {}

    #column definitions
    ID = Column('ID', Integer, primary_key=True, nullable=False)
    Name = Column('Name', String(128))
    Membership = Column('Membership', Integer, ForeignKey('memberships.ID'), default=2)
    CPUs = Column('CPUs', Integer, nullable=False, default=1)
    Rack = Column('Rack', Integer)
    Rank = Column('Rank', Integer)
    Arch = Column('Arch', String(32))
    OS = Column('OS', Enum(u'linux', u'sunos'), nullable=False, default=u'linux')
    RunAction = Column('RunAction', String(64), default='os')
    InstallAction = Column('InstallAction', String(64), default='install')

    #relation definitions
    # map the networks belonging to this node
    Networks = sqlalchemy.orm.relationship("Network")

    def __repr__(self):
        return "<Node(name='%s')>" % (self.Name)



class NodeAttribute(RocksBase, Base):
    __tablename__ = 'node_attributes'

    __table_args__ = {}

    #column definitions
    Attr = Column('Attr', String(128), primary_key=True, nullable=False)
    Node = Column('Node', Integer, primary_key=True, nullable=False)
    Value = Column('Value', TEXT())

    #relation definitions


class NodeRoll(RocksBase, Base):
    __tablename__ = 'node_rolls'

    __table_args__ = {}

    #column definitions
    Node = Column('Node', Integer, primary_key=True, nullable=False)
    RollID = Column('RollID', Integer, primary_key=True, nullable=False)

    #relation definitions


class NodeRoute(RocksBase, Base):
    __tablename__ = 'node_routes'

    __table_args__ = {}

    #column definitions
    Gateway = Column('Gateway', String(32), nullable=False)
    Netmask = Column('Netmask', String(32), primary_key=True, nullable=False)
    Network = Column('Network', String(32), primary_key=True, nullable=False)
    Node = Column('Node', Integer, primary_key=True, nullable=False)
    Subnet = Column('Subnet', Integer, ForeignKey('subnets.ID'))

    #relation definitions


class OsAttribute(RocksBase, Base):
    __tablename__ = 'os_attributes'

    __table_args__ = {}

    #column definitions
    Attr = Column('Attr', String(128), primary_key=True, nullable=False)
    OS = Column('OS', Enum(u'sunos', u'linux'), primary_key=True, nullable=False, default=u'linux')
    Value = Column('Value', TEXT())

    #relation definitions


class OsRoute(RocksBase, Base):
    __tablename__ = 'os_routes'

    __table_args__ = {}

    #column definitions
    Gateway = Column('Gateway', String(32), nullable=False)
    Netmask = Column('Netmask', String(32), primary_key=True, nullable=False)
    Network = Column('Network', String(32), primary_key=True, nullable=False)
    OS = Column('OS', Enum(u'sunos', u'linux'), primary_key=True, nullable=False, default=u'linux')
    Subnet = Column('Subnet', Integer, ForeignKey('subnets.ID'))

    #relation definitions


class Partition(RocksBase, Base):
    __tablename__ = 'partitions'

    __table_args__ = {}

    #column definitions
    Device = Column('Device', String(128), nullable=False)
    FormatFlags = Column('FormatFlags', String(128), nullable=False)
    FsType = Column('FsType', String(128), nullable=False)
    ID = Column('ID', Integer, primary_key=True, nullable=False)
    Mountpoint = Column('Mountpoint', String(128), nullable=False)
    Node = Column('Node', Integer, nullable=False)
    PartitionFlags = Column('PartitionFlags', String(128), nullable=False)
    PartitionID = Column('PartitionID', String(128), nullable=False)
    PartitionSize = Column('PartitionSize', String(128), nullable=False)
    SectorStart = Column('SectorStart', String(128), nullable=False)

    #relation definitions


class PublicKey(RocksBase, Base):
    __tablename__ = 'public_keys'

    __table_args__ = {}

    #column definitions
    Description = Column('Description', String(4096))
    ID = Column('ID', Integer, primary_key=True, nullable=False)
    Node = Column('Node', Integer, nullable=False)
    Public_Key = Column('Public_Key', String(4096))

    #relation definitions


class Resolvechain(RocksBase, Base):
    __tablename__ = 'resolvechain'

    __table_args__ = {}

    #column definitions
    ID = Column('ID', Integer, primary_key=True, nullable=False)
    Name = Column('Name', String(64), nullable=False, default=0)
    Category = Column('Category', Integer, ForeignKey('categories.ID'), nullable=False)
    Precedence = Column('Precedence', Integer, nullable=False, default=10)

    #relation definitions


class Roll(RocksBase, Base):
    __tablename__ = 'rolls'

    __table_args__ = {}

    #column definitions
    ID = Column('ID', Integer, primary_key=True, nullable=False)
    Name = Column('Name', String(128), nullable=False)
    Version = Column('Version', String(32), nullable=False)
    Arch = Column('Arch', String(32), nullable=False)
    OS = Column('OS', Enum(u'linux', u'sunos'), nullable=False, default=u'linux')
    Enabled = Column('Enabled', Enum(u'yes', u'no'), nullable=False, default=u'yes')

    #relation definitions


class SecGlobalAttribute(RocksBase, Base):
    __tablename__ = 'sec_global_attributes'

    __table_args__ = {}

    #column definitions
    Attr = Column('Attr', String(128), primary_key=True, nullable=False)
    Enc = Column('Enc', String(64))
    Value = Column('Value', TEXT())

    #relation definitions


class SecNodeAttribute(RocksBase, Base):
    __tablename__ = 'sec_node_attributes'

    __table_args__ = {}

    #column definitions
    Attr = Column('Attr', String(128), primary_key=True, nullable=False)
    Enc = Column('Enc', String(64))
    Node = Column('Node', Integer, primary_key=True, nullable=False)
    Value = Column('Value', TEXT())

    #relation definitions


class Subnet(RocksBase, Base):
    __tablename__ = 'subnets'

    __table_args__ = {}

    #column definitions
    ID = Column('ID', Integer, primary_key=True, nullable=False)
    name = Column('name', String(32), nullable=False, unique=True)
    dnszone = Column('dnszone', String(64), nullable=False, unique=True)
    subnet = Column('subnet', String(32), nullable=False)
    netmask = Column('netmask', String(32), nullable=False)
    mtu = Column('mtu', Integer, default=1500)
    servedns = Column('servedns', Boolean, default=False)

    #relation definitions


class VmDisk(RocksBase, Base):
    __tablename__ = 'vm_disks'

    __table_args__ = {}

    #column definitions
    Device = Column('Device', String(512))
    ID = Column('ID', Integer, primary_key=True, nullable=False)
    Mode = Column('Mode', String(64))
    Name = Column('Name', String(512))
    Prefix = Column('Prefix', String(512))
    Size = Column('Size', Integer, nullable=False)
    VBD_Type = Column('VBD_Type', String(64))
    Vm_Node = Column('Vm_Node', Integer, nullable=False)

    #relation definitions


class VmNode(RocksBase, Base):
    __tablename__ = 'vm_nodes'

    __table_args__ = {}

    #column definitions
    ID = Column('ID', Integer, primary_key=True, nullable=False)
    Mem = Column('Mem', Integer, nullable=False)
    Node = Column('Node', Integer, nullable=False)
    PhysNode = Column('PhysNode', Integer, nullable=False)
    Slice = Column('Slice', Integer, nullable=False)
    Virt_Type = Column('Virt_Type', String(64))
    cdrom_path = Column('cdrom_path', String(512))

    #relation definitions

