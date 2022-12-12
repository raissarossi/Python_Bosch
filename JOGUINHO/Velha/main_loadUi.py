from PyQt5 import uic, QtWidgets

def funcao():
    print("teste")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    
    janela = uic.loadUi('jogo_da_velha.ui')
    
    janela.show()
    app.exec()