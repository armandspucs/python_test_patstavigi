"""Funkcija akceptē divus argumentus - skaiļus a un b,
aprēķina to dalījumu un atgriež to. Ja skaiļus dalīt nedrīkst,
atgriež 0.

Argumenti:
    a {int vai float} -- pirmais skaitlis
    b {int vai float} -- otrais skaitlis
Atgriež:
    int vai float -- rezultāts
"""

def dali(a,b):
    result = a/b
    if result < 1:
      result = 0
    return result