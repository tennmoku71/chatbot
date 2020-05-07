#!/bin/bash

python3 -m http.server --cgi 8080 &
pid=$!
echo "pid: $pid"
echo "access http://localhost:8080/cgi-bin/chatbot.py"
echo "server stop sudo kill -9 $pid"
sleep 1