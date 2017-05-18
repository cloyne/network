# Cloyne network

## Internet uplink

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

## HE router

    External IP:       64.62.133.41
    Netmask:           255.255.255.248 (/29)
    Hostname:          he.cloyne.org
    Other IP:          64.62.214.118

It is a [Mikrotik RouterBoard 2011UiAS-RM](http://routerboard.com/RB2011UiAS-RM).

## Main router

    External IP:       64.62.133.42
    Internal IP:       10.20.32.1
    Netmask:           255.255.255.248 (/29)
    Hostname:          router.cloyne.org
    DHCP client range: 10.20.32.100 - 10.20.35.190 (859 addresses)

It is a [Mikrotik RouterBoard 450G](http://routerboard.com/RB450G).

## Servers

### server1 ###

    External IP: 64.62.133.43 (eth0)
    Hostname:    server1.cloyne.org
    Login:       username cloyne + sudo su for root 

Running Ubuntu LTS distribution as a host for Docker images. Services:
 * Secondary DNS server (using [cloyne/powerdns-slave](https://github.com/cloyne/docker-powerdns-slave) Docker image)

Partitions:
 * root: `/dev/disk/by-uuid/5d604660-e02f-41e8-8f39-877a38f32f67`

### server2 ###

    External IP: 64.62.133.44 (eth0)
    Hostname:    server2.cloyne.org
    Internal IP: 10.20.32.10 (eth1)
    Login:       username cloyne + sudo su for root 

Running Ubuntu LTS distribution as a host for Docker images. Services:
 * Primary DNS server (using [cloyne/powerdns-master](https://github.com/cloyne/docker-powerdns-master) Docker image)
 * Mail server (Postfix) (using [cloyne/postfix](https://github.com/cloyne/postfix) Docker image)
 * MySQL (using [tozd/mysql](https://github.com/tozd/mysql) Docker image)
 * PostgreSQL (using [tozd/postgresql](https://github.com/tozd/postgresql) Docker image)
 * Nginx reverse proxy (using [cloyne/web](https://github.com/cloyne/web) Docker image)
 * [phpMyAdmin](https://cloyne.org/phpmyadmin/) (using [tozd/phpmyadmin](https://github.com/tozd/phpmyadmin) Docker image)
 * [phpPgAdmin](https://cloyne.org/phppgadmin/) (using [tozd/phppgadmin](https://github.com/tozd/phppgadmin) Docker image)
 * [Cloyne.org](https://cloyne.org) blog (Wordpress) (using [cloyne/blog](https://github.com/cloyne/blog) Docker image)
 * local [iperf server](https://iperf.fr/) (using [tozd/iperf](https://github.com/tozd/iperf) Docker image)

Partitions:
 * root: `/dev/sdg1`
 * `/srv`: `/dev/md1`
 * `/srv/mnt`: `/dev/md0` (used for daily local backup of files and databases, using [tozd/rdiff-backup](https://github.com/tozd/docker-rdiff-backup) Docker image)

```
$ cat /proc/mdstat

md0 : active raid1 sdd1[1] sde1[0]
      488253248 blocks super 1.2 [2/2] [UU]
      
md1 : active raid1 sdb1[1] sda1[2]
      1465006080 blocks super 1.2 [2/2] [UU]
      bitmap: 9/11 pages [36KB], 65536KB chunk
```

### server3 ###

    External IP: 64.62.133.45 (p1p1)
    Hostname:    server3.cloyne.org
    Internal IP: 10.20.32.11 (p1p2)
    Internal IP: 172.16.0.103 (p1p3)
    Login:       username cloyne + sudo su for root 

Running Ubuntu LTS distribution as a host for Docker images. It contains 8 x 3 TB hard drives, 6 x 750 GB drives, configured in pairs into RAID-1, combined into a 13 TB LVM volume. Services:
 * [ownCloud](https://owncloud.org/) (using [cloyne/owncloud](https://github.com/cloyne/owncloud) Docker image)
 * local [iperf server](https://iperf.fr/) (using [tozd/iperf](https://github.com/tozd/iperf) Docker image)
 * [nodewatcher](http://nodewatcher.net/) (TODO)

One hard drive bay (8) is currently empty because of a failed hard drive. Its mirror (`/dev/sdg1`, bay 5, 750 GB) can be used as a replacement for some other drive when needed.

Partitions:
 * root: `/dev/sda1`
 * `/srv`: `/dev/mapper/vg0-srv`

```
$ cat /proc/mdstat
md5 : active raid1 sdk1[3] sdj1[2]
      732277568 blocks super 1.2 [2/2] [UU]
md7 : active raid1 sdp1[1] sdo1[0]
      732277568 blocks super 1.2 [2/2] [UU
md6 : active raid1 sdn1[1] sdm1[0]
      732277568 blocks super 1.2 [2/2] [UU]
md2 : active raid1 sdh1[1] sdf1[2]
      2929542976 blocks super 1.2 [2/2] [UU]
md3 : active raid1 sdl1[1] sdi1[0]
      2929542976 blocks super 1.2 [2/2] [UU]
md0 : active raid1 sdb1[3] sdc1[2]
      2929542976 blocks super 1.2 [2/2] [UU]
md1 : active raid1 sde1[2] sdd1[3]
      2929542976 blocks super 1.2 [2/2] [UU]
```

```
$ lvdisplay --maps
  --- Logical volume ---
  LV Path                /dev/vg0/srv
  LV Name                srv
  VG Name                vg0
  LV UUID                UvYIg3-QMId-m19Y-BeQ5-DtQV-QSPK-znMAFt
  LV Write Access        read/write
  LV Creation host, time server3, 2015-05-16 23:15:51 -0700
  LV Status              available
  # open                 1
  LV Size                12.86 TiB
  Current LE             3371192
  Segments               7
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
    Physical volume	/dev/md7
    Physical extents	0 to 178777
   
  Logical extent 3039658 to 3218435:
    Type		linear
    Physical volume	/dev/md5
    Physical extents	0 to 178777
   
  Logical extent 3218436 to 3371191:
    Type		linear
    Physical volume	/dev/md6
    Physical extents	0 to 152755
```

```
$ pvs -o+pv_used
  PV         VG   Fmt  Attr PSize   PFree   Used   
  /dev/md0   vg0  lvm2 a--    2.73t      0    2.73t
  /dev/md1   vg0  lvm2 a--    2.73t      0    2.73t
  /dev/md2   vg0  lvm2 a--    2.73t      0    2.73t
  /dev/md3   vg0  lvm2 a--    2.73t      0    2.73t
  /dev/md5   vg0  lvm2 a--  698.35g      0  698.35g
  /dev/md6   vg0  lvm2 a--  698.35g 101.65g 596.70g
  /dev/md7   vg0  lvm2 a--  698.35g      0  698.35g
```

```
$ ~/files/tw_cli/tw_cli /c2 show
Unit  UnitType  Status         %RCmpl  %V/I/M  Stripe  Size(GB)  Cache  AVrfy
------------------------------------------------------------------------------
u0    SINGLE    VERIFYING      -       75%     -       2793.96   Ri     ON     
u1    SINGLE    VERIFYING      -       75%     -       2793.96   Ri     ON     
u2    SINGLE    VERIFYING      -       30%     -       2793.96   Ri     ON     
u3    SINGLE    VERIFYING      -       0%      -       2793.96   Ri     ON     
u4    SINGLE    VERIFY-PAUSED  -       0%      -       2793.96   Ri     ON     
u5    SINGLE    VERIFY-PAUSED  -       0%      -       698.481   Ri     ON     
u6    SINGLE    VERIFY-PAUSED  -       0%      -       2793.96   Ri     ON     
u7    SINGLE    VERIFY-PAUSED  -       0%      -       2793.96   Ri     ON     
u8    SINGLE    VERIFY-PAUSED  -       0%      -       698.481   Ri     ON     
u9    SINGLE    VERIFY-PAUSED  -       0%      -       698.481   Ri     ON     
u10   SINGLE    VERIFY-PAUSED  -       0%      -       2793.96   Ri     ON     
u11   SINGLE    VERIFY-PAUSED  -       0%      -       698.481   Ri     ON     
u12   SINGLE    VERIFY-PAUSED  -       0%      -       698.481   Ri     ON     
u13   SINGLE    VERIFY-PAUSED  -       0%      -       698.481   Ri     ON     
u14   SINGLE    VERIFY-PAUSED  -       0%      -       698.481   Ri     ON     

VPort Status         Unit Size      Type  Phy Encl-Slot    Model
------------------------------------------------------------------------------
p0    VERIFYING      u0   2.73 TB   SATA  0   -            WDC WD30EFRX-68EUZN0
p1    VERIFYING      u1   2.73 TB   SATA  1   -            WDC WD30EFRX-68EUZN0
p2    VERIFYING      u2   2.73 TB   SATA  2   -            WDC WD30EFRX-68EUZN0
p3    VERIFYING      u3   2.73 TB   SATA  3   -            WDC WD30EFRX-68EUZN0
p4    VERIFYING      u4   2.73 TB   SATA  4   -            WDC WD30EFRX-68EUZN0
p5    VERIFYING      u5   698.63 GB SATA  5   -            ST3750640NS         
p6    VERIFYING      u6   2.73 TB   SATA  6   -            WDC WD30EFRX-68EUZN0
p7    VERIFYING      u7   2.73 TB   SATA  7   -            WDC WD30EFRX-68EUZN0
p9    VERIFYING      u8   698.63 GB SATA  9   -            ST3750640NS         
p10   VERIFYING      u9   698.63 GB SATA  10  -            ST3750640NS         
p11   VERIFYING      u10  2.73 TB   SATA  11  -            WDC WD30EFRX-68EUZN0
p12   VERIFYING      u11  698.63 GB SATA  12  -            ST3750640NS         
p13   VERIFYING      u12  698.63 GB SATA  13  -            ST3750640NS         
p14   VERIFYING      u13  698.63 GB SATA  14  -            ST3750640NS         
p15   VERIFYING      u14  698.63 GB SATA  15  -            ST3750640NS         

Name  OnlineState  BBUReady  Status    Volt     Temp     Hours  LastCapTest
---------------------------------------------------------------------------
bbu   On           Yes       OK        OK       OK       0      xx-xxx-xxxx  
```

`VPort` tells you which hard drive bay a disk is in. `Unit` tells you under which SCSI number it is available in the system.
Using that you can see under which device filename you can a hard drive. For example, drive in bay 11 is unit 10, so greping `dmesg | grep 'sd 2:0:10:0'` gives you `sd 2:0:10:0: [sdl] 5859352576 512-byte logical blocks: (3.00 TB/2.73 TiB)`, so `/dev/sdl` is the device filename under which the drive is available. **VPort and Unit can get out of sync and order.** You can try to reorder them and get them in sync by moving them around in hardware RAID BIOS, but it takes a lot of time because the interface is bugy and you hve to move them around one by one, repeating many times, until changes stick correctly.

On the other hand, `smartctl` operates on `VPort` numbers. So for the drive in bay 11, you can access its SMART information using `smartctl -a -d 3ware,11 /dev/twa0`.

## Printers

### printer1 (Brother MFC-9330CDW) ###

    Internal IP:  10.20.32.90
    Hostname:     printer1.cloyne.org
    Location:     Pool/Mail room
    Wired MAC:    30:05:5C:A8:CD:68
    Wireless MAC: 44-1c-a8-38-ea-2b

### label printer (Brother QL-710W) ###

    Internal IP: 10.20.32.91
    MAC:         00:80:92:CF:09:B1

### Makerspace printer (Canon MX870) ###

    Internal IP: 10.20.32.92
    Hostname:    printer2.cloyne.org
    Location:    W0B (Makerspace)
    MAC:         00:1E:8F:98:3B:1E

## APs

 * [10.20.32.40](http://10.20.32.40) - FamilyRoom, 04:18:d6:20:60:44, Ubiquiti UniFi AP Pro, channel 6, 48
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

### Kingman

Temporary configured to this IP range until Kingman gets its own router.

 * 10.20.35.220 - Study Room,      80:2a:a8:13:4b:ed, Ubiquiti UniFi AP-AC-Pro, channel 11, 44
 * 10.20.35.221 - Network Closet,  80:2a:a8:13:4a:19, Ubiquiti UniFi AP-AC-Pro, channel 1, 149
 * 10.20.35.222 - Dining Room,     80:2a:a8:13:4b:bb, Ubiquiti UniFi AP-AC-Pro, channel 1, 36
 * 10.20.35.223 - 2nd Floor North, 80:2a:a8:13:4b:c5, Ubiquiti UniFi AP-AC-Pro, channel 6, 161

### Other

Old (not in used by stored in storage, we keep this information to know how to connect to a device if we will want to reuse it):

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
 * [10.20.35.212](http://10.20.35.212) – Kingman-Cloyne, 24:A4:3C:BE:4E:A0 (temporary moved from 10.20.99.210 until Kingman gets its own router)
 * [10.20.35.240](http://10.20.35.240) – Cloyne-Euclid KORUZA, B8:27:EB:7A:6A:BB
 * [10.20.35.241](http://10.20.35.241) – Euclid-Cloyne KORUZA, B8:27:EB:23:21:E7
