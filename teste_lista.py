from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(452, 509)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # noinspection PyArgumentList
        self.additem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.add_it())
        self.additem_pushButton.setGeometry(QtCore.QRect(20, 62, 81, 31))
        self.additem_pushButton.setObjectName("additem_pushButton")
        self.deleteitem_pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.delete_it())
        self.deleteitem_pushButton_2.setGeometry(QtCore.QRect(130, 62, 81, 31))
        self.deleteitem_pushButton_2.setObjectName("deleteitem_pushButton_2")
        self.clear_pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clear_it())
        self.clear_pushButton_3.setGeometry(QtCore.QRect(240, 62, 81, 31))
        self.clear_pushButton_3.setObjectName("clear_pushButton_3")
        self.adicionar_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.adicionar_lineEdit.setGeometry(QtCore.QRect(20, 19, 411, 31))
        self.adicionar_lineEdit.setObjectName("adicionar_lineEdit")
        self.minhalista_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.minhalista_listWidget.setGeometry(QtCore.QRect(20, 110, 411, 351))
        self.minhalista_listWidget.setObjectName("minhalista_listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 452, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Adicionar item para a lista
    def add_it(self):
        # Pegar o item da caixa
        item = self.adicionar_lineEdit.text()

        # Adicionar item a lista
        self.minhalista_listWidget.addItem(item)

        # Limpar a caixa
        self.adicionar_lineEdit.setText("")

    # Deletar item
    def delete_it(self):
        # Identificar a linha selecionada ou linha atual
        clicked = self.minhalista_listWidget.currentRow()
        # Informar a linha selecionada
        # self.adicionar_lineEdit.setText(str(clicked))

        # Deletar a linha selecionada
        self.minhalista_listWidget.takeItem(clicked)

    # Limpar item
    def clear_it(self):
        self.minhalista_listWidget.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.additem_pushButton.setText(_translate("MainWindow", "Adicionar"))
        self.deleteitem_pushButton_2.setText(_translate("MainWindow", "Deletar"))
        self.clear_pushButton_3.setText(_translate("MainWindow", "Limpar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
