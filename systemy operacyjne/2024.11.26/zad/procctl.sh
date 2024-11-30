#!/bin/bash

print_menu() {
    echo -e "\nProcess Control:"
    echo "1) List top 5 processes by CPU usage"
    echo "2) List top 5 processes by memory usage"
    echo "3) Show process tree"
    echo "4) Show process name by PID"
    echo "5) Show process PID(s) by name"
    echo "6) Kill process by PID"
    echo "7) Kill process by name"
    echo "q) Exit"
    echo -n "Choice: "
}

list_top_5_by_cpu() {
    echo -e "1) List top 5 processes by CPU usage:\n"
    tput rmam
    ps aux | head -n 1 && ps aux | sort -n -r -k 3 | head -n 5
    tput smam
}

list_top_5_by_memory() {
    echo -e "2) List top 5 processes by memory usage:\n"
    tput rmam
    ps aux | head -n 1 && ps aux | sort -n -r -k 4 | head -n 5
    tput smam
}

show_process_tree() {
    echo -e "3) Show process tree:\n"
    pstree
}

show_process_name_by_pid() {
    echo -e "4) Show process name by PID:\n"

    echo -n "Enter process PID: "
    read pid

    if [[ $pid =~ ^[0-9]+$ ]] ; then
        ps $pid > /dev/null
        if [ $? -eq 0 ] ; then
            echo "Process name: "
            ps $pid | tail -n 1 | awk '{for (i=5; i<=NF; i++) printf "%s ", $i} END {print ""}'
        else
            echo "Process with PID $pid does not exists."
        fi
    else
        echo "Error: Invalid input (must be a number)."
    fi
}

show_process_pid_by_name() {
    echo -e "5) Show process PID by name:\n"
    
    echo -n "Enter process name: "
    read name

    pgrep -f "$name" > /dev/null
    if [ $? -eq 0 ] ; then
        echo "Process PID(s): "
        pgrep -f "$name"
    else
        echo "Process with name '$name' does not exists."
    fi
}

kill_process_by_pid() {
    echo -e "6) Kill process by PID:\n"
    
    echo -n "Enter process PID: "
    read pid

    if [[ $pid =~ ^[0-9]+$ ]] ; then
        ps $pid > /dev/null
        if [ $? -eq 0 ] ; then 
            kill $pid 
            echo "Process with PID $pid was killed."
        else
            echo "Process with PID $pid does not exists."
        fi
    else
        echo "Error: Invalid input (must be a number)."
    fi
}

kill_process_by_name() {
    echo -e "7) Kill process by name:\n"
    
    echo -n "Enter process name: "
    read name

    pgrep -f "$name" > /dev/null
    if [ $? -eq 0 ] ; then
        if [ "$name" != "" ] ; then
            echo "Process(es) with name '$name' was(were) killed."
            echo "Killed process(es) PID:"
            pgrep -f "$name"
            pkill -f "$name"
        else
            echo "Error: Invalid name."
        fi
    else
        echo "Process with name '$name' does not exists."
    fi
}




command="none"


while [ $command != "q" ] 
do
    print_menu
    read command

    echo ""

    case $command in
        ("1")
            list_top_5_by_cpu
            ;;
        ("2")
            list_top_5_by_memory
            ;;
        ("3")
            show_process_tree
            ;;
        ("4")
            show_process_name_by_pid
            ;;
        ("5")
            show_process_pid_by_name
            ;;
        ("6")
            kill_process_by_pid
            ;;
        ("7")
            kill_process_by_name
            ;;
        ("q")
            echo "Exit program."
            break
            ;;
        (*)
            echo "Command '$command' does not exists."
            
    esac
    
done
