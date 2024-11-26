#!/bin/bash


cpu() {
    echo "a"
}

# brak procentów
memory() {
    total=$(free -m | awk 'NR>1 {print $2}' | head -n 1)
    used=$(free -m | awk 'NR>1 {print $3}' | head -n 1)

    procent=$(($((used))/$((total))*100))

    echo "Memory: $used / $total MiB ($procent% used)"
}

load() {
    echo -n "Load: " && uptime | awk '{print $8, $9, $10}'
}

uptime() {
    echo -n "Uptime: " && uptime | awk '{print $3}' | tr -d ',' | awk -F: '{print $1 " hour,", $2 " minutes"}'
}

kernel() {
echo "a"
}

gpu() {
echo "a"
}

user() {
echo "a"
}

shell() {
echo "a"
}

processes() {
echo "a"
}

threads() {
echo "a"
}

ip() {
echo "a"
}

dns() {
echo "a"
}

internet() {
    ping 8.8.8.8 -W 1 -c 1
}


memory


# root -> zwraca 1