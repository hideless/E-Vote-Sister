from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy

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

    class Admin:
        def dataAdmin(self, user, pas):
            for i in range(rowadm):
                # print(adm.cell(i + 1, 0).value, adm.cell(i+1, 1).value)
                if (str(adm.cell(i + 1, 0).value) == user and str(adm.cell(i+1, 1).value) == pas):
                    return True
                else:
                    return False

        def regis(self, nim):
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
                        return "Regis Success"
                    else:
                        return "Sudah Regis"
            server.serve_forever()

        def cekVoter(self,nim):
            for i in range(rowmhs-1):
                if (int(mhs.cell(i+1, 0).value) == nim):
                    if (str(mhs.cell(i+1, 4).value) == "yes"):
                        return True

    server.register_instance(Admin())

    server.register_introspection_functions()
    class Candidate():
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
        def inputRecord(self, record, nim):
            for i in range(rowrec):
                print(nim, rec.cell(i + 1, 0).value)
                if (int(rec.cell(i + 1, 0).value) == nim):
                    wb = open_workbook("database.xls")
                    wr = copy(wb)
                    s = wr.get_sheet(2)
                    r = wr.get_sheet(0)

                    print("masuk")
                    s.write(i+1, 6, int(record[0]))
                    s.write(i+1, 7, int(record[1]))
                    s.write(i+1, 8, int(record[2]))
                    for z in range(rowmhs):
                        if (int(mhs.cell(i + 1, 0).value) == nim):
                            r.write(i+1, 5, "yes")
                    wr.save('database.xls')
                    return True
                    break

    server.register_instance(Candidate())

    class AllFuncs(Admin,Candidate):
        pass
    server.register_instance(AllFuncs())

    try:
        print("Gunakan Control + C untuk keluar")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Exit")