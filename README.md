# Cloyne network

## Fiber Internet

Through [Sonic.net](http://sonic.net/), fiber itself is operated by AT&T.

    50.0.115.224/28
    Network:              50.0.115.224 (838890464)
    Netmask:              255.255.255.240
    Gateway:              50.0.115.225
    Broadcast:            50.0.115.239 (838890479)
    Primary DNS:          208.201.224.11
    Second. DNS:          208.201.224.33
    Time:                 64.142.1.20
    Bandwidth:            50/50 Mbit/s
    Usable address range: 50.0.115.226 - 50.0.115.238 (13 addresses)

Sonic.net network operations phone number is +1-877-706-662. Equipment directly connected to the fiber has to have configured fixed 100 Mbit/s full-duplex configuration and autonegotiation must be disabled.

## Main router

    External IP:       50.0.115.226
    Internal IP:       10.20.32.1
    Netmask:           255.255.252.0 (/22)
    Hostname:          router.cloyne.net
    DHCP client range: 10.20.32.100 - 10.20.35.190 (859 addresses)

It is a [Mikrotik RouterBoard 450G](http://routerboard.com/RB450G). See `router` directory for more information.

## Servers

### server1 ###

    External IP: 50.0.115.227 (eth0)
    Hostname:    server1.cloyne.net
    Login:       username root

Running Debian Linux distribution as a host for Docker images. Services:
 * Secondary DNS server

Partitions:
 * root: `/dev/disk/by-uuid/5d604660-e02f-41e8-8f39-877a38f32f67`

### server2 ###

    External IP: 50.0.115.228 (eth0)
    Hostname:    server2.cloyne.net
    Internal IP: 10.20.32.10 (eth1)
    Login:       username root

Running Debian Linux distribution as a host for Docker images. Services:
 * Primary DNS server
 * Mail server (Postfix)
 * MySQL
 * PostgreSQL
 * Nginx reverse proxy
 * [phpMyAdmin](http://cloyne.net/phpmyadmin/)
 * [phpPgAdmin](http://cloyne.net/phppgadmin/)
 * [Cloyne.org](http://cloyne.org) blog (Wordpress)

Partitions:
 * root: `/dev/sdg1`
 * `/srv`: `/dev/md1`
 * `/srv/var`: `/dev/md0`

```
$ cat /proc/mdstat

md0 : active raid1 sde1[1] sdf1[0]
      488253248 blocks super 1.2 [2/2] [UU]
md1 : active raid10 sdb1[3] sdd1[4] sdc1[2] sda1[0]
      2930011136 blocks super 1.2 512K chunks 2 near-copies [4/4] [UUUU]
```

### server3 ###

    External IP: 50.0.115.229 (p5p1)
    Hostname:    server3.cloyne.net
    Internal IP: 10.20.32.11 (p6p1)
    Login:       username cloyne + sudo su for root 

Running Ubuntu Server Linux distribution as a host for Docker images. It contains 8 x 3 TB hard drives, 8 x 750 GB drives, configured in pairs into RAID-1, combined into a 15 TB LVM volume. Services:
 * ownCloud

Partitions:
 * root: `/dev/sda1`
 * `/srv`: `/dev/mapper/vg0-srv`

```
$ cat /proc/mdstat

md3 : active raid1 sdm1[1] sdi1[0]
      2929542976 blocks super 1.2 [2/2] [UU]
md1 : active raid1 sdd1[0] sde1[1]
      2929542976 blocks super 1.2 [2/2] [UU]
md7 : active raid1 sdq1[1] sdp1[0]
      732277568 blocks super 1.2 [2/2] [UU]
md0 : active raid1 sdc1[1] sdb1[0]
      2929542976 blocks super 1.2 [2/2] [UU]
md2 : active raid1 sdh1[1] sdf1[0]
      2929542976 blocks super 1.2 [2/2] [UU]
md4 : active raid1 sdj1[1] sdg1[0]
      732277568 blocks super 1.2 [2/2] [UU]
md6 : active raid1 sdn1[0] sdo1[1]
      732277568 blocks super 1.2 [2/2] [UU]
md5 : active raid1 sdk1[0] sdl1[1]
      732277568 blocks super 1.2 [2/2] [UU]
```

```
$ lvdisplay --maps

  LV Path                /dev/vg0/srv
  LV Name                srv
  VG Name                vg0
  LV UUID                UvYIg3-QMId-m19Y-BeQ5-DtQV-QSPK-znMAFt
  LV Write Access        read/write
  LV Creation host, time server3, 2015-05-16 23:15:51 -0700
  LV Status              available
  # open                 1
  LV Size                13.64 TiB
  Current LE             3575992
  Segments               8
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     256
  Block device           252:0
   
  --- Segments ---
  Logical extent 0 to 715219:
    Type		linear
    Physical volume	/dev/md0
    Physical extents	0 to 715219
   
  Logical extent 715220 to 1430439:
    Type		linear
    Physical volume	/dev/md1
    Physical extents	0 to 715219
   
  Logical extent 1430440 to 2145659:
    Type		linear
    Physical volume	/dev/md2
    Physical extents	0 to 715219
   
  Logical extent 2145660 to 2860879:
    Type		linear
    Physical volume	/dev/md3
    Physical extents	0 to 715219
   
  Logical extent 2860880 to 3039657:
    Type		linear
    Physical volume	/dev/md4
    Physical extents	0 to 178777
   
  Logical extent 3039658 to 3218435:
    Type		linear
    Physical volume	/dev/md5
    Physical extents	0 to 178777
   
  Logical extent 3218436 to 3397213:
    Type		linear
    Physical volume	/dev/md6
    Physical extents	0 to 178777
   
  Logical extent 3397214 to 3575991:
    Type		linear
    Physical volume	/dev/md7
    Physical extents	0 to 178777
```

## Computers

### Maintanance room ###

    Internal IP: 10.20.32.80
    Hostname:    maintenance.cloyne.net
    MAC:         64:31:50:25:B1:84

## Printers

### printer1 (HP LaserJet 500 MFP M525) ###

    Internal IP: 10.20.32.90
    Hostname:    printer1.cloyne.net
    Location:    Pool/Mail room
    MAC:         28:80:23:11:83:3C

### label printer (Brother QL-710W) ###

    Internal IP: 10.20.32.91
    MAC:         00:80:92:CF:09:B1

### Makerspace printer (Canon MX870) ###

    Internal IP: 10.20.32.92
    Location:    W0B (Makerspace)
    MAC:         00:1E:8F:98:3B:1E

## APs

 * [10.20.32.40](http://10.20.32.40) - FamilyRoom, 04:18:d6:20:60:44, Ubiquiti UniFi AP Pro, channel 6, 140
 * [10.20.32.41](http://10.20.32.41) - W3J, e8:94:f6:68:87:51, TP-LINK TL-WR1043ND v2, channel 11
 * [10.20.32.42](http://10.20.32.42) - E2J, 04:18:d6:20:58:df, Ubiquiti UniFi AP Pro, channel 6, 132
 * [10.20.32.43](http://10.20.32.43) - W2C, 04:18:d6:20:5c:fe, Ubiquiti UniFi AP Pro, channel 6, 124
 * [10.20.32.44](http://10.20.32.44) - W3A, c0:4a:00:5d:c3:f3, TP-LINK TL-WR1043ND v2, channel 1
 * [10.20.32.45](http://10.20.32.45) - W0B, c0:4a:00:40:e3:61, TP-LINK TL-WR1043ND v2, channel 1
 * [10.20.32.46](http://10.20.32.46) - E3AB, e8:94:f6:68:84:78, TP-LINK TL-WR1043ND v2, channel 1
 * [10.20.32.47](http://10.20.32.47) - GreatHall, 04:18:d6:20:59:c8, Ubiquiti UniFi AP Pro, channel 1, 116
 * [10.20.32.48](http://10.20.32.48) - E2D, 04:18:d6:20:5a:1f, Ubiquiti UniFi AP Pro, channel 11, 108
 * [10.20.32.49](http://10.20.32.49) - W2H, 04:18:d6:20:59:c7, Ubiquiti UniFi AP Pro, channel 1, 100
 * [10.20.32.50](http://10.20.32.50) - C2P, 04:18:d6:20:58:e4, Ubiquiti UniFi AP Pro, channel 11, 64
 * [10.20.32.51](http://10.20.32.51) - C2C, 04:18:d6:20:5f:e6, Ubiquiti UniFi AP Pro, channel 1, 56
 * [10.20.32.52](http://10.20.32.52) - W1E, 90:f6:52:ea:05:ec, TP-LINK TL-WR1043ND, channel 11
 * [10.20.32.53](http://10.20.32.53) - C3K, 90:F6:52:2A:08:54, TP-LINK TL-WR1043ND, channel 6

Old:

 * [192.168.0.42](http://192.168.0.42) - C2K, a0:f3:c1:ff:2a:94, TP-Link, channel 11
 * [192.168.0.43](http://192.168.0.43) - FamilyRoom, a0:f3:c1:ff:14:70,  TP-Link, channel 11
 * [192.168.0.46](http://192.168.0.46) - E3J, 04:18:d6:20:5d:20, Ubiquiti UniFi AP Pro, channel 6
 * [192.168.0.59](http://192.168.0.59) - QuietStudyRoom, c0:4a:00:40:e4:4d, TP-Link, channel 11

## Switches

 * [10.20.32.20](http://10.20.32.20) - Network Room 2, fc:75:16:68:b4:49
 * [10.20.32.21](http://10.20.32.21) - C2K, 14:d6:4d:1e:4:16
 * [10.20.32.22](http://10.20.32.22) - E2SC, fc:75:16:68:bb:f9
 * [10.20.32.23](http://10.20.32.23) - C3L, fc:75:16:68:bb:c9
 * [10.20.32.24](http://10.20.32.24) - E3SB, fc:75:16:68:b4:19
 * [10.20.32.25](http://10.20.32.25) - Mail Room, 14:d6:4d:1e:03:e6
 * [10.20.32.26](http://10.20.32.26) - W2SB, fc:75:16:68:b4:a9
 * [10.20.32.27](http://10.20.32.27) - Network Room 1, fc:75:16:68:bb:99
 * [10.20.32.28](http://10.20.32.28) - W3SB, fc:75:16:68:b4:79

We use Dlink Smart Console Utility to manage IP allocations of switches. Switches have web interface to manage their ports. The default gateway port is port 1 and DHCP traffic is only allowed through that port. To change this, edit the security settings in the switch's web configuration by going to security -> dhcp screening. 

## Mesh

 * [10.20.35.210](http://10.20.35.210) – Cloyne-Kingman, 24:A4:3C:9C:F6:AD
 * [10.20.35.211](http://10.20.35.211) – Cloyne-Euclid, 04:18:D6:A4:84:77
