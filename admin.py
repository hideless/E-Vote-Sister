import xmlrpc.client
import time

class admin:

    def cekAdmin(self, username, password):
        s = xmlrpc.client.ServerProxy('http://localhost:5000')
        cekAdmin = s.dataAdmin(username, password)

        if (cekAdmin == True ):
            pilih = ""
            while (pilih != "0"):
                print("\n""----- MENU UTAMA ADMIN -----")
                print("1. Registrasi Voter")
                print("2. Input Data Voter")
                print("3. Input Data Kandidat")
                print("0. Logout Admin")
                pilih = input("Pilih\t: ")
                if (pilih == "1"):
                    nim2 = input("\n""Masukkan NIM untuk diaktivasi: ")
                    nim = int(nim2)
                    print(s.regis(nim))
                    time.sleep(1)

                elif(pilih == "2"):
                    print("\nInput Data Voter")
                    nim = input("NIM: ")
                    nama = input("Nama: ")
                    fakultas = input("Fakultas: ")
                    prodi  = input("Prodi: ")
                    s.inputDataVoter(nim, nama, fakultas, prodi)
                    print("\n||| Data Telah Tersimpan |||")
                    time.sleep(2)

                elif(pilih == "3"):
                    if(cekAdmin == True):
                        print("\n||| Input Pasangan Kandidat BEM |||\n")
                        bem = list()
                        dpm = list()
                        hima = list()
                        jum2 = input("Jumlah Kandidat BEM: ")
                        jum = int(jum2)
                        while True:
                            if (jum >= 2):
                                print("\nInput Kandidat BEM")
                                for i in range(jum):
                                    temp = input("Nama Pasangan Kandidat\t: ")
                                    bem.append(str(temp))
                                break
                            else:
                                print("Jumlah Kandidat Tidak Valid (>=2)")
                                break

                        jum2 = input("\nJumlah Kandidat DPM: ")
                        jum = int(jum2)
                        while True:
                            if (jum >= 2):
                                print("\nInput Kandidat DPM")
                                for i in range(jum):
                                    temp = input("Nama Pasangan Kandidat\t: ")
                                    dpm.append(str(temp))
                                break
                            else:
                                print("Jumlah Kandidat Tidak Valid (>=2)")
                                break

                        jum2 = input("\nJumlah Kandidat HIMA: ")
                        jum = int(jum2)
                        while True:
                            if (jum >= 2):
                                print("\nInput Kandidat HIMA")
                                for i in range(jum):
                                    temp = input("Nama Pasangan Kandidat\t: ")
                                    hima.append(str(temp))
                                break
                            else:
                                print("Jumlah Kandidat Tidak Valid (>=2)")
                                break
                        s.inputDataKandidat(bem, dpm, hima)
                        print("\nData Telah Disimpan!")
                        print("Kembali Ke Menu Utama Dalam 3 Detik...")
                        time.sleep(3)

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
