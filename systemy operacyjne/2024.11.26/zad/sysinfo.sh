#!/bin/bash


print_cpu() {
    echo -n "CPU: " 
    cat /proc/cpuinfo | head -n 5 | tail -n 1 | cut -c 14-100
}

print_memory() {
    total=$(free -m | awk 'NR>1 {print $2}' | head -n 1)
    used=$(free -m | awk 'NR>1 {print $3}' | head -n 1)

    procent=$((100*$used/$total)) 

    echo "Memory: $used / $total MiB ($procent% used)"
}

print_load() {
    echo -n "Load: " 
    uptime | awk '{print $8, $9, $10}'
}

print_uptime() {
    echo -n "Uptime: "
    uptime | awk '{print $3}' | tr -d ',' | awk -F: '{print $1 " hour,", $2 " minutes"}'
}

print_kernel() {
echo "a"
}

print_gpu() {
echo "a"
}

print_user() {
echo -n "User: "
whoami
}

print_shell() {
echo "a"
}

print_processes() {
echo "a"
}

print_threads() {
echo "a"
}

print_ip() {
echo "a"
}

print_dns() {
    echo -n "DNS: "
    cat /etc/resolv.conf | grep 'nameserver' | cut -c 12-27
}

print_internet() {
    ping 8.8.8.8 -W 1 -c 1
}


if [ $1 ] ; then 
    echo "ss"
else
    print_cpu
    print_memory
    print_load
    print_uptime
    print_kernel
    print_gpu
    print_user
    print_shell
    print_processes
    print_threads
    print_ip
    print_dns
    print_internet
fi




# root -> zwraca 1