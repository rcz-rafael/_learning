# -*- coding: utf-8 -*-
# Define a codificação do arquivo como UTF-8

from PyQt5 import QtCore, QtGui, QtWidgets  # Importa as classes necessárias do PyQt5
from PyQt5.QtWidgets import QMessageBox     # Importa a classe QMessageBox para caixas de diálogo
import sqlite3  # Importa o módulo sqlite3 para trabalhar com banco de dados SQLite


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        # Define a interface do usuário (UI)
        Dialog.setObjectName("Cadastro")    # Define o nome do objeto tela
        Dialog.resize(1000, 720)    # Define o tamanho da tela
        # Cria um rótulo para exibir o título da aplicação
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 30, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btn_salvar = QtWidgets.QPushButton(Dialog)
        self.btn_salvar.setGeometry(QtCore.QRect(90, 352, 81, 31))
        self.btn_salvar.setObjectName("btn_salvar")
        self.btn_cancelar = QtWidgets.QPushButton(Dialog)
        self.btn_cancelar.setGeometry(QtCore.QRect(210, 352, 81, 31))
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 240, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 290, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(270, 290, 21, 16))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.input_name = QtWidgets.QLineEdit(Dialog)
        self.input_name.setGeometry(QtCore.QRect(90, 90, 331, 20))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(10)
        self.input_name.setFont(font)
        self.input_name.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 5px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}")
        self.input_name.setObjectName("input_name")
        self.input_endereco = QtWidgets.QLineEdit(Dialog)
        self.input_endereco.setGeometry(QtCore.QRect(90, 140, 331, 20))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(10)
        self.input_endereco.setFont(font)
        self.input_endereco.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 5px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}")
        self.input_endereco.setObjectName("input_endereco")
        self.input_email = QtWidgets.QLineEdit(Dialog)
        self.input_email.setGeometry(QtCore.QRect(90, 190, 331, 20))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(10)
        self.input_email.setFont(font)
        self.input_email.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 5px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}")
        self.input_email.setObjectName("input_email")
        self.input_telefone = QtWidgets.QLineEdit(Dialog)
        self.input_telefone.setGeometry(QtCore.QRect(90, 240, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(10)
        self.input_telefone.setFont(font)
        self.input_telefone.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 5px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}")
        self.input_telefone.setObjectName("input_telefone")
        self.input_cpf = QtWidgets.QLineEdit(Dialog)
        self.input_cpf.setGeometry(QtCore.QRect(90, 290, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(10)
        self.input_cpf.setFont(font)
        self.input_cpf.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 5px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}")
        self.input_cpf.setObjectName("input_cpf")
        self.input_rg = QtWidgets.QLineEdit(Dialog)
        self.input_rg.setGeometry(QtCore.QRect(300, 290, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(10)
        self.input_rg.setFont(font)
        self.input_rg.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 5px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}")
        self.input_rg.setObjectName("input_rg")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(30, 20, 451, 41))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.input_celular = QtWidgets.QLineEdit(Dialog)
        self.input_celular.setGeometry(QtCore.QRect(300, 240, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(10)
        self.input_celular.setFont(font)
        self.input_celular.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 5px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}")
        self.input_celular.setObjectName("input_celular")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(240, 240, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.btn_limpar = QtWidgets.QPushButton(Dialog)
        self.btn_limpar.setGeometry(QtCore.QRect(330, 352, 81, 31))
        self.btn_limpar.setObjectName("btn_limpar")
        self.btn_salvar.raise_()
        self.btn_cancelar.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.input_name.raise_()
        self.input_endereco.raise_()
        self.input_email.raise_()
        self.input_telefone.raise_()
        self.input_cpf.raise_()
        self.input_rg.raise_()
        self.tableWidget.raise_()
        self.label.raise_()
        self.input_celular.raise_()
        self.label_8.raise_()
        self.btn_limpar.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "CADASTRO DE USUÁRIO"))
        self.btn_salvar.setText(_translate("Dialog", "SALVAR"))
        self.btn_cancelar.setText(_translate("Dialog", "CANCELAR"))
        self.label_2.setText(_translate("Dialog", "NOME:"))
        self.label_3.setText(_translate("Dialog", "ENDEREÇO:"))
        self.label_4.setText(_translate("Dialog", "E-MAIL:"))
        self.label_5.setText(_translate("Dialog", "TELEFONE:"))
        self.label_6.setText(_translate("Dialog", "CPF:"))
        self.label_7.setText(_translate("Dialog", "RG:"))
        self.label_8.setText(_translate("Dialog", "CELULAR:"))
        self.btn_limpar.setText(_translate("Dialog", "LIMPAR"))

    def salvar_cadastro(self):
        nome = self.input_name.text()
        endereco = self.input_endereco.text()
        email = self.input_email.text()
        telefone = self.input_telefone.text()
        celular = self.input_celular.text()
        cpf = self.input_cpf.text()
        rg = self.input_rg.text()

        try:
            banco = sqlite3.connect("banco_cadastro.bd")
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS dados (nome text, endereco text, email text, telefone text, "
                           "celular text, cpf text, rg text)")
            cursor.execute("INSERT INTO dados (nome, endereco, email, telefone, celular, cpf, rg) "
                           "VALUES (?, ?, ?, ?, ?, ?, ?)", (nome, endereco, email, telefone, celular, cpf, rg))
            banco.commit()
            banco.close()

        except sqlite3.Error as erro:
            print("Erro ao salvar os dados: ", erro)

        # Caixa pop up
        msg = QMessageBox()
        msg.setWindowTitle("Salvar Conteúdo")
        msg.setText("Dados salvos com sucesso!")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.btn_salvar.clicked.connect(ui.salvar_cadastro)
    Dialog.show()
    sys.exit(app.exec_())