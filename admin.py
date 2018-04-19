import xmlrpc.client

class admin:

    def cekAdmin(self, username, password):
        s = xmlrpc.client.ServerProxy('http://127.0.0.1:5000')
        cekAdmin = s.dataAdmin(username, password)

        if (cekAdmin == True ):
            nim = 99
            while (nim != 0):
                print("Ketik 0 untuk keluar")
                nim2 = input("NIM untuk regis : ")
                nim = int(nim2)
                print(s.regis(nim))
            # print(s.system.listMethods())

pilih = 00
while(pilih != "0"):
    pilih = 00
    print("===== Menu Admin =====")

    username = input("Username : ")
    password = input("Password : ")
    a = admin()
    a.cekAdmin(username,password)