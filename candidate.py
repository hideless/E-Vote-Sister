import xmlrpc.client

class candidate():
    def cekAdmin(self, username, password):
        s = xmlrpc.client.ServerProxy('http://192.168.0.5:5000')
        cekAdmin = s.dataAdmin(username, password)
        time = str(s.getTime())

        if (time >= "2018-05-01 16:51:07"):
            if (cekAdmin == True):
                bem  = (s.candidateAppBEM())
                dpm = (s.candidateAppDPM())
                hima = (s.candidateAppHIMA())
                print("\n", "===== HASIL PEMILIHAN E-VOTE =====", "\n")

                print("------ HASIL BEM ------")
                for i in range(len(bem)):
                    print(bem[i])
                print("\n","------ HASIL DPM ------")
                for j in range(len(dpm)):
                    print(dpm[j])
                print("\n","------ HASIL HIMA ------")
                for k in range(len(hima)):
                    print(hima[k])

                print("\n ================================== \n")
            else:
                print("Login Gagal!")
                print("Username atau Password salah!")
        else:
            print("Voting masih berjalan")
while True:
    print("----- MENU CANDIDATE -----")
    username = input("Username : ")
    password = input("Password : ")
    print("--------------------------")
    c = candidate()
    c.cekAdmin(username, password)