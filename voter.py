import xmlrpc.client

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
    # print(a.cekvoter(nim))
    # print(a.cekStatusPilih(nim))
    if (a.cekvoter(nim) == True):
        if (a.cekStatusPilih(nim) == True):
            start = a.cektime()
            record = []
            print("Silahkan Gunakan Hak Pilih Anda...\n")
            print("---- PILIH BEM ----")
            for i in range(len(bem)):
                print("|", i+1, "|", bem[i])
            pilih1 = input("Pilih BEM : ")

            print("\n---- PILIH DPM ----")
            for j in range(len(dpm)):
                print("|", j+1, "|", dpm[j])
            pilih2 = input("Pilih DPM : ")

            print("\n---- PILIH HIMA ----")
            for k in range(len(hima)):
                print("|",k+1,"|", hima[k])
            pilih3 = input("Pilih HIMA : ")

            record = [pilih1, pilih2, pilih3]
            end = a.cektime()
            a.inputRecord(record, nim, start, end)
            print("Terimakasih Sudah Melakukan Voting \n")
        else:
            print("\n||| Mahasiswa sudah voting sebelumnya ||| \n")
    else:
        print("\n""||| NIM anda belum terdaftar |||")
        print("||| Silahkan mendaftarkan NIM anda kepada Admin |||", "\n")