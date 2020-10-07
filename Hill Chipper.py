import numpy as np
from math import sqrt

def ganti_string(isi):
    angka = []
    for i in isi:
        angka.append(ord(i) % 26 - 65)
    return angka

def ganti_angka(isi):
    isi = np.round(isi % 26 + 65)
    a = np.size(isi)
    isi = np.reshape(isi,a)
    string = ''
    for i in isi:
        angka = []
        angka.append(int(i))
        string += chr(angka[0])
    return string

def buat_kunci():
    while True:
            key = input("Key : ")
            a = int(sqrt(len(key)))
            if len(pesan) % a == 0:
                break
            else:
                print("Panjang kunci harus ",(a*a),"karena panjang pesannya merupakan kelipatan ",a)
    return key

while True:
    pesan = input("Pesan : ")
    if len(pesan)%2 != 0 and len(pesan)%3 !=0:
        print("Panjang pesan harus kelipatan 2 atau 3 , karena key berbentuk Matriks 2x2 atau 3x3")
    elif any(char.isdigit() for char in pesan):
        print("Hanya menerima inputan string")
    else:
        break

key = buat_kunci()

x = int(sqrt(len(key)))
int_key= ganti_string(key.upper())

int_pesan = ganti_string(pesan.upper())
matriks_pesan = np.reshape(int_pesan,(x,int(len(int_pesan)/x)))

matriks_key = np.reshape(int_key,(x,x))
key_invers = np.linalg.inv(matriks_key)

rumus_enkrip = np.dot(matriks_key,matriks_pesan)
rumus_dekrip = np.dot(key_invers,rumus_enkrip)

if pesan.islower():
    enkrip = ganti_angka(rumus_enkrip).lower()
    dekrip = ganti_angka(rumus_dekrip).lower()
else:
    enkrip = ganti_angka(rumus_enkrip)
    dekrip = ganti_angka(rumus_dekrip)

print("Hasil Enkripsi : ",enkrip)
print("Hasil Dekripsi : ",dekrip)
