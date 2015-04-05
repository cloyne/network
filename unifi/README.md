Flashing UniFi with OpenWrt
---------------------------

[Flash OpenWrt image on the UniFi](http://wiki.openwrt.org/toh/ubiquiti/uappro#installing_a_new_firmware_image):
* Configure your machine to an IP address in the range used by the AP. By default the AP uses `192.168.1.20`.
* `scp openwrt-ar71xx-generic-ubnt-uap-pro-squashfs-factory.bin admin@192.168.1.XXX:/tmp/`
* `ssh -l admin 192.168.1.XXX`
* `fwupdate.real -m openwrt-ar71xx-generic-ubnt-uap-pro-squashfs-factory.bin -d`

It reboots into OpenWrt which uses `192.168.1.1` as its initial IP address. Configure your machine to be in that range. Login with telnet:

```
telnet 192.168.1.1
```

Configure root password with `passwd`. Now disconnect from telnet and connect with SSH to `192.168.1.1` with username `root`.

In `/etc/config/system` configure the hostname.

Disable DHCP by running:

```
uci set dhcp.lan.ignore=1
uci set dhcp.lan.dhcpv6=disabled
uci set dhcp.lan.ra=disabled
uci commit dhcp

/etc/init.d/dnsmasq disable
```

Disable firewall by running:

```
/etc/init.d/firewall disable
```

Configure the LAN section in `/etc/config/network`:

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

Set `ipaddr` to the real IP address of the device.

Set `/etc/config/wireless` file to (check if file originally looks simlarly, like `path`s should be the same) by doing:

```
cat > /etc/config/wireless
```

And copy & paste in (finish with ctrl-d):

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

Edit the `/etc/config/wireless` and set the WiFi password.

Create `/etc/hotplug.d/iface/30-bitrates` by doing:

```
cat > /etc/hotplug.d/iface/30-bitrates
```

And copy & paste in (finish with ctrl-d):

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

Run:

```
chmod +x /etc/hotplug.d/iface/30-bitrates
```

And reboot:

```
reboot
```
