#!/bin/bash

X=77  

for Y in $(seq 71 90); do
  if [ $Y -ne $X ]; then
    sudo ip route add 10.192.$Y.0/30 via 192.168.48.$Y
  fi
done