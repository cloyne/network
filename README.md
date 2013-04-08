# cloyne network documentation

## fiber internet

IP Space:
50.0.115.224/28
   Network:     50.0.115.224 (838890464)
   Netmask:     255.255.255.240
   Gateway:     50.0.115.225
   Broadcast:   50.0.115.239 (838890479)
   Primary DNS: 208.201.224.11
   Second. DNS: 208.201.224.33
   Usable address range:  50.0.115.226 - 50.0.115.238 (13 addresses)

## router

RouterBoard 450G @ 192.168.0.1 / buccaneer
see router.config

## switches

192.168.0.20 main switch
192.168.0.21 C1 switch
192.168.0.22 C2 switch
192.168.0.23 C3 switch
192.168.0.25 E2 switch
192.168.0.26 E3 switch
192.168.0.27 W1 switch
192.168.0.28 W2 switch
192.168.0.29 W3 switch

## waps

192.168.0.41 C1 wap
192.168.0.42 C2 wap
192.168.0.43 C3 wap
192.168.0.45 E2 wap
192.168.0.46 E3 wap
192.168.0.47 W1 wap
192.168.0.48 W2 wap
192.168.0.49 W3 wap

## servers

### swashbuckler @ 192.168.0.10

Debian.
puppet master - http://docs.puppetlabs.com/guides/setting_up.html
nm user 
dns - https://github.com/lermit/puppet-bind
ntp -
monitoring -

### landlubber @ 192.168.0.15

CentOS.
nm user 
ftp -
samba -
nfs -

### unnamed

Debian.
nm user 
nfs mount - 
deluge -


### kiosks

Ubuntu.
clone user
nfs mount -
