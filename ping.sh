#!/bin/bash

python pingServer.py & sleep 2

python pingClient.py
