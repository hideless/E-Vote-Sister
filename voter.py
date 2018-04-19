import xmlrpc.client

class voter:

    def cekvoter(self, nim):
        s = xmlrpc.client.ServerProxy('http://127.0.0.1:5000')
        cek = s.cekVoter(nim)
        return cek

    def tampilBEM(self):
        s = xmlrpc.client.ServerProxy('http://127.0.0.1:5000')
        bem = s.tampilBEM()
        return bem

    def tampilDPM(self):
        s = xmlrpc.client.ServerProxy('http://127.0.0.1:5000')
        dpm = s.tampilDPM()
        return dpm

    def tampilHIMA(self):
        s = xmlrpc.client.ServerProxy('http://127.0.0.1:5000')
        hima = s.tampilHIMA()
        return hima

    def inputRecord(self,record,nim):
        s = xmlrpc.client.ServerProxy('http://127.0.0.1:5000')
        s.inputRecord(record,nim)

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
    if (a.cekvoter(nim) == True):
        record = []
        print("***** PILIH BEM *****")
        print(bem)
        pilih1 = input("Pilih BEM : ")

        print("***** PILIH DPM *****")
        print(dpm)
        pilih2 = input("Pilih DPM : ")

        print("***** PILIH KAHIM *****")
        print(hima)
        pilih3 = input("Pilih KAHIM : ")

        record = [pilih1, pilih2, pilih3]
        print(record)
        a.inputRecord(record,nim)