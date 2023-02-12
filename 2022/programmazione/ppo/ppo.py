#!/bin/env python3

import sys

# Se vuoi leggere/scrivere da file decommenta qua
# fin = open("input.txt", "r")  # File di input fornito dalla piattaforma
# fout = open("output.txt", "w")  # Output da inviare alla piattaforma

# Se vuoi leggere/scrivere da linea di comando decommenta qua
fin = sys.stdin  # input fornito dalla piattaforma
fout = sys.stdout  # Output da inviare alla piattaforma


def controlla(nuova, vecchia):
    print(nuova, vecchia)
    # SCRIVI QUA IL TUO CODICE
    # RITORNA 0 SE LA NUOVA PASSWORD NON SEGUE LE SPECIFICHE
    # RITORNA 1 SE LA NUOVA PASSWORD SEGUE LE SPECIFICHE
    return 1


N = int(fin.readline().strip())

for _ in range(N):
    nuova, vecchia = fin.readline().strip().split(" ")
    print(controlla(nuova, vecchia), file=fout)
