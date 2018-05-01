import xmlrpc.client
import time

class voter:
    def server(self):
        s = xmlrpc.client.ServerProxy('http://192.168.0.5:5000')
        return s

    def cekvoter(self, nim):
        s = a.server()
        cek = s.cekVoter(nim)
        return cek

    def tampilBEM(self):
        s = a.server()
        bem = s.tampilBEM()
        return bem

    def tampilDPM(self):
        s = a.server()
        dpm = s.tampilDPM()
        return dpm

    def tampilHIMA(self):
        s = a.server()
        hima = s.tampilHIMA()
        return hima

    def inputRecord(self,record,nim,start,end):
        s = a.server()
        s.inputRecord(record,nim,start,end)

    def cektime(self):
        s = a.server()
        time = s.getTime()
        return time

    def cekStatusPilih(self,nim):
        s = a.server()
        cek = s.cekStatusPilih(nim)
        return cek

a = voter()
bem = a.tampilBEM()
dpm = a.tampilDPM()
hima = a.tampilHIMA()

pilih = 99
record = []
while (pilih != 00):
    print("===== MENU VOTER =====")
    nim2 = input("NIM : ")
    nim = int(nim2)
    # if (a.cekvoter(nim) == False):
    #     print("\n""||| NIM anda belum terdaftar |||")
    #     print("||| Silahkan mendaftarkan NIM anda kepada Admin |||", "\n")
    # print(a.cekvoter(nim))
    # print(a.cekStatusPilih(nim))
    try:
        if (a.cekvoter(nim) == True):
            if (a.cekStatusPilih(nim) == True):
                start = a.cektime()
                record = []
                cek = False

                print("Silahkan Gunakan Hak Pilih Anda...\n")

                while (not cek):
                    print("---- PILIH BEM ----")
                    for i in range(len(bem)):
                        print("|", i+1, "|", bem[i])
                    temp = input("Pilih BEM : ")

                    if ((int(temp) <= len(bem)) and (int(temp) != 0)):
                        pilih1 = temp
                        cek = True
                    else:
                        print("\nInput anda salah!\nSilahkan pilih kembali!\n")

                cek = False

                while (not cek):
                    print("\n---- PILIH DPM ----")
                    for j in range(len(dpm)):
                        print("|", j+1, "|", dpm[j])
                    temp = input("Pilih DPM : ")

                    if ((int(temp) <= len(dpm)) and (int(temp) != 0)):
                        pilih2 = temp
                        cek = True
                    else:
                        print("\nInput anda salah!\nSilahkan pilih kembali!\n")

                cek = False

                while (not cek):
                    print("\n---- PILIH HIMA ----")
                    for k in range(len(hima)):
                        print("|",k+1,"|", hima[k])
                    temp = input("Pilih HIMA : ")

                    if ((int(temp) <= len(hima)) and (int(temp) != 0)):
                        pilih3 = temp
                        cek = True
                    else:
                        print("\nInput anda salah!\nSilahkan pilih kembali!\n")

                record = [pilih1, pilih2, pilih3]
                end = a.cektime()
                a.inputRecord(record, nim, start, end)
                print("\n||| Terimakasih Sudah Melakukan Voting |||")
                time.sleep(1)
                print("||| Program Akan Kembali Ke Menu Utama Dalam 2 Detik |||\n")
                time.sleep(2)
            else:
                print("\n||| Mahasiswa sudah voting sebelumnya ||| \n")
    except:
        print("\n""||| NIM anda belum terdaftar |||")
        print("||| Silahkan mendaftarkan NIM anda kepada Admin |||", "\n")