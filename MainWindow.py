from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1037, 735)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.Categoria = QtWidgets.QWidget()
        self.Categoria.setObjectName("Categoria")
        self.formLayoutWidget = QtWidgets.QWidget(self.Categoria)
        self.formLayoutWidget.setGeometry(QtCore.QRect(80, 10, 331, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.insert_id = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.insert_id.setObjectName("insert_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.insert_id)
        self.label_descrizione = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_descrizione.setObjectName("label_descrizione")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_descrizione)
        self.insert_descrizione = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.insert_descrizione.setObjectName("insert_descrizione")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.insert_descrizione)
        self.label_prezzo_giornaliero = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_prezzo_giornaliero.setObjectName("label_prezzo_giornaliero")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_prezzo_giornaliero)
        self.insert_prezzo_giornaliero = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.insert_prezzo_giornaliero.setObjectName("insert_prezzo_giornaliero")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.insert_prezzo_giornaliero)
        self.label_prezzo_settimanale = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_prezzo_settimanale.setObjectName("label_prezzo_settimanale")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_prezzo_settimanale)
        self.insert_prezzo_settimanale = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.insert_prezzo_settimanale.setObjectName("insert_prezzo_settimanale")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.insert_prezzo_settimanale)
        self.label_prezzo_mensile = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_prezzo_mensile.setObjectName("label_prezzo_mensile")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_prezzo_mensile)
        self.insert_prezzo_mensile = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.insert_prezzo_mensile.setObjectName("insert_prezzo_mensile")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.insert_prezzo_mensile)
        self.label_id = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_id.setObjectName("label_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_id)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Categoria)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(530, 10, 171, 205))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_aggiungi = QtWidgets.QToolButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_aggiungi.sizePolicy().hasHeightForWidth())
        self.btn_aggiungi.setSizePolicy(sizePolicy)
        self.btn_aggiungi.setCheckable(False)
        self.btn_aggiungi.setObjectName("btn_aggiungi")
        self.verticalLayout.addWidget(self.btn_aggiungi)
        self.btn_rimuovi = QtWidgets.QToolButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_rimuovi.sizePolicy().hasHeightForWidth())
        self.btn_rimuovi.setSizePolicy(sizePolicy)
        self.btn_rimuovi.setCheckable(False)
        self.btn_rimuovi.setObjectName("btn_rimuovi")
        self.verticalLayout.addWidget(self.btn_rimuovi)
        self.btn_modifica = QtWidgets.QToolButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_modifica.sizePolicy().hasHeightForWidth())
        self.btn_modifica.setSizePolicy(sizePolicy)
        self.btn_modifica.setCheckable(False)
        self.btn_modifica.setObjectName("btn_modifica")
        self.verticalLayout.addWidget(self.btn_modifica)
        self.btn_mostra = QtWidgets.QToolButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mostra.sizePolicy().hasHeightForWidth())
        self.btn_mostra.setSizePolicy(sizePolicy)
        self.btn_mostra.setCheckable(False)
        self.btn_mostra.setObjectName("btn_mostra")
        self.verticalLayout.addWidget(self.btn_mostra)
        self.btn_clear = QtWidgets.QPushButton(self.Categoria)
        self.btn_clear.setGeometry(QtCore.QRect(320, 160, 93, 28))
        self.btn_clear.setObjectName("btn_clear")
        self.insert_cerca = QtWidgets.QLineEdit(self.Categoria)
        self.insert_cerca.setGeometry(QtCore.QRect(10, 250, 161, 22))
        self.insert_cerca.setObjectName("insert_cerca")
        self.btn_cerca = QtWidgets.QPushButton(self.Categoria)
        self.btn_cerca.setGeometry(QtCore.QRect(80, 280, 93, 28))
        self.btn_cerca.setObjectName("btn_cerca")
        self.table_categoria = QtWidgets.QTableWidget(self.Categoria)
        self.table_categoria.setGeometry(QtCore.QRect(190, 250, 801, 241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_categoria.sizePolicy().hasHeightForWidth())
        self.table_categoria.setSizePolicy(sizePolicy)
        self.table_categoria.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_categoria.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_categoria.setColumnCount(0)
        self.table_categoria.setObjectName("table_categoria")
        self.table_categoria.setRowCount(0)
        self.table_categoria.verticalHeader().setVisible(False)
        self.btn_aggiorna_categoria = QtWidgets.QPushButton(self.Categoria)
        self.btn_aggiorna_categoria.setGeometry(QtCore.QRect(900, 500, 93, 28))
        self.btn_aggiorna_categoria.setObjectName("btn_aggiorna_categoria")
        self.tabWidget.addTab(self.Categoria, "")
        self.Auto = QtWidgets.QWidget()
        self.Auto.setObjectName("Auto")
        self.btn_cerca_auto = QtWidgets.QPushButton(self.Auto)
        self.btn_cerca_auto.setGeometry(QtCore.QRect(80, 280, 93, 28))
        self.btn_cerca_auto.setObjectName("btn_cerca_auto")
        self.table_auto = QtWidgets.QTableWidget(self.Auto)
        self.table_auto.setGeometry(QtCore.QRect(190, 250, 801, 241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_auto.sizePolicy().hasHeightForWidth())
        self.table_auto.setSizePolicy(sizePolicy)
        self.table_auto.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_auto.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_auto.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_auto.setColumnCount(0)
        self.table_auto.setObjectName("table_auto")
        self.table_auto.setRowCount(0)
        self.table_auto.verticalHeader().setVisible(False)
        self.btn_aggiorna_auto = QtWidgets.QPushButton(self.Auto)
        self.btn_aggiorna_auto.setGeometry(QtCore.QRect(900, 500, 93, 28))
        self.btn_aggiorna_auto.setObjectName("btn_aggiorna_auto")
        self.insert_cerca_auto = QtWidgets.QLineEdit(self.Auto)
        self.insert_cerca_auto.setGeometry(QtCore.QRect(10, 250, 161, 22))
        self.insert_cerca_auto.setObjectName("insert_cerca_auto")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.Auto)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(80, 10, 331, 198))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.insert_id_auto = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.insert_id_auto.setObjectName("insert_id_auto")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.insert_id_auto)
        self.label_marca_auto = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_marca_auto.setObjectName("label_marca_auto")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_marca_auto)
        self.insert_marca_auto = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.insert_marca_auto.setObjectName("insert_marca_auto")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.insert_marca_auto)
        self.label_modello_auto = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_modello_auto.setObjectName("label_modello_auto")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_modello_auto)
        self.insert_modello_auto = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.insert_modello_auto.setObjectName("insert_modello_auto")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.insert_modello_auto)
        self.label_colore_auto = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_colore_auto.setObjectName("label_colore_auto")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_colore_auto)
        self.insert_colore_auto = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.insert_colore_auto.setObjectName("insert_colore_auto")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.insert_colore_auto)
        self.label_targa_auto = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_targa_auto.setObjectName("label_targa_auto")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_targa_auto)
        self.insert_targa_auto = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.insert_targa_auto.setObjectName("insert_targa_auto")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.insert_targa_auto)
        self.label_id_auto = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_id_auto.setObjectName("label_id_auto")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_id_auto)
        self.label_data_acquisto_auto = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_data_acquisto_auto.setObjectName("label_data_acquisto_auto")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_data_acquisto_auto)
        self.label_categoria_auto = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_categoria_auto.setObjectName("label_categoria_auto")
        self.formLayout_5.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_categoria_auto)
        self.insert_categoria_auto = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.insert_categoria_auto.setObjectName("insert_categoria_auto")
        self.formLayout_5.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.insert_categoria_auto)
        self.insert_data_acquisto_auto = QtWidgets.QDateEdit(self.formLayoutWidget_3)
        self.insert_data_acquisto_auto.setObjectName("insert_data_acquisto_auto")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.insert_data_acquisto_auto)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Auto)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(530, 10, 171, 205))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btn_aggiungi_auto = QtWidgets.QToolButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_aggiungi_auto.sizePolicy().hasHeightForWidth())
        self.btn_aggiungi_auto.setSizePolicy(sizePolicy)
        self.btn_aggiungi_auto.setCheckable(False)
        self.btn_aggiungi_auto.setObjectName("btn_aggiungi_auto")
        self.verticalLayout_6.addWidget(self.btn_aggiungi_auto)
        self.btn_rimuovi_auto = QtWidgets.QToolButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_rimuovi_auto.sizePolicy().hasHeightForWidth())
        self.btn_rimuovi_auto.setSizePolicy(sizePolicy)
        self.btn_rimuovi_auto.setCheckable(False)
        self.btn_rimuovi_auto.setObjectName("btn_rimuovi_auto")
        self.verticalLayout_6.addWidget(self.btn_rimuovi_auto)
        self.btn_modifica_auto = QtWidgets.QToolButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_modifica_auto.sizePolicy().hasHeightForWidth())
        self.btn_modifica_auto.setSizePolicy(sizePolicy)
        self.btn_modifica_auto.setCheckable(False)
        self.btn_modifica_auto.setObjectName("btn_modifica_auto")
        self.verticalLayout_6.addWidget(self.btn_modifica_auto)
        self.btn_mostra_auto = QtWidgets.QToolButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mostra_auto.sizePolicy().hasHeightForWidth())
        self.btn_mostra_auto.setSizePolicy(sizePolicy)
        self.btn_mostra_auto.setCheckable(False)
        self.btn_mostra_auto.setObjectName("btn_mostra_auto")
        self.verticalLayout_6.addWidget(self.btn_mostra_auto)
        self.btn_clear_auto = QtWidgets.QPushButton(self.Auto)
        self.btn_clear_auto.setGeometry(QtCore.QRect(320, 210, 93, 28))
        self.btn_clear_auto.setObjectName("btn_clear_auto")
        self.insert_cerca_auto_categoria = QtWidgets.QLineEdit(self.Auto)
        self.insert_cerca_auto_categoria.setGeometry(QtCore.QRect(10, 340, 161, 22))
        self.insert_cerca_auto_categoria.setObjectName("insert_cerca_auto_categoria")
        self.btn_cerca_auto_categoria = QtWidgets.QPushButton(self.Auto)
        self.btn_cerca_auto_categoria.setGeometry(QtCore.QRect(80, 370, 93, 28))
        self.btn_cerca_auto_categoria.setObjectName("btn_cerca_auto_categoria")
        self.tabWidget.addTab(self.Auto, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(80, 10, 331, 171))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.insert_id_cliente = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.insert_id_cliente.setObjectName("insert_id_cliente")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.insert_id_cliente)
        self.label_descrizione_2 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_descrizione_2.setObjectName("label_descrizione_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_descrizione_2)
        self.insert_nome_cliente = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.insert_nome_cliente.setObjectName("insert_nome_cliente")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.insert_nome_cliente)
        self.label_prezzo_giornaliero_2 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_prezzo_giornaliero_2.setObjectName("label_prezzo_giornaliero_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_prezzo_giornaliero_2)
        self.insert_cognome_cliente = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.insert_cognome_cliente.setObjectName("insert_cognome_cliente")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.insert_cognome_cliente)
        self.label_prezzo_settimanale_2 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_prezzo_settimanale_2.setObjectName("label_prezzo_settimanale_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_prezzo_settimanale_2)
        self.label_prezzo_mensile_2 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_prezzo_mensile_2.setObjectName("label_prezzo_mensile_2")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_prezzo_mensile_2)
        self.insert_indirizzo_cliente = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.insert_indirizzo_cliente.setObjectName("insert_indirizzo_cliente")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.insert_indirizzo_cliente)
        self.label_id_2 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_id_2.setObjectName("label_id_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_id_2)
        self.insert_data_nascita_cliente = QtWidgets.QDateEdit(self.formLayoutWidget_4)
        self.insert_data_nascita_cliente.setObjectName("insert_data_nascita_cliente")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.insert_data_nascita_cliente)
        self.label = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label)
        self.insert_carta_credito_cliente = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.insert_carta_credito_cliente.setObjectName("insert_carta_credito_cliente")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.insert_carta_credito_cliente)
        self.btn_clear_cliente = QtWidgets.QPushButton(self.tab)
        self.btn_clear_cliente.setGeometry(QtCore.QRect(320, 190, 93, 28))
        self.btn_clear_cliente.setObjectName("btn_clear_cliente")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(530, 10, 171, 205))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_aggiungi_cliente = QtWidgets.QToolButton(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_aggiungi_cliente.sizePolicy().hasHeightForWidth())
        self.btn_aggiungi_cliente.setSizePolicy(sizePolicy)
        self.btn_aggiungi_cliente.setCheckable(False)
        self.btn_aggiungi_cliente.setObjectName("btn_aggiungi_cliente")
        self.verticalLayout_3.addWidget(self.btn_aggiungi_cliente)
        self.btn_rimuovi_cliente = QtWidgets.QToolButton(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_rimuovi_cliente.sizePolicy().hasHeightForWidth())
        self.btn_rimuovi_cliente.setSizePolicy(sizePolicy)
        self.btn_rimuovi_cliente.setCheckable(False)
        self.btn_rimuovi_cliente.setObjectName("btn_rimuovi_cliente")
        self.verticalLayout_3.addWidget(self.btn_rimuovi_cliente)
        self.btn_modifica_cliente = QtWidgets.QToolButton(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_modifica_cliente.sizePolicy().hasHeightForWidth())
        self.btn_modifica_cliente.setSizePolicy(sizePolicy)
        self.btn_modifica_cliente.setCheckable(False)
        self.btn_modifica_cliente.setObjectName("btn_modifica_cliente")
        self.verticalLayout_3.addWidget(self.btn_modifica_cliente)
        self.btn_mostra_cliente = QtWidgets.QToolButton(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mostra_cliente.sizePolicy().hasHeightForWidth())
        self.btn_mostra_cliente.setSizePolicy(sizePolicy)
        self.btn_mostra_cliente.setCheckable(False)
        self.btn_mostra_cliente.setObjectName("btn_mostra_cliente")
        self.verticalLayout_3.addWidget(self.btn_mostra_cliente)
        self.insert_cerca_cliente = QtWidgets.QLineEdit(self.tab)
        self.insert_cerca_cliente.setGeometry(QtCore.QRect(10, 250, 161, 22))
        self.insert_cerca_cliente.setObjectName("insert_cerca_cliente")
        self.btn_cerca_cliente = QtWidgets.QPushButton(self.tab)
        self.btn_cerca_cliente.setGeometry(QtCore.QRect(80, 280, 93, 28))
        self.btn_cerca_cliente.setObjectName("btn_cerca_cliente")
        self.table_cliente = QtWidgets.QTableWidget(self.tab)
        self.table_cliente.setGeometry(QtCore.QRect(190, 250, 801, 241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_cliente.sizePolicy().hasHeightForWidth())
        self.table_cliente.setSizePolicy(sizePolicy)
        self.table_cliente.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_cliente.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_cliente.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_cliente.setColumnCount(0)
        self.table_cliente.setObjectName("table_cliente")
        self.table_cliente.setRowCount(0)
        self.table_cliente.verticalHeader().setVisible(False)
        self.btn_aggiorna_cliente = QtWidgets.QPushButton(self.tab)
        self.btn_aggiorna_cliente.setGeometry(QtCore.QRect(900, 500, 93, 28))
        self.btn_aggiorna_cliente.setObjectName("btn_aggiorna_cliente")
        self.tabWidget.addTab(self.tab, "")
        self.Noleggio = QtWidgets.QWidget()
        self.Noleggio.setObjectName("Noleggio")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.Noleggio)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(40, 30, 401, 201))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formNoleggio = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formNoleggio.setContentsMargins(0, 0, 0, 0)
        self.formNoleggio.setObjectName("formNoleggio")
        self.label_nome = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_nome.setObjectName("label_nome")
        self.formNoleggio.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_nome)
        self.insert_nome = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.insert_nome.setObjectName("insert_nome")
        self.formNoleggio.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.insert_nome)
        self.label_cognome = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_cognome.setObjectName("label_cognome")
        self.formNoleggio.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_cognome)
        self.insert_cognome = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.insert_cognome.setObjectName("insert_cognome")
        self.formNoleggio.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.insert_cognome)
        self.label_data_nascita = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_data_nascita.setObjectName("label_data_nascita")
        self.formNoleggio.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_data_nascita)
        self.insert_data_nascita = QtWidgets.QDateEdit(self.formLayoutWidget_2)
        self.insert_data_nascita.setObjectName("insert_data_nascita")
        self.formNoleggio.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.insert_data_nascita)
        self.label_indirizzo = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_indirizzo.setObjectName("label_indirizzo")
        self.formNoleggio.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_indirizzo)
        self.insert_indirizzo = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.insert_indirizzo.setObjectName("insert_indirizzo")
        self.formNoleggio.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.insert_indirizzo)
        self.label_targa = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_targa.setObjectName("label_targa")
        self.formNoleggio.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_targa)
        self.insert_targa = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.insert_targa.setObjectName("insert_targa")
        self.formNoleggio.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.insert_targa)
        self.label_data_inizio = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_data_inizio.setObjectName("label_data_inizio")
        self.formNoleggio.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_data_inizio)
        self.label_data_fine = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_data_fine.setObjectName("label_data_fine")
        self.formNoleggio.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_data_fine)
        self.insert_data_inizio = QtWidgets.QDateEdit(self.formLayoutWidget_2)
        self.insert_data_inizio.setObjectName("insert_data_inizio")
        self.formNoleggio.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.insert_data_inizio)
        self.insert_data_fine = QtWidgets.QDateEdit(self.formLayoutWidget_2)
        self.insert_data_fine.setObjectName("insert_data_fine")
        self.formNoleggio.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.insert_data_fine)
        self.btn_conferma_noleggio = QtWidgets.QPushButton(self.Noleggio)
        self.btn_conferma_noleggio.setGeometry(QtCore.QRect(350, 240, 93, 28))
        self.btn_conferma_noleggio.setObjectName("btn_conferma_noleggio")
        self.btn_costo_noleggio = QtWidgets.QPushButton(self.Noleggio)
        self.btn_costo_noleggio.setGeometry(QtCore.QRect(240, 240, 93, 28))
        self.btn_costo_noleggio.setObjectName("btn_costo_noleggio")
        self.label_calcola_costo = QtWidgets.QLabel(self.Noleggio)
        self.label_calcola_costo.setGeometry(QtCore.QRect(40, 310, 401, 31))
        self.label_calcola_costo.setText("")
        self.label_calcola_costo.setObjectName("label_calcola_costo")
        self.tabWidget.addTab(self.Noleggio, "")
        self.Cronologia = QtWidgets.QWidget()
        self.Cronologia.setObjectName("Cronologia")
        self.table_cronologia = QtWidgets.QTableWidget(self.Cronologia)
        self.table_cronologia.setGeometry(QtCore.QRect(20, 20, 959, 451))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_cronologia.sizePolicy().hasHeightForWidth())
        self.table_cronologia.setSizePolicy(sizePolicy)
        self.table_cronologia.setMouseTracking(False)
        self.table_cronologia.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.table_cronologia.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.table_cronologia.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_cronologia.setFrameShadow(QtWidgets.QFrame.Plain)
        self.table_cronologia.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_cronologia.setGridStyle(QtCore.Qt.SolidLine)
        self.table_cronologia.setColumnCount(0)
        self.table_cronologia.setObjectName("table_cronologia")
        self.table_cronologia.setRowCount(0)
        self.table_cronologia.horizontalHeader().setVisible(False)
        self.table_cronologia.horizontalHeader().setSortIndicatorShown(False)
        self.table_cronologia.verticalHeader().setVisible(False)
        self.btn_aggiorna_cronologia = QtWidgets.QPushButton(self.Cronologia)
        self.btn_aggiorna_cronologia.setGeometry(QtCore.QRect(890, 480, 93, 28))
        self.btn_aggiorna_cronologia.setObjectName("btn_aggiorna_cronologia")
        self.btn_mostra_cronologia = QtWidgets.QPushButton(self.Cronologia)
        self.btn_mostra_cronologia.setGeometry(QtCore.QRect(770, 480, 93, 28))
        self.btn_mostra_cronologia.setObjectName("btn_mostra_cronologia")
        self.tabWidget.addTab(self.Cronologia, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1037, 26))
        self.menubar.setObjectName("menubar")
        self.menuAutonoleggio = QtWidgets.QMenu(self.menubar)
        self.menuAutonoleggio.setObjectName("menuAutonoleggio")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuAutonoleggio.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_descrizione.setText(_translate("MainWindow", "Descrizione"))
        self.label_prezzo_giornaliero.setText(_translate("MainWindow", "Prezzo giornaliero"))
        self.label_prezzo_settimanale.setText(_translate("MainWindow", "Prezzo settimanale"))
        self.label_prezzo_mensile.setText(_translate("MainWindow", "Prezzo mensile"))
        self.label_id.setText(_translate("MainWindow", "Id"))
        self.btn_aggiungi.setText(_translate("MainWindow", "Aggiungi"))
        self.btn_rimuovi.setText(_translate("MainWindow", "Rimuovi"))
        self.btn_modifica.setText(_translate("MainWindow", "Modifica"))
        self.btn_mostra.setText(_translate("MainWindow", "Mostra tutto"))
        self.btn_clear.setText(_translate("MainWindow", "Clear"))
        self.insert_cerca.setPlaceholderText(_translate("MainWindow", "Cerca categoria..."))
        self.btn_cerca.setText(_translate("MainWindow", "Cerca"))
        self.table_categoria.setSortingEnabled(False)
        self.btn_aggiorna_categoria.setText(_translate("MainWindow", "Aggiorna"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Categoria), _translate("MainWindow", "Categoria"))
        self.btn_cerca_auto.setText(_translate("MainWindow", "Cerca"))
        self.table_auto.setSortingEnabled(False)
        self.btn_aggiorna_auto.setText(_translate("MainWindow", "Aggiorna"))
        self.insert_cerca_auto.setPlaceholderText(_translate("MainWindow", "Cerca targa..."))
        self.label_marca_auto.setText(_translate("MainWindow", "Marca"))
        self.label_modello_auto.setText(_translate("MainWindow", "Modello"))
        self.label_colore_auto.setText(_translate("MainWindow", "Colore"))
        self.label_targa_auto.setText(_translate("MainWindow", "Targa"))
        self.label_id_auto.setText(_translate("MainWindow", "Id"))
        self.label_data_acquisto_auto.setText(_translate("MainWindow", "Data acquisto"))
        self.label_categoria_auto.setText(_translate("MainWindow", "Categoria"))
        self.insert_data_acquisto_auto.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.btn_aggiungi_auto.setText(_translate("MainWindow", "Aggiungi"))
        self.btn_rimuovi_auto.setText(_translate("MainWindow", "Rimuovi"))
        self.btn_modifica_auto.setText(_translate("MainWindow", "Modifica"))
        self.btn_mostra_auto.setText(_translate("MainWindow", "Mostra tutto"))
        self.btn_clear_auto.setText(_translate("MainWindow", "Clear"))
        self.insert_cerca_auto_categoria.setPlaceholderText(_translate("MainWindow", "Cerca per categoria..."))
        self.btn_cerca_auto_categoria.setText(_translate("MainWindow", "Cerca"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Auto), _translate("MainWindow", "Auto"))
        self.label_descrizione_2.setText(_translate("MainWindow", "Nome"))
        self.label_prezzo_giornaliero_2.setText(_translate("MainWindow", "Cognome"))
        self.label_prezzo_settimanale_2.setText(_translate("MainWindow", "Data di nascita"))
        self.label_prezzo_mensile_2.setText(_translate("MainWindow", "Indirizzo"))
        self.label_id_2.setText(_translate("MainWindow", "Id"))
        self.label.setText(_translate("MainWindow", "Carta di credito"))
        self.btn_clear_cliente.setText(_translate("MainWindow", "Clear"))
        self.btn_aggiungi_cliente.setText(_translate("MainWindow", "Aggiungi"))
        self.btn_rimuovi_cliente.setText(_translate("MainWindow", "Rimuovi"))
        self.btn_modifica_cliente.setText(_translate("MainWindow", "Modifica"))
        self.btn_mostra_cliente.setText(_translate("MainWindow", "Mostra tutto"))
        self.insert_cerca_cliente.setPlaceholderText(_translate("MainWindow", "Cerca cliente..."))
        self.btn_cerca_cliente.setText(_translate("MainWindow", "Cerca"))
        self.table_cliente.setSortingEnabled(False)
        self.btn_aggiorna_cliente.setText(_translate("MainWindow", "Aggiorna"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Clienti"))
        self.label_nome.setText(_translate("MainWindow", "Nome*"))
        self.label_cognome.setText(_translate("MainWindow", "Cognome*"))
        self.label_data_nascita.setText(_translate("MainWindow", "Data di nascita*(AAAA/MM/GG)"))
        self.insert_data_nascita.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.label_indirizzo.setText(_translate("MainWindow", "Indirizzo*"))
        self.label_targa.setText(_translate("MainWindow", "Targa*"))
        self.label_data_inizio.setText(_translate("MainWindow", "Data inizio noleggio*"))
        self.label_data_fine.setText(_translate("MainWindow", "Data fine noleggio*"))
        self.insert_data_inizio.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.insert_data_fine.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.btn_conferma_noleggio.setText(_translate("MainWindow", "Conferma"))
        self.btn_costo_noleggio.setText(_translate("MainWindow", "Calcola costo"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Noleggio), _translate("MainWindow", "Noleggio"))
        self.table_cronologia.setSortingEnabled(True)
        self.btn_aggiorna_cronologia.setText(_translate("MainWindow", "Aggiorna"))
        self.btn_mostra_cronologia.setText(_translate("MainWindow", "Mostra tutto"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Cronologia), _translate("MainWindow", "Cronologia"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
