#!/usr/bin/env python

import shlex
import subprocess

cmd = "ls -la /tmp'"
proc = subprocess.Popen(shlex.split(cmd), shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

for line in iter(proc.stdout.readline, ''):
        print line[:-1]
