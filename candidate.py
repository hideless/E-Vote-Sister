import xmlrpc.client

class candidate():
    def cekAdmin(self, username, password):
        s = xmlrpc.client.ServerProxy('http://192.168.0.5:5000')
        cekAdmin = s.dataAdmin(username, password)

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

            print("Hasil Akhir Pemilihan:")
            print("BEM Terpilih adalah: ", )
            print("DPM Terpilih adalah: ", )
            print("HIMA Terpilih adalah: ", )
        else:
            print("Login Gagal!")
            print("Username atau Password salah!")
while True:
    print("----- MENU CANDIDATE -----")
    username = input("Username : ")
    password = input("Password : ")
    print("--------------------------")
    c = candidate()
    c.cekAdmin(username, password)