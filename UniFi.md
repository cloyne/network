Flashing UniFi with OpenWrt
---------------------------

Flash OpenWrt image on the UniFi.

Login with telnet, set the password. Login with SSH.

In `/etc/config/system` configure the hostname.

Disable DHCP:

```
uci set dhcp.lan.ignore=1
uci set dhcp.lan.dhcpv6=disabled
uci set dhcp.lan.ra=disabled
uci commit dhcp

/etc/init.d/dnsmasq disable
```

Disable firewall:

```
/etc/init.d/firewall disable
```

Configure `/etc/config/network`:

```
config interface 'lan'
	option ifname 'eth0'
	option force_link '1'
	option type 'bridge'
	option proto 'static'
	option ipaddr '192.168.0.XXX'
	option netmask '255.255.0.0'
	option ip6assign '60'
```

In `/etc/config/wireless` configure:

```
config wifi-device  radio0
	option type     mac80211
	option channel  36
	option hwmode	11a
	option path	'platform/ar934x_wmac'
	option htmode	HT20
	option require_mode n
	option txpower 17
	#option basic_rate '6000'

config wifi-iface
	option device   radio0
	option network  lan
	option mode     ap
	option ssid     Cloyne
	option encryption 'psk2'
	option key	'XXX'

config wifi-device  radio1
	option type     mac80211
	option channel  11
	option hwmode	11g
	option path	'pci0000:00/0000:00:00.0'
	option htmode	HT20
	option require_mode n
	option txpower 17
	#option basic_rate '6000'

config wifi-iface
	option device   radio1
	option network  lan
	option mode     ap
	option ssid     Cloyne
	option encryption 'psk2'
	option key	'XXX'
```

Create `/etc/hotplug.d/iface/30-bitrates`:

```
#!/bin/sh

. /lib/functions.sh
. /lib/functions/network.sh

# Disable legacy 2.4GHz low bitrates
if [ ifup = "$ACTION" ]; then
    case "$DEVICE" in
        wlan*)
            logger setting bitrate for device "$DEVICE" on interface "$INTERFACE"
            iw "$DEVICE" set bitrates legacy-2.4 6 9 12 18 24 36 48 54 ht-mcs-2.4 lgi-2.4
        ;;
        br-*)
            # Bridged interface, check if any wifi interface is member
            for i in $(ls /sys/class/net/$DEVICE/brif); do
                case "$i" in
                    wlan*)
                        logger setting bitrate for device "$i" on interface "$INTERFACE"
                        iw "$i" set bitrates legacy-2.4 6 9 12 18 24 36 48 54 ht-mcs-2.4 lgi-2.4
                    ;;
                esac
            done
        ;;
    esac
fi
```
