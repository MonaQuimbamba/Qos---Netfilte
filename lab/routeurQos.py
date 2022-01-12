#! /usr/bin/python3
# coding: utf-8
import subprocess

interface_reseau = b"r1-eth0"
ecoute_reseau = subprocess.Popen(b"tcpdump -c 1 -lnv -i %s "%(interface_reseau),shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
print("Resultat du TCPDUMP :" ,ecoute_reseau.stdout.read().decode("utf-8"))
regle_firewall = subprocess.Popen(b"iptables -A PREROUTING -t mangle  -j MARK --set-mark 1",shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
print(" Régle a été appliqué ")
