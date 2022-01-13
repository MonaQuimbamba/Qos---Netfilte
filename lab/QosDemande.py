#! /usr/bin/python3
# coding: utf-8
import subprocess

interface_reseau = b"r1-eth0"
filtre_ecoute = b"'ip and (ip[1] & 0x02 == 0x02)'"
ecoute_reseau = subprocess.Popen(b"tcpdump -c 1 -ln -i %s %s"%(interface_reseau,filtre_ecoute),shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
print("Resultat du TCPDUMP :" ,ecoute_reseau.stdout.read())
