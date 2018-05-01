import xmlrpc.client

class supervisor():
    def Login(self, username, password):
        if (username == "supervisor" and password == "supervisor"):
            print("Login Success")
            return True
        else:
            print("Login Failed")
            return False
    def server(self):
        s = xmlrpc.client.ServerProxy('http://127.0.0.1:5000')
        return s
    def Hasil(self):
        s = a.server()
        bem = (s.candidateAppBEM())
        dpm = (s.candidateAppDPM())
        hima = (s.candidateAppHIMA())

        print("***** HASIL BEM *****")
        for i in range(len(bem)):
            print(bem[i])
        print("***** HASIL DPM *****")
        for j in range(len(dpm)):
            print(dpm[j])
        print("***** HASIL HIMA *****")
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
    print("===== MENU SUPERVISOR =====")
    username = input("Username\t: ")
    password = input("Password\t: ")
    pilih = ""
    while pilih != "0":
        if (a.Login(username,password) == True):
            print("1. Lihat Hasil Pemilu")
            print("2. Lihat Jumlah Voter")
            print("3. Lihat Detail Pemilihan")
            print("4. Reset Data")
            print("0. Log Out")
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
                print(a.resetAll())
        else:
            break
