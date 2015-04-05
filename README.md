# Cloyne network

## Fiber Internet

Through [Sonic.net](http://sonic.net/), fiber itself is operated by AT&T.

    50.0.115.224/28
    Network:     50.0.115.224 (838890464)
    Netmask:     255.255.255.240
    Gateway:     50.0.115.225
    Broadcast:   50.0.115.239 (838890479)
    Primary DNS: 208.201.224.11
    Second. DNS: 208.201.224.33
    Time:        64.142.1.20
    Bandwidth:   50/50 Mbit/s
    Usable address range:  50.0.115.226 - 50.0.115.238 (13 addresses)

Sonic.net network operations phone number is +1-877-706-662. Equipment directly connected to the fiber has to have configured fixed 100 Mbit/s full-duplex configuration and autonegotiation must be disabled.

## Main router

    External IP: 50.0.115.226
    Internal IP: 192.168.0.1
    Hostname:    router.cloyne.net

It is a [Mikrotik RouterBoard 450G](http://routerboard.com/RB450G). See `router` directory for more information.

## Servers

### server1 ###

    External IP: 50.0.115.227
    Hostname:    server1.cloyne.net

Running Debian Linux distribution as a host for Docker images. Services:
 * Secondary DNS server

### server2 ###

    External IP: 50.0.115.228
    Hostname:    server2.cloyne.net

Running Debian Linux distribution as a host for Docker images. Services:
 * Primary DNS server
 * Mail server (Postfix)
 * MySQL
 * PostgreSQL
 * Nginx reverse proxy
 * [phpMyAdmin](http://cloyne.net/phpmyadmin/)
 * [phpPgAdmin](http://cloyne.net/phppgadmin/)
 * [Cloyne.org](http://cloyne.org) blog (Wordpress)

## Printers

### printer1 (HP LaserJet 500 MFP M525) ###

    Internal IP: 192.168.0.100
    Hostname:    printer1.cloyne.net
    Location:    Library
    MAC:         28:80:23:11:83:3C

### label printer (Brother QL-710W) ###

    Internal IP: 192.168.0.101
    MAC:         00:80:92:CF:09:B1

## APs

 * [192.168.0.41](http://192.168.0.41) - FamilyRoom, 04:18:d6:20:60:44, UniFi AP-Pro, channel 1
 * [192.168.0.44](http://192.168.0.44) - W3J, e8:94:f6:68:87:51, TP-Link, channel 6
 * [192.168.0.45](http://192.168.0.45) - E2J, 04:18:d6:20:58:df, UniFi AP-Pro, channel 11
 * [192.168.0.47](http://192.168.0.47) - W2C, 04:18:d6:20:5c:fe, UniFi AP-Pro, channel 1
 * [192.168.0.48](http://192.168.0.48) - W3A, c0:4a:00:5d:c3:f3, TP-Link, channel 11
 * [192.168.0.49](http://192.168.0.49) - Hackerspace, c0:4a:00:40:e3:61, TP-Link, channel 11
 * [192.168.0.50](http://192.168.0.50) - E3StudyRoom, e8:94:f6:68:84:78, TP-Link, channel 1
 * [192.168.0.51](http://192.168.0.51) - GreatHall, 04:18:d6:20:59:c8, UniFi AP-Pro, channel 6
 * [192.168.0.52](http://192.168.0.52) - E2D, 04:18:d6:20:5a:1f, UniFi AP-Pro, channel 1
 * [192.168.0.53](http://192.168.0.53) - W2H, 04:18:d6:20:59:c7, UniFi AP-Pro, channel 11
 * [192.168.0.54](http://192.168.0.54) - C2P, 04:18:d6:20:58:e4, UniFi AP-Pro, channel 6
 * [192.168.0.55](http://192.168.0.55) - C2C, 04:18:d6:20:5f:e6, UniFi AP-Pro, channel 6
 * [192.168.0.57](http://192.168.0.57) - W1E, 90:f6:52:ea:05:ec, TP-Link, channel 6
 * [192.168.0.58](http://192.168.0.58) - C3K, 90:F6:52:2A:08:54, TP-Link, channel 1

Temporary:

 * [192.168.0.42](http://192.168.0.42) - C2K, a0:f3:c1:ff:2a:94, TP-Link, channel 11
 * [192.168.0.43](http://192.168.0.43) - FamilyRoom, a0:f3:c1:ff:14:70,  TP-Link, channel 11
 * [192.168.0.46](http://192.168.0.46) - E3J, 04:18:d6:20:5d:20, UniFi AP-Pro, channel 6
 * [192.168.0.59](http://192.168.0.59) - QuietStudyRoom, c0:4a:00:40:e4:4d, TP-Link, channel 11

## Switches
 * [192.168.0.20](http://192.168.0.20) - Network Room 2 - fc:75:16:68:b4:49
 * [192.168.0.21](http://192.168.0.21) - C2 - 14:d6:4d:1e:4:16
 * [192.168.0.22](http://192.168.0.22) - E2 - fc:75:16:68:bb:f9
 * [192.168.0.23](http://192.168.0.23) - C3 - fc:75:16:68:bb:c9
 * [192.168.0.24](http://192.168.0.24) - E3 - fc:75:16:68:b4:19
 * [192.168.0.25](http://192.168.0.25) - Mail Room - 14:d6:4d:1e:03:e6
 * [192.168.0.26](http://192.168.0.26) - W2 - fc:75:16:68:b4:a9
 * [192.168.0.27](http://192.168.0.27) - Network Room 1 - fc:75:16:68:bb:99
 * [192.168.0.28](http://192.168.0.28) - W3 - fc:75:16:68:b4:79
 

# Possibly old information

## network mapping in progress

see `network` directory and `network.csv`

## waps

see `waps` directory

## switches

## servers

### kiosks

Ubuntu.
- 'clone' user
- TODO: nfs mount
