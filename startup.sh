#!/usr/bin/env bash

source setup/lib/bin/activate

nohup python3 run/wsgi.py &
