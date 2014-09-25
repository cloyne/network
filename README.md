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

### printer1 ###

    Internal IP: 192.168.0.100
    Hostname:    printer1.cloyne.net

## APs

 * 192.168.0.41 - MailRoom, 1c:df:f:94:95:5a, cisco
 * 192.168.0.42 - C2K, 68:7f:74:c:f7:7f, dd-wrt
 * 192.168.0.43 - FamilyRoom, 68:7f:74:c:f7:c4, dd-wrt
 * 192.168.0.45 - E2J, 1c:df:f:94:93:47, cisco
 * 192.168.0.46 - E3J, c4:71:fe:34:27:4c, cisco
 * 192.168.0.47 - W12, c4:71:fe:34:28:55, cisco
 * 192.168.0.51 - GreatHall, fc:99:47:44:43:98, cisco
 * 192.168.0.52 - E2D, fc:99:47:94:71:19, cisco
 * 192.168.0.53 - W2H, fc:99:47:44:25:cb, cisco, channel 11
 * 192.168.0.54 - C2P, fc:99:47:44:43:19, cisco
 * 192.168.0.55 - C2C, fc:99:47:2d:8:a4, cisco
 * 192.168.0.57 - W2C, 74:ea:3a:a2:cf:ce, openwrt
 * 192.168.0.58 - C3K, a0:f3:c1:ff:2a:94, openwrt
 * 192.168.0.59 - test, c0:4a:00:40:e4:4c, official

## Switches

 * 192.168.0.21 - 14:d6:4d:1e:4:16
 * 192.168.0.23 - fc:75:16:68:bb:c9

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
