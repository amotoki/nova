# Copyright 2012 OpenStack LLC.
# All Rights Reserved
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import socket

from nova import flags
from nova.openstack.common import cfg

network_opts = [
    cfg.StrOpt('flat_network_bridge',
               default=None,
               help='Bridge for simple network instances'),
    cfg.StrOpt('flat_network_dns',
               default='8.8.4.4',
               help='Dns for simple network'),
    cfg.BoolOpt('flat_injected',
                default=False,
                help='Whether to attempt to inject network setup into guest'),
    cfg.StrOpt('flat_interface',
               default=None,
               help='FlatDhcp will bridge into this interface if set'),
    cfg.IntOpt('vlan_start',
               default=100,
               help='First VLAN for private networks'),
    cfg.StrOpt('vlan_interface',
               default=None,
               help='vlans will bridge into this interface if set'),
    cfg.IntOpt('num_networks',
               default=1,
               help='Number of networks to support'),
    cfg.StrOpt('vpn_ip',
               default='$my_ip',
               help='Public IP for the cloudpipe VPN servers'),
    cfg.IntOpt('vpn_start',
               default=1000,
               help='First Vpn port for private networks'),
    cfg.BoolOpt('multi_host',
                default=False,
                help='Default value for multi_host in networks'),
    cfg.IntOpt('network_size',
               default=256,
               help='Number of addresses in each private subnet'),
    cfg.StrOpt('floating_range',
               default='4.4.4.0/24',
               help='Floating IP address block'),
    cfg.StrOpt('default_floating_pool',
               default='nova',
               help='Default pool for floating ips'),
    cfg.StrOpt('fixed_range',
               default='10.0.0.0/8',
               help='Fixed IP address block'),
    cfg.StrOpt('fixed_range_v6',
               default='fd00::/48',
               help='Fixed IPv6 address block'),
    cfg.StrOpt('gateway',
               default=None,
               help='Default IPv4 gateway'),
    cfg.StrOpt('gateway_v6',
               default=None,
               help='Default IPv6 gateway'),
    cfg.IntOpt('cnt_vpn_clients',
               default=0,
               help='Number of addresses reserved for vpn clients'),
    cfg.IntOpt('fixed_ip_disassociate_timeout',
               default=600,
               help='Seconds after which a deallocated ip is disassociated'),
    cfg.IntOpt('create_unique_mac_address_attempts',
               default=5,
               help='Number of attempts to create unique mac address'),
    cfg.BoolOpt('auto_assign_floating_ip',
                default=False,
                help='Autoassigning floating ip to VM'),
    cfg.StrOpt('network_host',
               default=socket.gethostname(),
               help='Network host to use for ip allocation in flat modes'),
    cfg.BoolOpt('fake_call',
                default=False,
                help='If True, skip using the queue and make local calls'),
    cfg.BoolOpt('force_dhcp_release',
                default=False,
                help='If True, send a dhcp release on instance termination'),
    cfg.StrOpt('dhcp_domain',
               default='novalocal',
               help='domain to use for building the hostnames'),
    cfg.StrOpt('l3_lib',
               default='nova.network.l3.LinuxNetL3',
               help="Indicates underlying L3 management library")
    ]

FLAGS = flags.FLAGS
FLAGS.register_opts(network_opts)
