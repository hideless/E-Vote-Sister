import xmlrpc.client

print("===== MENU VOTER =====")

class voter:

    def cekvoter(self, nim):
        s = xmlrpc.client.ServerProxy('http://127.0.0.1:5000')
        cek = s.cekVoter(nim)
        return cek

    def tampil(self):
        s = xmlrpc.client.ServerProxy('http://127.0.0.1:5000')
        return s.tampilBEM()

nim2 = input("NIM : ")
nim = int(nim2)
a = voter()
record = []
if (a.cekvoter(nim) == True):
    print(a.tampil())
    pilih1 = input("Pilih BEM : ")

    print("PILIH DPM")
    print("1. MT dan Khanza")
    print("2. Agi dan Erin")
    print("3. Taufan dan Tashya")
    pilih2 = input("Pilih DPM : ")

    print("PILIH KAHIM")
    print("1. Udin Gebok dan Jajang Oray")
    print("2. Asep Pengkor dan Usep Pitak")
    print("3. Dadang Sumur dan Ujang Kebon")
    pilih3 = input("Pilih KAHIM : ")

    record = [pilih1,pilih2,pilih3]