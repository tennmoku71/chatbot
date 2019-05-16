#!/bin/bash

python3 -m http.server --cgi 8080 &
pid=$!
echo "pid: $pid"
sleep 5
open -n -W -a Google\ Chrome http://localhost:8080/cgi-bin/chatbot.py
echo done
