import threading
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy
import datetime
import time

#membatasi path
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

#membuat server
with SimpleXMLRPCServer(("127.0.0.1",5000), requestHandler=RequestHandler) as server:
    workbook = xlrd.open_workbook("database.xls")
    mhs = workbook.sheet_by_index(0)
    adm = workbook.sheet_by_index(1)
    rec = workbook.sheet_by_index(2)
    bem = workbook.sheet_by_index(3)
    dpm = workbook.sheet_by_index(4)
    hima = workbook.sheet_by_index(5)
    rowadm = adm.nrows
    rowmhs = mhs.nrows
    rowrec = rec.nrows
    rowbem = bem.nrows
    rowdpm = dpm.nrows
    rowhima = hima.nrows

    cbem = list()
    cdpm = list()
    chima = list()

    #untuk mengetahui metode yang register
    server.register_introspection_functions()

    class Admin(threading.Thread):
        def dataAdmin(self, user, pas):
            for i in range(1,rowadm):
                # print(adm.cell(i, 0).value, adm.cell(i, 1).value)
                if (str(adm.cell(i, 0).value) == user and str(adm.cell(i, 1).value) == pas):
                    return True
            return False

        def getTime(self):
            time = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            return time

        def regis(self, nim):
            workbook = xlrd.open_workbook("database.xls")
            mhs = workbook.sheet_by_index(0)
            rec = workbook.sheet_by_index(2)
            rowrec = rec.nrows
            for i in range (rowmhs):
                if (int(mhs.cell(i+1, 0).value) == nim):
                    if (str(mhs.cell(i+1, 4).value) != "yes"):
                        wb = open_workbook("database.xls")
                        wr = copy(wb)
                        s = wr.get_sheet(0)
                        r = wr.get_sheet(2)

                        for j in range(4):
                            r.write(rowrec, j, mhs.cell(i+1, j).value)

                        s.write(i+1, 4, 'yes')
                        wr.save('database.xls')
                        return "Registrasi Sukses! \nSilahkan Lakukan E-Voting"
                    else:
                        return "Maaf, Anda Sudah Melakukan Registrasi Sebelumnya"
            return True

        def cekVoter(self,nim):
            workbook = xlrd.open_workbook("database.xls")
            mhs = workbook.sheet_by_index(0)
            rowmhs = mhs.nrows
            for i in range(1,rowmhs):
                # print(int(mhs.cell(i, 0).value), nim, rowmhs)
                # print(int(mhs.cell(i, 0).value), str(mhs.cell(i, 4).value))
                if (int(mhs.cell((i), 0).value) == nim):
                    # print(int(mhs.cell(i, 0).value), str(mhs.cell(i, 4).value), int(mhs.cell(i, 6).value))
                    if (str(mhs.cell(i, 4).value) == "yes" and int(mhs.cell(i, 6).value) == 0):
                        wb = open_workbook("database.xls")
                        wr = copy(wb)
                        s = wr.get_sheet(0)

                        s.write(i, 6, 1)
                        wr.save('database.xls')
                        return True
                    else:
                        return False

        def inputDataVoter(self, nim, nama, fakultas, prodi):
            workbook = xlrd.open_workbook("database.xls")
            mhs = workbook.sheet_by_index(0)
            rowmhs = mhs.nrows


            wb = open_workbook("database.xls")
            wr = copy(wb)
            s = wr.get_sheet(0)

            s.write(rowmhs, 0, int(nim))
            s.write(rowmhs, 1, nama)
            s.write(rowmhs, 2, fakultas)
            s.write(rowmhs, 3, prodi)
            s.write(rowmhs, 4, "no")
            s.write(rowmhs, 5, "no")
            s.write(rowmhs, 6, int(0))

            wr.save('database.xls')

            return True

        def cekRegis(self):
            workbook = xlrd.open_workbook("database.xls")
            mhs = workbook.sheet_by_index(0)
            rowmhs = mhs.nrows
            cek = False
            for x in range(rowmhs):
                # print(str((mhs.cell(x, 4).value)))
                if(str(mhs.cell(x, 4).value) == "yes"):
                    # print("Masuk")
                    cek = True
            return cek

        def inputDataKandidat(self, xbem, xdpm, xhima):
            wb = open_workbook("database.xls")
            wr = copy(wb)
            s = wr.get_sheet(3)
            t = wr.get_sheet(4)
            u = wr.get_sheet(5)
            
            for i in range(1,(rowbem)):
                s.write(i, 0 , int(i))
                s.write(i, 0, "")
                s.write(i, 1,"")
                s.write(i, 2, "")

            for i in range(1,(rowdpm)):
                t.write(i, 0 , int(i))
                t.write(i, 0, "")
                t.write(i, 1,"")
                t.write(i, 2, "")

            for i in range(1,(rowhima)):
                u.write(i, 0 , int(i))
                u.write(i, 0, "")
                u.write(i, 1,"")
                u.write(i, 2, "")

            for i in range(len(xbem)):
                s.write(i+1, 0, int(i + 1))
                s.write(i+1, 1, str(xbem[i]))
                s.write(i + 1, 2, int(0))
            for i in range(len(xdpm)):
                t.write(i+1, 0, int(i + 1))
                t.write(i+1, 1, str(xdpm[i]))
                t.write(i + 1, 2, int(0))
            for i in range(len(xhima)):
                u.write(i+1, 0, int(i + 1))
                u.write(i+1, 1, str(xhima[i]))
                u.write(i + 1, 2, int(0))

            wr.save('database.xls')
            return True

        def resetDataMahasiswa(self):
            workbook = xlrd.open_workbook("database.xls")
            mhs = workbook.sheet_by_index(0)
            rowmhs = mhs.nrows

            wb = open_workbook("database.xls")
            wr = copy(wb)
            s = wr.get_sheet(0)

            for i in range(1, rowmhs):
                s.write(i, 4, "no")
                s.write(i, 5, "no")
                s.write(i, 6, 0)

            wr.save('database.xls')

            return True

        def resetDataRecord(self):
            workbook = xlrd.open_workbook("database.xls")
            rec = workbook.sheet_by_index(2)
            rowrec = rec.nrows
            colrec = rec.ncols

            wb = open_workbook("database.xls")
            wr = copy(wb)
            s = wr.get_sheet(2)

            for i in range(1, rowrec):
                for j in range(0, colrec):
                    s.write(i, j, None)

            wr.save('database.xls')

            return True

        def resetDataBEM(self):
            workbook = xlrd.open_workbook("database.xls")
            bem = workbook.sheet_by_index(3)
            rowbem = bem.nrows

            wb = open_workbook("database.xls")
            wr = copy(wb)
            s = wr.get_sheet(3)

            for i in range(1, rowbem):
                s.write(i, 2, 0)

            wr.save('database.xls')

            return True

        def resetDataDPM(self):
            workbook = xlrd.open_workbook("database.xls")
            dpm = workbook.sheet_by_index(4)
            rowdpm = dpm.nrows

            wb = open_workbook("database.xls")
            wr = copy(wb)
            s = wr.get_sheet(4)

            for i in range(1, rowdpm):
                s.write(i, 2, 0)

            wr.save('database.xls')

            return True

        def resetDataHIMA(self):
            workbook = xlrd.open_workbook("database.xls")
            hima = workbook.sheet_by_index(5)
            rowhima = hima.nrows

            wb = open_workbook("database.xls")
            wr = copy(wb)
            s = wr.get_sheet(5)

            for i in range(1, rowhima):
                s.write(i, 2, 0)

            wr.save('database.xls')

            return True

        def resetALL(self):
            a = Admin()
            a.resetDataBEM()
            a.resetDataDPM()
            a.resetDataHIMA()
            a.resetDataMahasiswa()
            a.resetDataRecord()

            return True

    server.register_instance(Admin())

    server.register_introspection_functions()
    class Voters():
        def tampilBEM(self):
            cbem = []
            for i in range(rowbem-1):
                # print(i+1,". ",bem.cell(i+1, 1).value)
                cbem.append(str(bem.cell(i+1, 1).value))
            return cbem
        def tampilDPM(self):
            cdpm = []
            for i in range(rowdpm-1):
                # print(i+1,". ",dpm.cell(i+1, 1).value)
                cdpm.append(str(dpm.cell(i + 1, 1).value))
            return cdpm
        def tampilHIMA(self):
            chima = []
            for i in range(rowhima-1):
                # print(i+1,". ",hima.cell(i+1, 1).value)
                chima.append(str(hima.cell(i + 1, 1).value))
            return chima
        def cekStatusPilih(self, nim):
            workbook = xlrd.open_workbook("database.xls")
            mhs = workbook.sheet_by_index(0)
            rowmhs = mhs.nrows
            for i in range(1, rowmhs):
                # print(int(mhs.cell(i, 0).value), str(mhs.cell(i, 5).value))
                if (int(mhs.cell(i, 0).value) == nim and str(mhs.cell(i, 5).value) == "no"):
                    # if (str(mhs.cell(i+1, 5).value) == "no"):
                    return True
            return False

        def inputRecord(self, record, nim, start, end):
            workbook = xlrd.open_workbook("database.xls")
            rec = workbook.sheet_by_index(2)
            mhs = workbook.sheet_by_index(0)
            bem = workbook.sheet_by_index(3)
            dpm = workbook.sheet_by_index(4)
            hima = workbook.sheet_by_index(5)
            rowrec = rec.nrows
            rowmhs = mhs.nrows
            for i in range(1, rowrec):
                if (int(rec.cell(i, 0).value) == nim):
                    wb = open_workbook("database.xls")
                    wr = copy(wb)
                    s = wr.get_sheet(2)
                    r = wr.get_sheet(0)
                    t = wr.get_sheet(3)
                    u = wr.get_sheet(4)
                    v = wr.get_sheet(5)

                    s.write(i, 4, start)
                    s.write(i, 5, end)
                    s.write(i, 6, int(record[0]))
                    s.write(i, 7, int(record[1]))
                    s.write(i, 8, int(record[2]))

                    for x in range(1,rowbem):
                        if (int(bem.cell(x,0).value) == int(record[0])):
                            t.write(x, 2, int(bem.cell(x,2).value)+1)

                    for x in range(1,rowdpm):
                        if (int(dpm.cell(x,0).value) == int(record[1])):
                            u.write(x, 2, int(dpm.cell(x,2).value)+1)

                    for x in range(1,rowhima):
                        if (int(hima.cell(x,0).value) == int(record[2])):
                            v.write(x, 2, int(hima.cell(x,2).value)+1)

                    for z in range(rowmhs):
                        if (int(mhs.cell(z + 1, 0).value) == nim):
                            r.write(z+1, 5, "yes")
                            break
                    wr.save('database.xls')
                    return True

    server.register_instance(Voters())

    class Candidate():
        def candidateAppBEM(self):
            cbem = []
            for i in range(1, rowbem):
                cbem.append([int(bem.cell(i, 0).value), str(bem.cell(i, 1).value), int(bem.cell(i, 2).value)])
            return cbem

        def candidateAppDPM(self):
            cdpm = []
            for i in range(1, rowdpm):
                cdpm.append([int(dpm.cell(i, 0).value), str(dpm.cell(i, 1).value), int(dpm.cell(i, 2).value)])
            return cdpm

        def candidateAppHIMA(self):
            chima = []
            for i in range(1, rowhima):
                chima.append([int(hima.cell(i, 0).value), str(hima.cell(i, 1).value), int(hima.cell(i, 2).value)])
            return chima

    server.register_instance(Candidate())

    class Supervisor():
        def voteBEM(self):
            jumlahBEM = 0
            for i in range(1, rowbem):
                jumlahBEM += int(bem.cell(i, 2).value)
            return jumlahBEM

        def voteDPM(self):
            jumlahDPM = 0
            for i in range(1, rowdpm):
                jumlahDPM += int(dpm.cell(i, 2).value)
            return jumlahDPM

        def voteHIMA(self):
            jumlahHIMA = 0
            for i in range(1, rowhima):
                jumlahHIMA += int(hima.cell(i, 2).value)
            return jumlahHIMA

        def showRecord(self):
            record = []
            workbook = xlrd.open_workbook("database.xls")
            rec = workbook.sheet_by_index(2)
            rowrec = rec.nrows
            for i in range(1, rowrec):
                record.append([rec.cell(i,0).value, rec.cell(i,6).value, rec.cell(i,7).value, rec.cell(i,8).value])
            return record

    server.register_instance(Supervisor())

    class AllFuncs(Admin, Voters, Candidate, Supervisor):
        pass
    server.register_instance(AllFuncs())

    try:
        print("Server sedang berjalan...")
        print("Gunakan Control + C untuk keluar")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Exit")
