import sys
import math
from datetime import datetime
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QStandardItemModel, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QErrorMessage, QMessageBox, QInputDialog, QLineEdit, QWidget, QTableView, QTableWidgetItem, QHeaderView
import mysql.connector
from MainWindow import Ui_MainWindow

try:
    from PyQt5.QtWinExtras import QtWin
    myappid = 'marconi.autonoleggio.app.version'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)    
except ImportError:
    pass

# Connessione al db
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="autonoleggio"
)

app = QtWidgets.QApplication(sys.argv)
mycursor = mydb.cursor()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Autonoleggio")
        self.setWindowIcon(QtGui.QIcon("app_icon.ico"))
#Categoria
        self.btn_aggiungi.clicked.connect(self.AggiungiCategoria)
        self.btn_rimuovi.clicked.connect(self.RimuoviCategoria)
        self.btn_modifica.clicked.connect(self.ModificaCategoria)
        self.btn_cerca.clicked.connect(self.CercaCategoria)
        self.btn_mostra.clicked.connect(self.MostraListaCategoria)
        self.btn_aggiorna_categoria.clicked.connect(self.AggiornaTableCategoria)
        self.btn_clear.clicked.connect(self.Clear)
#Auto
        self.btn_aggiungi_auto.clicked.connect(self.AggiungiAuto)
        self.btn_rimuovi_auto.clicked.connect(self.RimuoviAuto)
        self.btn_modifica_auto.clicked.connect(self.ModificaAuto)
        self.btn_cerca_auto.clicked.connect(self.CercaAuto)
        self.btn_cerca_auto_categoria.clicked.connect(self.CercaCategoriaAuto)
        self.btn_mostra_auto.clicked.connect(self.MostraListaAuto)
        self.btn_aggiorna_auto.clicked.connect(self.AggiornaTableAuto)
        self.btn_clear_auto.clicked.connect(self.ClearAuto)
#Cliente
        self.btn_aggiungi_cliente.clicked.connect(self.AggiungiCliente)
        self.btn_rimuovi_cliente.clicked.connect(self.RimuoviCliente)
        self.btn_modifica_cliente.clicked.connect(self.ModificaCliente)
        self.btn_cerca_cliente.clicked.connect(self.CercaCliente)
        self.btn_mostra_cliente.clicked.connect(self.MostraListaCliente)
        self.btn_aggiorna_cliente.clicked.connect(self.AggiornaTableCliente)
        self.btn_clear_cliente.clicked.connect(self.ClearCliente)
#Noleggio
        self.btn_conferma_noleggio.clicked.connect(self.ConfermaNoleggio)
        self.btn_costo_noleggio.clicked.connect(self.CalcolaCosto)
#Cronologia
        self.btn_mostra_cronologia.clicked.connect(self.MostraCronologia)
        self.btn_aggiorna_cronologia.clicked.connect(self.AggiornaCronologia)


### CATEGORIA ###

 #Aggiungi categoria, FUNZIONA
    def AggiungiCategoria(self):
        mycursor.execute("""insert into categoria (id, descrizione, prezzo_giornaliero, prezzo_settimanale, prezzo_mensile) 
                                values(%s, %s, %s, %s, %s)""", (None,
                                                            self.insert_descrizione.text(),
                                                            self.insert_prezzo_giornaliero.text(),
                                                            self.insert_prezzo_settimanale.text(),
                                                            self.insert_prezzo_mensile.text())
                        )
        
        mydb.commit()
        QMessageBox.information(self, "Avviso", "Categoria inserita correttamente")

        self.insert_id.setText(" ")
        self.insert_descrizione.setText(" ")
        self.insert_prezzo_giornaliero.setText(" ")
        self.insert_prezzo_settimanale.setText(" ")
        self.insert_prezzo_mensile.setText(" ")

#Rimuovi categoria data la descrizione, FUNZIONA
    def RimuoviCategoria(self, inputDescrizione):
        inputDescrizione, okPressed = QInputDialog.getText(self, "Rimuovi", "Inserisci descrizione categoria", QLineEdit.Normal, "")
        if okPressed:
            Delete="delete from categoria where descrizione = '%s'" %(inputDescrizione)
            mycursor.execute(Delete)
            mydb.commit()
            QMessageBox.information(self, "Avviso", "Categoria rimossa")

#Modifica categoria dato l'id, FUNZIONA
    def ModificaCategoria(self):
        mycursor.execute("update categoria set descrizione='%s', prezzo_giornaliero='%s', prezzo_settimanale='%s', prezzo_mensile='%s' where id='%s'"
        %(self.insert_descrizione.text(), self.insert_prezzo_giornaliero.text(), self.insert_prezzo_settimanale.text(), self.insert_prezzo_mensile.text(), self.insert_id.text()))
        mydb.commit()

        QMessageBox.information(self, "Avviso", "Categoria modificata")

        self.insert_id.setText(" ")
        self.insert_descrizione.setText(" ")
        self.insert_prezzo_giornaliero.setText(" ")
        self.insert_prezzo_settimanale.setText(" ")
        self.insert_prezzo_mensile.setText(" ")

#Cerca una categoria specifica utilizzando la descrizione (viene visualizzata nella tabella), FUNZIONA
    def CercaCategoria(self):
        mycursor.execute("select * from categoria where descrizione = '%s'" %(self.insert_cerca.text()))
        risultato = mycursor.fetchone()
        if risultato == None:
            errore = QMessageBox()
            errore.setIcon(QMessageBox.Critical)
            errore.setText("Inserire un valore valido.")
            errore.setWindowTitle("Errore")
            errore.exec_()
        else:
            self.table_categoria.setColumnCount(5)
            self.table_categoria.setRowCount(1)
            self.table_categoria.setHorizontalHeaderLabels(["Id", "Descrizione", "Prezzo giorn.", "Prezzo sett.", "Prezzo mensile"])
            self.table_categoria.horizontalHeader().setStretchLastSection(True) 
            self.table_categoria.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            rowcount = 0
            for col, value in enumerate(risultato):
                    item = QTableWidgetItem()
                    item.setData(QtCore.Qt.DisplayRole, value)
                    self.table_categoria.setItem(rowcount, col, item)

#Mostra tutte le categorie nella tabella, FUNZIONA
    def MostraListaCategoria(self):
        mycursor.execute("select * from categoria order by id")
        risultati = mycursor.fetchall()
        self.table_categoria.setRowCount(len(risultati))
        self.table_categoria.setColumnCount(5)
        self.table_categoria.setHorizontalHeaderLabels(["Id", "Descrizione", "Prezzo giorn.", "Prezzo sett.", "Prezzo mensile"])
        self.table_categoria.horizontalHeader().setStretchLastSection(True) 
        self.table_categoria.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        rowcount = 0
        for rowcount, sqlRow in enumerate(risultati):
            for col, value in enumerate(sqlRow):
                item = QTableWidgetItem()
                item.setData(QtCore.Qt.DisplayRole, value)
                self.table_categoria.setItem(rowcount, col, item)

#Aggiorna i valori di table_categoria, FUNZIONA
    def AggiornaTableCategoria(self):
        while (self.table_categoria.rowCount() > 0):
            self.table_categoria.removeRow(0)
        self.MostraListaCategoria()
            

 #Clear i campi da compilare in categoria, FUNZIONA
    def Clear(self):
        self.insert_id.setText(" ")
        self.insert_descrizione.setText(" ")
        self.insert_prezzo_giornaliero.setText(" ")
        self.insert_prezzo_settimanale.setText(" ")
        self.insert_prezzo_mensile.setText(" ")


### AUTO ###

#Aggiungi un'auto, FUNZIONA
    def AggiungiAuto(self):
            data_acquisto_auto = self.insert_data_acquisto_auto.date().toPyDate()
            formatted_data_acquisto_auto = data_acquisto_auto.strftime('%Y-%m-%d')
            mycursor.execute("""insert into auto (id, marca, modello, colore, targa, data_acquisto, id_categoria)
                                    values(%s, %s, %s, %s, %s, %s, (select id from categoria where descrizione = %s))""", 
                                                                (None,
                                                                self.insert_marca_auto.text(),
                                                                self.insert_modello_auto.text(),
                                                                self.insert_colore_auto.text(),
                                                                self.insert_targa_auto.text(),
                                                                formatted_data_acquisto_auto,
                                                                self.insert_categoria_auto.text())
                            )
            
            mydb.commit()
            QMessageBox.information(self, "Avviso", "Auto inserita correttamente")

            self.insert_id_auto.setText(" ")
            self.insert_marca_auto.setText(" ")
            self.insert_modello_auto.setText(" ")
            self.insert_colore_auto.setText(" ")
            self.insert_targa_auto.setText(" ")
            self.insert_categoria_auto.setText(" ")

#Rimuovi un'auto data la targa, FUNZIONA
    def RimuoviAuto(self):
        inputTarga, okPressed = QInputDialog.getText(self, "Rimuovi", "Inserisci targa auto", QLineEdit.Normal, "")
        if okPressed:
            Delete="delete from auto where targa = '%s'" %(inputTarga)
            mycursor.execute(Delete)
            mydb.commit()
            QMessageBox.information(self, "Avviso", "Auto rimossa")

#Modifica un'auto dato l'id, FUNZIONA 
    def ModificaAuto(self):
        data_acquisto_auto = self.insert_data_acquisto_auto.date().toPyDate()
        formatted_data_acquisto_auto = data_acquisto_auto.strftime('%Y-%m-%d')
        mycursor.execute("update auto set marca='%s', modello='%s', colore='%s', targa='%s', data_acquisto='%s', id_categoria=(select id from categoria where descrizione = '%s') where id='%s'"
        %(self.insert_marca_auto.text(),self.insert_modello_auto.text(),self.insert_colore_auto.text(),self.insert_targa_auto.text(),formatted_data_acquisto_auto,self.insert_categoria_auto.text(), self.insert_id_auto.text()))

        mydb.commit()
        QMessageBox.information(self, "Avviso", "Auto modificata")
        self.insert_id_auto.setText(" ")
        self.insert_marca_auto.setText(" ")
        self.insert_modello_auto.setText(" ")
        self.insert_colore_auto.setText(" ")
        self.insert_targa_auto.setText(" ")
        self.insert_categoria_auto.setText(" ")

#Cerca un'auto inserendo la targa, FUNZIONA
    def CercaAuto(self):
        mycursor.execute("select * from auto where targa = '%s'" %(self.insert_cerca_auto.text()))
        risultato = mycursor.fetchone()
        if risultato == None:
            errore = QMessageBox()
            errore.setIcon(QMessageBox.Critical)
            errore.setText("Inserire un valore valido.")
            errore.setWindowTitle("Errore")
            errore.exec_()
        else:
            self.table_auto.setColumnCount(7)
            self.table_auto.setRowCount(1)
            self.table_auto.setHorizontalHeaderLabels(["Id", "Marca", "Modello", "Colore", "Targa", "Data acquisto", "Categoria"])
            self.table_auto.horizontalHeader().setStretchLastSection(True) 
            self.table_auto.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            rowcount = 0
            for col, value in enumerate(risultato):
                if col==5:
                    formatted_value = value.strftime("%Y-%m-%d")
                    qtDate = QtCore.QDate.fromString(formatted_value, 'yyyy-MM-dd')
                    item = QTableWidgetItem()
                    item.setData(QtCore.Qt.DisplayRole, formatted_value)
                    self.table_auto.setItem(rowcount, col, item)
                else:    
                    item = QTableWidgetItem()
                    item.setData(QtCore.Qt.DisplayRole, value)
                    self.table_auto.setItem(rowcount, col, item)

#Cerca tutte le auto appartenenti alla categoria scelta e le mostra nella tabella, FUNZIONA
    def CercaCategoriaAuto(self):
        mycursor.execute("select * from auto where id_categoria = (select id from categoria where descrizione = '%s')" %(self.insert_cerca_auto_categoria.text()))
        risultato = mycursor.fetchall()
        if risultato == None:
            errore = QMessageBox()
            errore.setIcon(QMessageBox.Critical)
            errore.setText("Inserire un valore valido.")
            errore.setWindowTitle("Errore")
            errore.exec_()
        else:
            self.table_auto.setColumnCount(7)
            self.table_auto.setRowCount(len(risultato))
            self.table_auto.setHorizontalHeaderLabels(["Id", "Marca", "Modello", "Colore", "Targa", "Data acquisto", "Categoria"])
            self.table_auto.horizontalHeader().setStretchLastSection(True) 
            self.table_auto.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            rowcount = 0
            for rowcount, sqlRow in enumerate(risultato):
                for col, value in enumerate(sqlRow):
                    if col==5:
                        formatted_value = value.strftime("%Y-%m-%d")
                        qtDate = QtCore.QDate.fromString(formatted_value, 'yyyy-MM-dd')
                        item = QTableWidgetItem()
                        item.setData(QtCore.Qt.DisplayRole, formatted_value)
                        self.table_auto.setItem(rowcount, col, item)
                    else:    
                        item = QTableWidgetItem()
                        item.setData(QtCore.Qt.DisplayRole, value)
                        self.table_auto.setItem(rowcount, col, item)

#Mostra tutte le auto presenti nella tabella, FUNZIONA 
    def MostraListaAuto(self):
        mycursor.execute("select auto.id, marca, modello, colore, targa, data_acquisto, descrizione from auto join categoria on categoria.id = auto.id_categoria order by id")
        risultati = mycursor.fetchall()
        self.table_auto.setRowCount(len(risultati))
        self.table_auto.setColumnCount(7)
        self.table_auto.setHorizontalHeaderLabels(["Id", "Marca", "Modello", "Colore", "Targa", "Data acquisto", "Categoria"])
        self.table_auto.horizontalHeader().setStretchLastSection(True) 
        self.table_auto.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        rowcount = 0
        for rowcount, sqlRow in enumerate(risultati):
            for col, value in enumerate(sqlRow):
                if col==5:
                    formatted_value = value.strftime("%Y-%m-%d")
                    qtDate = QtCore.QDate.fromString(formatted_value, 'yyyy-MM-dd')
                    item = QTableWidgetItem()
                    item.setData(QtCore.Qt.DisplayRole, formatted_value)
                    self.table_auto.setItem(rowcount, col, item)
                else:
                    item = QTableWidgetItem()
                    item.setData(QtCore.Qt.DisplayRole, value)
                    self.table_auto.setItem(rowcount, col, item)

#Aggiorna i valori di table_auto, FUNZIONA
    def AggiornaTableAuto(self):
        while (self.table_auto.rowCount() > 0):
            self.table_auto.removeRow(0)
        self.MostraListaAuto()

#Clear i campi da compilare in auto, FUNZIONA
    def ClearAuto(self):
        self.insert_id_auto.setText(" ")
        self.insert_marca_auto.setText(" ")
        self.insert_modello_auto.setText(" ")
        self.insert_colore_auto.setText(" ")
        self.insert_targa_auto.setText(" ")
        self.insert_categoria_auto.setText(" ")


### CLIENTE ###

#Aggiungi un cliente, FUNZIONA
    def AggiungiCliente(self):
        data_nascita = self.insert_data_nascita_cliente.date().toPyDate()
        formatted_data_nascita = data_nascita.strftime('%Y-%m-%d')
        mycursor.execute("""insert into cliente (id, nome, cognome, data_nascita, indirizzo, numero_carta_di_credito) 
                                values(%s, %s, %s, %s, %s, %s)""", (None,
                                                            self.insert_nome_cliente.text(),
                                                            self.insert_cognome_cliente.text(),
                                                            formatted_data_nascita,
                                                            self.insert_indirizzo_cliente.text(),
                                                            self.insert_carta_credito_cliente.text())
                        )
        
        mydb.commit()
        QMessageBox.information(self, "Avviso", "Cliente inserito correttamente")

        self.insert_id_cliente.setText(" ")
        self.insert_nome_cliente.setText(" ")
        self.insert_cognome_cliente.setText(" ")
        self.insert_indirizzo_cliente.setText(" ")
        self.insert_carta_credito_cliente.setText(" ")

#Rimuovi un cliente dato l'ID, FUNZIONA
    def RimuoviCliente(self):
        inputCliente, okPressed = QInputDialog.getText(self, "Rimuovi", "Inserisci id cliente", QLineEdit.Normal, "")
        if okPressed:
            Delete="delete from cliente where id = '%s'" %(inputCliente)
            mycursor.execute(Delete)
            mydb.commit()
            QMessageBox.information(self, "Avviso", "Cliente rimosso")

#Modifica cliente dato l'id, FUNZIONA
    def ModificaCliente(self):
        data_nascita = self.insert_data_nascita_cliente.date().toPyDate()
        formatted_data_nascita = data_nascita.strftime('%Y-%m-%d')
        mycursor.execute("update cliente set nome='%s', cognome='%s', data_nascita='%s', indirizzo='%s', numero_carta_di_credito='%s' where id=%s"
        %(self.insert_nome_cliente.text(), self.insert_cognome_cliente.text(), formatted_data_nascita, self.insert_indirizzo_cliente.text(),self.insert_carta_credito_cliente.text(),self.insert_id_cliente.text()))
        
        mydb.commit()
        QMessageBox.information(self, "Avviso", "Cliente modificato")

        self.insert_id_cliente.setText(" ")
        self.insert_nome_cliente.setText(" ")
        self.insert_cognome_cliente.setText(" ")
        self.insert_indirizzo_cliente.setText(" ")
        self.insert_carta_credito_cliente.setText(" ")

#Cerca un cliente dato l'id, FUNZIONA
    def CercaCliente(self):
        nominativo = self.insert_cerca_cliente.text().split()
        mycursor.execute("select * from cliente where nome = '%s' and cognome = '%s'" %(nominativo[0], nominativo[1]))
        risultato = mycursor.fetchone()
        if risultato == None:
            errore = QMessageBox()
            errore.setIcon(QMessageBox.Critical)
            errore.setText("Inserire un valore valido.")
            errore.setWindowTitle("Errore")
            errore.exec_()
        else:
            self.table_cliente.setColumnCount(6)
            self.table_cliente.setRowCount(1)
            self.table_cliente.setHorizontalHeaderLabels(["Id", "Nome", "Cognome", "Data di nascita", "Indirizzo", "Carta di credito"])
            self.table_cliente.horizontalHeader().setStretchLastSection(True) 
            self.table_cliente.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            rowcount = 0
            for col, value in enumerate(risultato):
                if col==3:
                    formatted_value = value.strftime("%Y-%m-%d")
                    qtDate = QtCore.QDate.fromString(formatted_value, 'yyyy-MM-dd')
                    item = QTableWidgetItem()
                    item.setData(QtCore.Qt.DisplayRole, formatted_value)
                    self.table_cliente.setItem(rowcount, col, item)
                else:
                    item = QTableWidgetItem()
                    item.setData(QtCore.Qt.DisplayRole, value)
                    self.table_cliente.setItem(rowcount, col, item)

#Mostra nella tabella tutti i clienti registrati, FUNZIONA
    def MostraListaCliente(self):
        mycursor.execute("select id, nome, cognome, data_nascita, indirizzo, numero_carta_di_credito from cliente")
        risultati = mycursor.fetchall()
        self.table_cliente.setRowCount(len(risultati))
        self.table_cliente.setColumnCount(6)
        self.table_cliente.setHorizontalHeaderLabels(["Id", "Nome", "Cognome", "Data di nascita", "Indirizzo", "Carta di credito"])
        self.table_cliente.horizontalHeader().setStretchLastSection(True) 
        self.table_cliente.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        rowcount = 0
        for rowcount, sqlRow in enumerate(risultati):
            for col, value in enumerate(sqlRow):
                if col==3:
                    formatted_value = value.strftime("%Y-%m-%d")
                    qtDate = QtCore.QDate.fromString(formatted_value, 'yyyy-MM-dd')
                    item = QTableWidgetItem()
                    item.setData(QtCore.Qt.DisplayRole, formatted_value)
                    self.table_cliente.setItem(rowcount, col, item)
                else:    
                    item = QTableWidgetItem()
                    item.setData(QtCore.Qt.DisplayRole, value)
                    self.table_cliente.setItem(rowcount, col, item)

#Aggiorna la tabella degli utenti, FUNZIONA
    def AggiornaTableCliente(self):
        while (self.table_cliente.rowCount() > 0):
            self.table_cliente.removeRow(0)
        self.MostraListaCliente()

#Fa il clear dei campi da compilare in cliente, FUNZIONA
    def ClearCliente(self):
        self.insert_id_cliente.setText(" ")
        self.insert_nome_cliente.setText(" ")
        self.insert_cognome_cliente.setText(" ")
        self.insert_indirizzo_cliente.setText(" ")
        self.insert_carta_credito_cliente.setText(" ")

### NOLEGGIO ###

#Aggiunge un noleggio prendendo l'id_cliente dal nome, cognome, data_nascita e indirizzo e l'id_categoria dalla targa, FUNZIONA
    def ConfermaNoleggio(self):
        data_inizio = self.insert_data_inizio.date().toPyDate()
        formatted_data_inizio = data_inizio.strftime('%Y-%m-%d')
        data_fine = self.insert_data_fine.date().toPyDate()
        formatted_data_fine = data_fine.strftime('%Y-%m-%d')
        data_nascita = self.insert_data_nascita.date().toPyDate()
        formatted_data_nascita = data_nascita.strftime('%Y-%m-%d')
        mycursor.execute("""insert into noleggio (data_inizio, data_fine, id_cliente, id_auto)
        values (%s, %s, (select id from cliente where nome=%s and cognome=%s and data_nascita=%s and indirizzo=%s), (select id from auto where targa=%s))""",
        (formatted_data_inizio, formatted_data_fine, self.insert_nome.text(), self.insert_cognome.text(), formatted_data_nascita, self.insert_indirizzo.text(), self.insert_targa.text() ))
        mydb.commit()

        QMessageBox.information(self, "Avviso", "Noleggio aggiunto")

#Calcola e mostra il costo di un noleggio dati la targa della macchina da noleggiare e la data di inizio e fine noleggio, FUNZIONA
    def CalcolaCosto(self):
        mycursor.execute("select prezzo_giornaliero, prezzo_settimanale, prezzo_mensile from categoria where id=(select id_categoria from auto where targa='%s')"%(self.insert_targa.text()))
        query_prezzi = mycursor.fetchall()
        prezzo_giornaliero = (query_prezzi[0][0])
        prezzo_settimanale = (query_prezzi[0][1])
        prezzo_mensile = (query_prezzi[0][2])
        data_inizio = self.insert_data_inizio.date().toPyDate()
        data_fine = self.insert_data_fine.date().toPyDate()
        durata_noleggio = (data_fine - data_inizio).days

        if durata_noleggio%30 == 0:
            prezzo_noleggio = prezzo_mensile * (durata_noleggio/30)
        elif durata_noleggio%7 == 0:
            prezzo_noleggio = prezzo_settimanale * (durata_noleggio/7)
        elif durata_noleggio > 30:
            numero_mesi = math.floor(durata_noleggio/30)
            prezzo_solo_mesi = numero_mesi * prezzo_mensile   
            durata_senza_mesi = durata_noleggio - (numero_mesi * 30)

            if durata_senza_mesi >= 7:
                numero_settimane = math.floor(durata_senza_mesi/7)
                prezzo_solo_settimane = numero_settimane * prezzo_settimanale
                durata_solo_giorni = durata_senza_mesi - (numero_settimane * 7)
                prezzo_solo_giorni = durata_solo_giorni * prezzo_giornaliero
                prezzo_noleggio = prezzo_solo_giorni + prezzo_solo_settimane + prezzo_solo_mesi
            else:
                prezzo_solo_giorni = durata_senza_mesi * prezzo_giornaliero
                prezzo_noleggio = prezzo_solo_giorni + prezzo_solo_mesi

        elif durata_noleggio < 30 and durata_noleggio > 7:
            numero_settimane = math.floor(durata_noleggio/7)
            prezzo_solo_settimane = numero_settimane * prezzo_settimanale
            durata_solo_giorni = durata_noleggio - (numero_settimane * 7)
            prezzo_solo_giorni = durata_solo_giorni * prezzo_giornaliero
            prezzo_noleggio = prezzo_solo_giorni + prezzo_solo_settimane
    
        else:
            prezzo_solo_giorni = durata_noleggio * prezzo_giornaliero
            prezzo_noleggio = prezzo_solo_giorni

        self.label_calcola_costo.setFont(QFont('Arial', 10))
        self.label_calcola_costo.setText("Il costo del noleggio è di €" + str(prezzo_noleggio))

### CRONOLOGIA ###

#Mostra in una tabella la lista dei noleggi effettuati, FUNZIONA
    def MostraCronologia(self):
        mycursor.execute("select noleggio.id, data_inizio, data_fine, cliente.nome, cliente.cognome, auto.targa from noleggio join cliente on noleggio.id_cliente = cliente.id join auto on noleggio.id_auto = auto.id")
        risultati = mycursor.fetchall()
        self.table_cronologia.setRowCount(len(risultati))
        self.table_cronologia.setColumnCount(6)
        self.table_cronologia.horizontalHeader().setVisible(True)
        self.table_cronologia.setHorizontalHeaderLabels(["Id", "Data inizio", "Data fine", "Nome", "Cognome", "Targa"])
        self.table_cronologia.horizontalHeader().setStretchLastSection(True) 
        self.table_cronologia.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        rowcount = 0
        for rowcount, sqlRow in enumerate(risultati):
            for col, value in enumerate(sqlRow):
                if col==1 or col==2:
                    formatted_value = value.strftime("%Y-%m-%d")
                    qtDate = QtCore.QDate.fromString(formatted_value, 'yyyy-MM-dd')
                    item = QTableWidgetItem()
                    item.setData(QtCore.Qt.DisplayRole, formatted_value)
                    self.table_cronologia.setItem(rowcount, col, item)
                else:
                    item = QTableWidgetItem()
                    item.setData(QtCore.Qt.DisplayRole, value)
                    self.table_cronologia.setItem(rowcount, col, item)
    
#Aggiorna la tabella cronologia, FUNZIONA
    def AggiornaCronologia(self):
        while (self.table_cronologia.rowCount() > 0):
            self.table_cronologia.removeRow(0)
        self.MostraCronologia()

def main():
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()