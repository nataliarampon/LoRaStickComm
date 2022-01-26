#!/bin/bash
set -x #echo on

PORT=$(sudo socat -d -d pty,raw,echo=0 pty,raw,echo=0 2>&1 | grep -wo -m1 "/dev/.*" &)
echo "$PORT"
make PORT=$PORT run