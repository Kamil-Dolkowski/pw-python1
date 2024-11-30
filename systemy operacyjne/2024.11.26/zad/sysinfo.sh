#!/bin/bash


print_cpu() {
    echo -n "CPU: " 
    cat /proc/cpuinfo | head -n 5 | tail -n 1 | cut -c 14-
}

print_memory() {
    total=$(free -m | awk 'NR>1 {print $2}' | head -n 1)
    used=$(free -m | awk 'NR>1 {print $3}' | head -n 1)

    procent=$((100*$used/$total)) 

    echo "Memory: $used / $total MiB ($procent% used)"
}

print_load() {
    echo -n "Load: " 
    uptime | awk -F, '{print $3 $4 $5}' | cut -c 17-
}

print_uptime() {
    echo -n "Uptime: "
    uptime -p | cut -c 4-
}

print_kernel() {
    echo -n "Kernel: "
    uname -r
}

print_gpu() {
    echo -n "GPU: "
    lspci | grep "VGA" | awk -F: '{print $3}' | cut -c 2-
}

print_user() {
    echo -n "User: "
    whoami
}

print_shell() {
    echo -n "Shell: "
    env | grep "SHELL=" | awk -F/ '{print $3}'
}

print_processes() {
    echo -n "Processes: "
    ps -e | grep -E "[0-9]+" -c
}

print_threads() {
    echo -n "Threads: "
    ps -me | grep " -" -c
}

print_ip() {
    echo -n "IP: "
    echo -n "$(ip addr show | grep "inet " | awk '{print $2}' | head -n 1) "
    echo $(ip addr show | grep "inet " | awk '{print $2}' | tail -n 1)
}

print_dns() {
    echo -n "DNS: "
    cat /etc/resolv.conf | grep 'nameserver' | cut -c 12-27
}

print_internet() {
    echo -n "Internet: "

    ping 8.8.8.8 -W 1 -c 1 &> /dev/null 
    if [ $? -eq 0 ] ; then
        echo "OK"
    else
        echo "NOT OK"
    fi
}


return_value=0



if [ $1 ] ; then 
    while [ $1 ]; 
    do 
        command=$1

        case ${command,,} in
            ("cpu")
                print_cpu
                ;;
            ("memory")
                print_memory
                ;;
            ("load")
                print_load
                ;;
            ("uptime")
                print_uptime
                ;;
            ("kernel")
                print_kernel
                ;;
            ("gpu")
                print_gpu
                ;;
            ("user")
                print_user
                ;;
            ("shell")
                print_shell
                ;;
            ("processes")
                print_processes
                ;;
            ("threads")
                print_threads
                ;;
            ("ip")
                print_ip
                ;;
            ("dns")
                print_dns
                ;;
            ("internet")
                print_internet
                ;;
            (*)
                echo "Error: Argument '$1' does not exists."
                return_value=1
                break
                ;;
        esac

        shift

    done
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


echo -e "\nReturn value: $return_value"
