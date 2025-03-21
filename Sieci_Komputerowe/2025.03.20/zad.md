## Jako odpowiedzi na poniższe pytania podaj polecenia, które wywołałeś oraz wartość jeżeli jest o nią pytanie:

1. Adres MAC routera, który łączy sieć pracowni z internetem.
2. Ping wszystkich urządzeń jednocześnie w podsieci 10.123.0.0/23.
3. Przeskanuj porty, które są otwarte na interfejsie `lo` (loopback).
4. Adres serwera DNS, który jest ustawiony w systemie.
5. Zmień adres MAC karty sieciowej na 00:11:22:33:44:55.
6. Podaj rekord DNS dla poczty e-mail adresu kosmatka.pl używając serwer DNS 8.8.8.8 (bez edycji globalnych ustawień serwerów DNS).
7. Podaj adres IPv6 adresu google.pl.
8. Podaj kiedy została zarejestrowana domena kosmatka.pl i do kiedy jest opłacona (gdzie można znaleźć listę domen, które wygasły dzisiejszego dnia?).
9. Wypisz porty, które są otwarte w systemie wraz z numerem PID i nazwą programu.
10. Przez jakie routery przechodzą pakiety, które trafiają do serwera pw.plock.pl?

**Polecenia:** arp, ip, netstat, nmap, ping, traceroute, dig, whois, nslookup

&nbsp;

# Rozwiązanie

1. arp -a
```
_gateway (192.168.48.1) at e0:23:ff:ce:f7:0f [ether] on enp0s31f6
```

2. ping -b 10.123.1.255
```
PING 10.123.1.255 (10.123.1.255) 56(84) bytes of data.
From 148.81.246.1 icmp_seq=1 Destination Host Unreachable
```

3. nmap -p- 127.0.0.1
```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-03-21 09:10 CET
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000027s latency).
Not shown: 65532 closed tcp ports (conn-refused)
PORT     STATE SERVICE
22/tcp   open  ssh
631/tcp  open  ipp
5432/tcp open  postgresql

Nmap done: 1 IP address (1 host up) scanned in 1.37 seconds
```

4. cat /etc/resolv.conf
```
# This is /run/systemd/resolve/stub-resolv.conf managed by man:systemd-resolved(8).
# Do not edit.
#
# This file might be symlinked as /etc/resolv.conf. If you're looking at
# /etc/resolv.conf and seeing this text, you have followed the symlink.
#
# This is a dynamic resolv.conf file for connecting local clients to the
# internal DNS stub resolver of systemd-resolved. This file lists all
# configured search domains.
#
# Run "resolvectl status" to see details about the uplink DNS servers
# currently in use.
#
# Third party programs should typically not access this file directly, but only
# through the symlink at /etc/resolv.conf. To manage man:resolv.conf(5) in a
# different way, replace this symlink by a static file or a different symlink.
#
# See man:systemd-resolved.service(8) for details about the supported modes of
# operation for /etc/resolv.conf.

nameserver 127.0.0.53
options edns0 trust-ad
search .
```

5. 

6. dig @8.8.8.8 kosmatka.pl MX
```
; <<>> DiG 9.18.30-0ubuntu0.24.04.2-Ubuntu <<>> @8.8.8.8 kosmatka.pl MX
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 63897
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;kosmatka.pl.			IN	MX

;; ANSWER SECTION:
kosmatka.pl.		21600	IN	MX	10 mx2.privateemail.com.
kosmatka.pl.		21600	IN	MX	10 mx1.privateemail.com.

;; Query time: 26 msec
;; SERVER: 8.8.8.8#53(8.8.8.8) (UDP)
;; WHEN: Thu Mar 20 16:58:37 CET 2025
;; MSG SIZE  rcvd: 96
```

7. nslookup google.pl
```
Server:		127.0.0.53
Address:	127.0.0.53#53

Non-authoritative answer:
Name:	google.pl
Address: 142.250.186.195
Name:	google.pl
Address: 2a00:1450:401b:80d::2003
```

8. whois kosmatka.pl
```
Data rejestracji: 2022-12-02 12:27:10
Opłata do: 2032-12-02 12:27:10

https://www.dns.pl/lista_domen_usunietych
```
9. sudo netstat -tulp
```
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 localhost:postgresql    0.0.0.0:*               LISTEN      1611/postgres       
tcp        0      0 _localdnsproxy:domain   0.0.0.0:*               LISTEN      1050/systemd-resolv 
tcp        0      0 localhost:ipp           0.0.0.0:*               LISTEN      1582/cupsd          
tcp        0      0 _localdnsstub:domain    0.0.0.0:*               LISTEN      1050/systemd-resolv 
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN      1/init              
tcp6       0      0 ip6-localhost:ipp       [::]:*                  LISTEN      1582/cupsd          
udp        0      0 _localdnsproxy:domain   0.0.0.0:*                           1050/systemd-resolv 
udp        0      0 _localdnsstub:domain    0.0.0.0:*                           1050/systemd-resolv 
udp        0      0 0.0.0.0:mdns            0.0.0.0:*                           1153/avahi-daemon:  
udp        0      0 0.0.0.0:39406           0.0.0.0:*                           1153/avahi-daemon:  
udp6       0      0 [::]:59455              [::]:*                              1153/avahi-daemon:  
udp6       0      0 [::]:mdns               [::]:*                              1153/avahi-daemon:
```

10. traceroute pw.plock.pl
```
traceroute to pw.plock.pl (148.81.247.250), 64 hops max
  1   192.168.48.1  0.738ms  0.390ms  0.610ms 
  2   148.81.247.250  1.278ms  0.734ms  0.569ms
```