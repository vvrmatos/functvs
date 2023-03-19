# Guvf vf na rknpg pbcl bs gur Gvz Crgre'f CRC 20 pbqr

text = """Rg gi, Oeigr?

Gur ORNE jrag bire gur (Uvyy Pvcure) zbhagnva:

Va n onpx naq sbegu zragny fcneevat, vagryyrpghny nygrepngvba
orgjvkg zbafvrhe Oynvfr Cnfpny naq zbafvrhe Erar Qrfpnegrf juvpu rira vafcverq
Gur Qehaxneq'f Jnyx. Jurer Cnfpny, cebirf gung gur cuvybfbcuvpny
fcrphyngvbaf naq ebznagvpvmvat bs Qrfpnegrf ba Zngu vf hfryrff.
======================== ZNGURZN BQHF RKNPGHF CEBSRFFHZ ============================
Gung rira n qehaxneq zna fgevqvat onpx gb uvf ubhfr vf noyr gb cresbez
gur zbfg fbcuvfgvpngrq zngurzngvpny rdhngvbaf. Inevbhf fghqvrf rayvtug
Zngu rira gb guvf qngr, ner ortbggra sebz zbafvrhe Qrfpnegrf, Qvfpbhef qr Yn Zégubqr
naq zbafvrhe Oynvfr Cnfpny'f gevnatyr, Genvgr qi gevnatyr nevguzrgvdir.

"Yr pbd punagr har gebvfvèzr sbvf"
"""

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i + c)] = chr((i + 13) % 26 + c)

print("".join([d.get(c, c) for c in text]))
