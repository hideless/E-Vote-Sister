import xmlrpc.client

class candidate():
    def cekAdmin(self, username, password):
        s = xmlrpc.client.ServerProxy('http://127.0.0.1:5000')
        cekAdmin = s.dataAdmin(username, password)

        if (cekAdmin == True):
            bem  = (s.candidateAppBEM())
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
        else:
            print("Login Failed")
while True:
    print("===== MENU CANDIDATE =====")
    username = input("Username : ")
    password = input("Password : ")
    c = candidate()
    c.cekAdmin(username, password)