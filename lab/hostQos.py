#! /usr/bin/python3
# coding: utf-8
import subprocess

paquet = subprocess.Popen(b"hping3 -c 10 -V  --ttl 2 192.168.20.1",shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
print("Paquet envoyé :" ,paquet.stdout.read().decode("utf-8"))
