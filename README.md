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
    Hostname: server1.cloyne.net

Running Debian Linux distribution as a host for Docker images. Services:
 * Secondary DNS server

### server2 ###

    External IP: 50.0.115.228
    Hostname: server2.cloyne.net

Running Debian Linux distribution as a host for Docker images. Services:
 * Primary DNS server
 * Mail server (Postfix)
 * MySQL
 * PostgreSQL
 * Nginx reverse proxy
 * phpMyAdmin
 * phpPgAdmin
 * Cloyne.org blog (Wordpress)

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
