'''
from mininet.topo import Topo
from mininet.log import setLogLevel, info

class MyTopo( Topo ):

    def addSwitch(self, name, **opts ):
        kwargs = { 'protocols' : 'OpenFlow13'}
        kwargs.update( opts )
        return super(MyTopo, self).addSwitch( name, **kwargs )

    def __init__( self ):
        "Create MyTopo topology..."

        # Inisialisasi Topology
        Topo.__init__( self )

        # Add hosts and switches
        h1 = self.addHost( 'h1', ip='192.168.1.1' )
        h2 = self.addHost( 'h2', ip='192.168.1.2' )
        h3 = self.addHost( 'h3', ip='192.168.1.3' )
        h4 = self.addHost( 'h4', ip='192.168.1.4' )
        h5 = self.addHost( 'h5', ip='192.168.1.5' )
        h6 = self.addHost( 'h6', ip='192.168.1.6' )

        s1 = self.addSwitch ( 's1' )
        s2 = self.addSwitch( 's2' )

# Add links
        self.addLink ( h1,s1 )
        self.addLink ( h2,s1 )
        self.addLink ( h3,s2 )
        self.addLink ( h4,s2 )
        self.addLink ( h5,s3 )
        self.addLink ( h6,s3 )

topos = { 'mytopo': ( lambda: MyTopo() ) }