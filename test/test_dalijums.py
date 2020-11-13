import pytest
from src.temp_f import temp_f
def test_temp_f(a,b):
    assert temp_f(98) == 36.67 #body temp
    assert temp_f(32) == 0 #water freezes
    assert temp_f(212) == 100 #water boils
    assert temp_f(-480) == −273.15 #apzināti pārāk zems fareheitos


"""
Funkcija akceptē vienu argumentu - temperatūru Fārenheita grādos,
un atgriež temperatūru Celsija grādos. Zemākā temperatūra
Celsija grādos var būt −273.15, tādēļ, ja aprēķinātā temperatūra ir zemāka, atgriež −273.15.

Argumenti:
    t {int vai float} -- temperatūra Fārenheita grādos
Atgriež:
    int vai float -- temperatūra Celsija grādos
"""