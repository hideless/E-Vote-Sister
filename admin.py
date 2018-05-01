import xmlrpc.client
import time

class admin:

    def cekAdmin(self, username, password):
        s = xmlrpc.client.ServerProxy('http://192.168.0.5:5000')
        cekAdmin = s.dataAdmin(username, password)

        if (cekAdmin == True ):
            pilih = ""
            while (pilih != "0"):
                print("\n""----- MENU UTAMA ADMIN -----")
                print("1. Registrasi Voter")
                print("2. Input Data")
                print("3. Input Kandidat")
                print("0. Logout Admin")
                pilih = input("Pilih\t: ")
                if (pilih == "1"):
                    nim2 = input("\n""Masukkan NIM untuk diaktivasi: ")
                    nim = int(nim2)
                    print(s.regis(nim))
                    time.sleep(1)

                elif(pilih == "2"):
                    print("Input Data")
                    nim = input("NIM\t: ")
                    nama = input("Nama\t: ")
                    fakultas = input("Fakultas\t: ")
                    prodi  = input("Prodi\t: ")
                    s.inputDataVoter(nim, nama, fakultas, prodi)
                    print("Data Saved")

                elif(pilih == "3"):
                    cek = s.cekRegis()
                    print(cek)
                    if(cek != True):
                        print("Input Pasangan Kandidat")
                        bem = list()
                        dpm = list()
                        hima = list()
                        jum2 = input("Jumlah Kandidat BEM\t: ")
                        jum = int(jum2)
                        while True:
                            if (jum >= 2):
                                print("Input Kandidat BEM")
                                for i in range(jum):
                                    temp = input("Nama Pasangan Kandidat\t: ")
                                    bem.append(str(temp))
                                break
                            else:
                                print("Jumlah Kandidat Tidak Valid (>=2)")

                        jum2 = input("Jumlah Kandidat DPM\t: ")
                        jum = int(jum2)
                        while True:
                            if (jum >= 2):
                                print("Input Kandidat DPM")
                                for i in range(jum):
                                    temp = input("Nama Pasangan Kandidat\t: ")
                                    dpm.append(str(temp))
                                break
                            else:
                                print("Jumlah Kandidat Tidak Valid (>=2)")

                        jum2 = input("Jumlah Kandidat HIMA\t: ")
                        jum = int(jum2)
                        while True:
                            if (jum >= 2):
                                print("Input Kandidat HIMA")
                                for i in range(jum):
                                    temp = input("Nama Pasangan Kandidat\t: ")
                                    hima.append(str(temp))
                                break
                            else:
                                print("Jumlah Kandidat Tidak Valid (>=2)")
                        s.inputDataKandidat(bem, dpm, hima)

                    else:
                        print("Access Denied")
                        
            # print(s.system.listMethods())

pilih = 00
while(pilih != "0"):
    pilih = 00
    print("\n""----- Login Admin -----")
    username = input("Username : ")
    password = input("Password : ")
    print("-----------------------")
    a = admin()
    a.cekAdmin(username,password)
