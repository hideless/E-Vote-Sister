import xmlrpc.client
import time

class supervisor():
    def Login(self, username, password):
        if (username == "supervisor" and password == "supervisor"):
            return True
        else:
            return False
    def server(self):
        s = xmlrpc.client.ServerProxy('http://192.168.0.5:5000')
        return s
    def Hasil(self):
        s = a.server()
        bem = (s.candidateAppBEM())
        dpm = (s.candidateAppDPM())
        hima = (s.candidateAppHIMA())

        print("\n----- HASIL PEMILIHAN BEM -----")
        for i in range(len(bem)):
            print(bem[i])
        print("\n----- HASIL PEMILIHAN DPM -----")
        for j in range(len(dpm)):
            print(dpm[j])
        print("\n----- HASIL PEMILIHAN HIMA -----")
        for k in range(len(hima)):
            print(hima[k])

    def showBEM(self):
        s = a.server()
        return s.voteBEM()
    def showDPM(self):
        s = a.server()
        return s.voteDPM()
    def showHIMA(self):
        s = a.server()
        return s.voteHIMA()
    def showRecord(self):
        s = a.server()
        return s.showRecord()
    def resetAll(self):
        s = a.server()
        reset = (s.resetALL())

a = supervisor()
while True:
    print("----- MENU LOGIN SUPERVISOR -----")
    username = input("Username\t: ")
    password = input("Password\t: ")
    print("---------------------------------")
    pilih = ""
    while pilih != "0":
        if (a.Login(username,password) == True):
            print("\n----- MENU UTAMA SUPERVISOR -----")
            print("1. Lihat Hasil Pemilu")
            print("2. Lihat Jumlah Voter")
            print("3. Lihat Detail Pemilihan")
            print("4. Reset Data")
            print("0. Logout")
            pilih =  input("Pilih\t: ")
            if (pilih == "1"):
                a.Hasil()

            elif (pilih == "2"):
                print("Total Pemilih BEM\t: ", a.showBEM())
                print("Total Pemilih DPM\t: ", a.showDPM())
                print("Total Pemilih HIMA\t: ", a.showHIMA())
                if(a.showBEM() == a.showDPM() and a.showDPM() == a.showHIMA()):
                    print("Status data\t: Valid")
                else:
                    print("Status data\t: Tidak Valid")

            elif(pilih == "3"):
                print("NIM\tBEM\tDPM\tHIMA\t")
                for i in range(len(a.showRecord())):
                    print(a.showRecord()[i])

            elif (pilih == "4"):
                a.resetAll()
                print("Database Berhasil di Reset!")
                print("Kembali ke Menu Utama dalam 3 Detik...")
                time.sleep(3)
            elif (pilih == "0"):
                print("\nProgram Akan Kembali Ke Menu Login Dalam 3 Detik...")
                time.sleep(3)
                break
        else:
            break
