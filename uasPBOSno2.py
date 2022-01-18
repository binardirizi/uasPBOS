print ("Jawaban No 2")
print("MENAMBAHKAN DATA MAHASISWA")
print("======================================================================")
import os
os.system("cls")

list_nama =[]
list_alamat =[]
list_nim =[]

class dataMahasiswa :
    def __init__(self,nama,alamat,nim):
        self.nama=nama
        list_nama.append(self.nama)
        self.alamat=alamat
        list_alamat.append(self.alamat)
        self.nim=nim
        list_nim.append(self.nim)

    def tampildata(self):
        n=0
        print("-------------------------------")
        print("---------Data Mahasiswa--------")

        for i in range(x):
            n+=1
            print("|| No ||\tNama\t||\tAlamat\t\t\t||\tNIM\t\t||")
            print("||{}||".format(n),end="")
            print("{}\t\t".format(list_nama[i]),end="")
            print("{}\t\t".format(list_alamat[i]),end="")
            print("{}\t\t".format(list_nim[i]),end="")

            i=+1

stop = False
x=0

while(not stop):
    inputNama = input("Masukkan Nama\t\t: ")
    inputAlamat = input("Masukkan Alamat\t\t: ")
    inputNIM = input("Masukkan NIM\t\t: ")

    mahasiswa = dataMahasiswa(inputNama,inputAlamat,inputNIM)

    x+=1

    ulang = input("Apakah Anda Akan Menambah Data? [Y/T] : ")

    if (ulang=='t' or ulang=='T'):
        stop=True