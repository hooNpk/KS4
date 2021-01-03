import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        self._create_kiwoom_instance()
        self._set_signal_slots()
    
    def _create_kiwoom_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")
        print("CREATE KIWOOM INSTANCE")
    
    def _set_signal_slots(self):
        self.OnEventConnect.connect(self._event_connect)
        print("On EVENT CONNECT")
    
    def _event_connect(self, err_code):
        if err_code == 0:
            print("로그인 성공")
        else:
            print("로그인 에러코드 : "+str(err_code))
        
        self.login_event_loop.exit()
    
    def comm_connect(self):
        self.dynamicCall("CommConnect()")
        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()
    
    def get_all_codes_names(self):
        ret = self.dynamicCall("GetCodeListByMarket(QString)", ["0"])
        kospi_code_list = ret.split(';')
        kospi_code_name_list = []

        for code in kospi_code_list:
            name = self.dynamicCall("GetMasterCodeName(QString)", [code])
            kospi_code_name_list.append(code + " : " + name)
        
        for item in kospi_code_name_list:
            print(item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    kiwoom = Kiwoom()
    kiwoom.comm_connect()
    kiwoom.get_all_codes_names()
    sys.exit(app.exec_())