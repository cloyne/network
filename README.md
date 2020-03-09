# Cloyne network

We are migrating documentation to the cloyne/network
[wiki](http://github.com/cloyne/network/wiki). This page is a quick reference
for internet and intranet connectivity.
For in depth documentation, check out:
* [Domains and Servers](https://github.com/cloyne/network/wiki/Domains-and-Servers)
    * Domain names and how to set up subdomains
    * Detailed information about each server's hardware, and an overview of
        software configuration
* [Internet Uplink and LAN](https://github.com/cloyne/network/wiki/Internet-Uplink-and-LAN)
    * Detailed router info
    * Access Points
    * Switches
    * Mesh
    * Kingman
    * Other
* [Printer](https://github.com/cloyne/network/wiki/Printer) - currently just
    contains outdated information but hopefully clohard will update it soon :)

Documentation of our [Web Apps](http://github.com/cloyne/servers/wiki) has been relocated to the
    [cloyne/servers](http://github.com/cloyne/servers) repository's wiki.
    * Sympa (cloyne.org/lists)
    * Cloyne Blog (cloyne.org)

## [Internet uplink](https://github.com/cloyne/network/wiki/Internet-Uplink-and-LAN)

Through [Hurricane Electric](https://he.net/).

    64.62.133.40/29
    Network:              64.62.133.40
    Netmask:              255.255.255.248
    Broadcast:            64.62.133.47
    DNS:                  216.218.196.2
    Usable address range: 64.62.133.41 - 64.62.133.46 (6 addresses)

    2001:470:104::/48
    Network:              2001:470:104::
    DNS:                  2001:470:0:473::473

    64.62.214.116/30 (point to point connection)
    HE:                   64.62.214.117
    Cloyne:               64.62.214.118

    2001:470:1:1c5::/126 (point to point connection)
    HE:                   2001:470:1:1c5::1
    Cloyne:               2001:470:1:1c5::2

Bandwidth limit is 100 Mbit/s.

## Static IPv4 addresses at a glance:

Device       | Internal IP        | External IP          | Hostname            | Hardware | Other
-------------|--------------------|----------------------|---------------------|----------|-------
`he-router`  |                    | 64.63.133.41         | he.cloyne.org       | [Mikrotik RouterBoard 2011UiAS-RM](http://routerboard.com/RB2011UiAS-RM) | Other IP: 64.62.214.118. Netmask: 255.255.255.248 (/29).
`clo-router` | 10.20.32.1         | 64.62.133.42         | router.cloyne.org   | [Mikrotik RouterBoard 850Gx2](http://routerboard.com/RB850Gx2) | Netmask: 255.255.255.248 (/29). DHCP client range: 10.20.32.100 - 10.20.35.190 (859 addresses)
`server1`    |                    | 64.62.133.43 (eth0)  | server1.cloyne.org  | 2-core Intel Atom processor and 4GB RAM. 64 GB SSD. | Secondary DNS server. Running Ubuntu LTS distribution as a host for [cloyne/powerdns-secondary](https://github.com/cloyne/docker-powerdns-secondary) Docker image.
`server2`    | 192.168.88.10 (eth1) | 64.62.133.44 (eth0)  | server2.cloyne.org  | 2-core Intel Atom processor and 4GB RAM. Partitions: 64 GB SSD (sda) + 2x 1500 GB HDD (sdb and sdc) + 2x 500 GB HDD (sdd, sde).| Hosts  primary DNS server (using [cloyne/powerdns-master](https://github.com/cloyne/docker-powerdns-master) Docker image), Mail server, and Cloyne.org blog.
`server3`    | 192.168.88.11 (p1p2) | 64.62.133.45 (p1p1)  | server3.cloyne.org  | contains 8 x 3 TB hard drives, 6 x 750 GB drives, configured in pairs into RAID-1, combined into a 13 TB LVM volume.
kingman      |                    | 64.62.133.46         | kingmanhall.org

See also on our wiki:
* [Internet uplink and LAN](https://github.com/cloyne/network/wiki/Internet-Uplink-and-LAN)
* [Domains and Servers](https://github.com/cloyne/network/wiki/Domains-and-Servers)

## Network Devices by IP

Device                    | Internal IP                                 | MAC Address       | Location       | Hardware    | Other
--------------------------|---------------------------------------------|-------------------|----------------|-------------|-------
Network Room Switch 2     | [10.20.32.20](http://10.20.32.20)           | fc:75:16:68:b4:49 | Network Room   |             |
C2K  Switch               | [10.20.32.21](http://10.20.32.21)           | 14:d6:4d:1e:4:16  | C2K            |             |
E2SC Switch               | [10.20.32.22](http://10.20.32.22)           | fc:75:16:68:bb:f9 | E2SC           |             |
C3L  Switch               | [10.20.32.23](http://10.20.32.23)           | fc:75:16:68:bb:c9 | C3L            |             |
E3SB Switch               | [10.20.32.24](http://10.20.32.24)           | fc:75:16:68:b4:19 | E3SB           |             |
Mail Room Switch          | [10.20.32.25](http://10.20.32.25)           | 14:d6:4d:1e:03:e6 | Mail Room      |             |
W2SB Switch               | [10.20.32.26](http://10.20.32.26)           | fc:75:16:68:b4:a9 | W2SB           |             |
Network Room Switch 1     | [10.20.32.27](http://10.20.32.27)           | fc:75:16:68:bb:99 | Network Room   |             |
W3SB Switch               | [10.20.32.28](http://10.20.32.28)           | fc:75:16:68:b4:79 | W3SB           |             |
Unused                    | 10.20.32.29 - 10.20.32.39 (10 IPs)          |                   |                |             |
`FamilyRoom` Access Point | [10.20.32.40](http://10.20.32.40)           | 04:18:d6:20:60:44 | LibEd Room     | Ubiquiti UniFi AP Pro  | channel 6, 48
`w3j`        Access Point | [10.20.32.41](http://10.20.32.41)           | e8:94:f6:68:87:51 | W3J            | TP-LINK TL-WR1043ND v2 | channel 11
`e2j`        Access Point | [10.20.32.42](http://10.20.32.42)           | 04:18:d6:20:58:df | E2J            | Ubiquiti UniFi AP Pro  | channel 6, 132
`w2c`        Access Point | [10.20.32.43](http://10.20.32.43)           | 04:18:d6:20:5c:fe | W2C            | Ubiquiti UniFi AP Pro  | channel 6, 124
`w3a`        Access Point | [10.20.32.44](http://10.20.32.44)           | c0:4a:00:5d:c3:f3 | W3A            | TP-LINK TL-WR1043ND v2 | channel 1
`w0b`        Access Point | [10.20.32.45](http://10.20.32.45)           | c0:4a:00:40:e3:61 | W0B            | TP-LINK TL-WR1043ND v2 | channel 1
`e3ab`       Access Point | [10.20.32.46](http://10.20.32.46)           | e8:94:f6:68:84:78 | E3AB           | TP-LINK TL-WR1043ND v2 | channel 1
`GreatHall`  Access Point | [10.20.32.47](http://10.20.32.47)           | 04:18:d6:20:59:c8 | Dining Room    | Ubiquiti UniFi AP Pro  | channel 1, 116
`e2d`        Access Point | [10.20.32.48](http://10.20.32.48)           | 04:18:d6:20:5a:1f | E2D            | Ubiquiti UniFi AP Pro  | channel 11, 108
`w2h`        Access Point | [10.20.32.49](http://10.20.32.49)           | 04:18:d6:20:59:c7 | W2H            | Ubiquiti UniFi AP Pro  | channel 1, 100
`c2p`        Access Point | [10.20.32.50](http://10.20.32.50)           | 04:18:d6:20:58:e4 | C2P            | Ubiquiti UniFi AP Pro  | channel 11, 64
`c2c`        Access Point | [10.20.32.51](http://10.20.32.51)           | 04:18:d6:20:5f:e6 | C2C            | Ubiquiti UniFi AP Pro  | channel 1, 56
`w1e`        Access Point | [10.20.32.52](http://10.20.32.52)           | 90:f6:52:ea:05:ec | W1E            | TP-LINK TL-WR1043ND    | channel 11
`c3k`        Access Point | [10.20.32.53](http://10.20.32.53)           | 90:F6:52:2A:08:54 | C3K            | TP-LINK TL-WR1043ND    | channel 6
`e3j`        Access Point | [10.20.32.54](http://10.20.32.54)           | 04:18:d6:20:5d:20 | E3J            | Ubiquiti UniFi AP Pro | channel 11, channel 36
Unused                    | 10.20.32.54 - 10.20.32.89 (36 IPs)          |                   |                |             |
printer1                  | [10.20.32.90](http://10.20.32.90)           |                   | Pool/Mail room | | [printer1.cloyne.org](printer1.cloyne.org) | TODO: add info for new printer Spring 2019
label printer             | [10.20.32.91](http://10.20.32.91)           | 00:80:92:CF:09:B1 |                | Brother QL-710W
Makerspace printer        | [10.20.32.92](http://10.20.32.92)           | 00:1E:8F:98:3B:1E | W0B            | Canon MX870 | [printer2.cloyne.org](printer2.cloyne.org)
Unused                    | 10.20.32.93 - 10.20.32.99 (10 IPs)          |                   |                |             |
DHCP client range         | 10.20.32.100 - 10.20.35.190 (859 addresses) |                   |                |             | Do not assign static IPs in this range!
clo-kng      Antenna      | [10.20.35.210](http://10.20.35.210)         | 24:A4:3C:9C:F6:AD | Cloyne E3      |
clo-euc      Antenna      | [10.20.35.211](http://10.20.35.211)         | 04:18:D6:A4:84:77 | Cloyne W3      | Not currently used
kng-clo      Antenna      | [10.20.35.212](http://10.20.35.212)         | 24:A4:3C:BE:4E:A0 | Kingman roof   | (temporary moved from 10.20.99.210 until Kingman gets its own router)
Study Room AP             | [10.20.35.220](http://10.20.35.220)         | 80:2a:a8:13:4b:ed | Ubiquiti UniFi AP-AC-Pro| channel 11, 44
Network Closet AP         | [10.20.35.221](http://10.20.35.221)         | 80:2a:a8:13:4a:19 | Ubiquiti UniFi AP-AC-Pro | channel 1, 149
Dining Room AP            | [10.20.35.222](http://10.20.35.222)         | 80:2a:a8:13:4b:bb | Ubiquiti UniFi AP-AC-Pro | channel 1, 36
2nd Floor North           | [10.20.35.223](http://10.20.35.223)         | 80:2a:a8:13:4b:c5 | Ubiquiti UniFi AP-AC-Pro | channel 6, 161
clo-euc      Antenna      | [10.20.35.240](http://10.20.35.240)         | B8:27:EB:7A:6A:BB | KORUZA
euc-clo      Antenna      | [10.20.35.241](http://10.20.35.241)         | B8:27:EB:23:21:E7 | KORUZA

Other 10.20.* ranges are described in [bsc-networks/mesh](https://github.com/bsc-networks/mesh), so please don't assign anything to those.

Kingman APs are temporary configured to the 10.20.35.220/30 IP range until Kingman gets its own router.

We use Dlink Smart Console Utility to manage IP allocations of switches. Switches have web interface to manage their ports. The default gateway port is port 1 and DHCP traffic is only allowed through that port. To change this, edit the security settings in the switch's web configuration by going to security -> dhcp screening.

Old (not in used by stored in storage, we keep this information to know how to connect to a device if we will want to reuse it):

 * [192.168.0.42](http://192.168.0.42) - C2K, a0:f3:c1:ff:2a:94, TP-Link, channel 11
 * [192.168.0.43](http://192.168.0.43) - FamilyRoom, a0:f3:c1:ff:14:70,  TP-Link, channel 11
 * [192.168.0.59](http://192.168.0.59) - QuietStudyRoom, c0:4a:00:40:e4:4d, TP-Link, channel 11
