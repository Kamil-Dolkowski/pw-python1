import sys

def bin_to_ip_address(ip_bin):
    first = (ip_bin >> 24)
    second = (ip_bin >> 16) & 0xFF
    third = (ip_bin >> 8) & 0xFF
    last = (ip_bin & 0xFF)
    address = f"{first}.{second}.{third}.{last}"
    return address

addr = sys.argv[1]
addr = addr.split("/")

ip = addr[0]
mask = addr[1]

ip = ip.split(".")
ip = (int(ip[0]) << 24) | (int(ip[1]) << 16) | (int(ip[2]) << 8) | int(ip[3])
print("Ip:\t\t\t", format(ip, '032b'))

mask_bin = int("1" * int(mask) + "0" * (32-int(mask)), 2)
print("Maska:\t\t\t", format(mask_bin, '032b'))

network_address = ip & mask_bin
print("Adres sieci:\t\t", format(network_address, '032b'))

broadcast = ip | (~mask_bin & 0xFFFFFFFF)
print("Adres rozgłoszeniowy:\t", format(broadcast, '032b'))

number_of_hosts = 2 ** (32 - int(mask))

print("========\n")

print("Adres IP sieci:\t\t", bin_to_ip_address(network_address))
print("Maska podsieci:\t\t", bin_to_ip_address(mask_bin))
print("Ilość hostów w sieci:\t", number_of_hosts)