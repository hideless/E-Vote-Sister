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
    bem = workbook.sheet_by_index(3)
    dpm = workbook.sheet_by_index(4)
    hima = workbook.sheet_by_index(5)
    rowadm = adm.nrows
    rowmhs = mhs.nrows
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

                        s.write(i+1, 4, 'yes')
                        wr.save('database.xls')
                        print("masuk")
                        return "Regis Success"
                    else:
                        return "Sudah Regis"
                else:
                    return "Failed"

        def cekVoter(self,nim):
            for i in range(rowmhs):
                if (int(mhs.cell(i+1, 0).value) == nim):
                    if (str(mhs.cell(i+1, 4).value) == "yes"):
                        return True

    server.register_instance(Admin())

    server.register_introspection_functions()
    class Candidate():
        def tampilBEM(self):
            for i in range(rowbem):
                print(i+1,". ",bem.cell(i+1, 0).value)
                cbem.append(str(bem.cell(i+1, 0).value))
            return cbem
        def tampilDPM(self):
            for i in range(rowdpm):
                # print(i+1,". ",dpm.cell(i+1, 0).value)
                cdpm.append(str(dpm.cell(i + 1, 0).value))
            return cdpm
        def tampilHIMA(self):
            for i in range(rowhima):
                # print(i+1,". ",hima.cell(i+1, 0).value)
                chima.append(str(hima.cell(i + 1, 0).value))
            return chima
    server.register_instance(Candidate())

    class AllFuncs(Admin,Candidate):
        pass
    server.register_instance(AllFuncs())

    try:
        print("Gunakan Control + C untuk keluar")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Exit")