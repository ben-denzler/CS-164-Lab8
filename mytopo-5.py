"""
Custom Topology:

    +--------+   +--------+   +--------+
    | client |---| router |---| server |
    +--------+   +--------+   +--------+

"""

from mininet.topo import Topo

class MyTopo(Topo):
    def build(self):
        # Add hosts
        client = self.addHost('client')
        server = self.addHost('server')
        router = self.addHost('router')

	# Add Link
        self.addLink(client, router)
        self.addLink(router, server)

topos = {'mytopo': (lambda: MyTopo())}
