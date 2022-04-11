#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink, Intf
from mininet.log import setLogLevel, info

def myNetwork():

    net = Mininet( topo=None,
                   build=False)

    info( '*** Adding controller\n' )
    net.addController(name='c0')

    info( '*** Add switches\n')
    s2 = net.addSwitch('s2', log_file="s2.log")
    s1 = net.addSwitch('s1', log_file="s1.log")
    Intf( 'enp0s3', node=s1 )

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', ip='0.0.0.0')

    info( '*** Add links\n')
    net.addLink(h1, s2)
    net.addLink(s1, s2, cls=TCLink,bw=0.25)

    info( '*** Starting network\n')
    net.start()
    h1.cmdPrint('dhclient '+h1.defaultIntf().name)
    h1.cmd('rm results/scenario7/STD-WGET-256k.txt')
    h1.cmd('sudo ethtool -K h1-eth0 gro off gso off tso off')
    s2.cmd('sudo ethtool -K s2-eth1 gro off gso off tso off')
    s2.cmd('sudo ethtool -K s2-eth2 gro off gso off tso off')
    s1.cmd('sudo ethtool -K s1-eth1 gro off gso off tso off')
    s1.cmd('sudo ethtool -K enp0s3 gro off gso off tso off')

    h1.cmd('wget http://sbrc2010.inf.ufrgs.br/anais/data/pdf/minicursos.pdf --progress=dot:binary -o results/scenario7/STD-WGET-256k.txt')
    #CLI(net)
    net.stop()

if __name__ == '__main__':
##    setLogLevel( 'info' )
    myNetwork()
