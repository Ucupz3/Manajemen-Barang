from PyQt6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout, QTableWidget,
    QTableWidgetItem, QPushButton, QLineEdit, QComboBox, QDateEdit
)
from PyQt6.QtCore import QDate
from models.transaksi_model import get_all_transaksi, tambah_transaksi
from models.barang_model import get_all_barang


class TransaksiWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kelola Transaksi")
        self.setGeometry(300, 200, 700, 400)

        layout = QVBoxLayout()

        # Judul
        layout.addWidget(QLabel("📦 Kelola Transaksi Barang"))

        # --- Input Form ---
        form_layout = QHBoxLayout()

        # Pilih Barang
        self.cmb_barang = QComboBox()
        for barang in get_all_barang():
            self.cmb_barang.addItem(barang["nama_barang"], barang["id"])  # ✅ pakai dict key

        # Tanggal
        self.date_input = QDateEdit()
        self.date_input.setDate(QDate.currentDate())

        # Jumlah
        self.input_jumlah = QLineEdit()
        self.input_jumlah.setPlaceholderText("Jumlah")

        # Tipe (masuk/keluar)
        self.cmb_tipe = QComboBox()
        self.cmb_tipe.addItems(["masuk", "keluar"])

        # Tombol tambah
        btn_tambah = QPushButton("Tambah Transaksi")
        btn_tambah.clicked.connect(self.tambah_transaksi)

        # Masukkan ke layout
        form_layout.addWidget(self.cmb_barang)
        form_layout.addWidget(self.date_input)
        form_layout.addWidget(self.input_jumlah)
        form_layout.addWidget(self.cmb_tipe)
        form_layout.addWidget(btn_tambah)

        layout.addLayout(form_layout)

        # --- Tabel Data Transaksi ---
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Barang", "Tanggal", "Jumlah", "Tipe"])
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        data = get_all_transaksi()
        self.table.setRowCount(len(data))
        for row_index, row_data in enumerate(data):
            # row_data bisa berupa dict
            self.table.setItem(row_index, 0, QTableWidgetItem(str(row_data["id"])))
            self.table.setItem(row_index, 1, QTableWidgetItem(str(row_data["nama_barang"])))
            self.table.setItem(row_index, 2, QTableWidgetItem(str(row_data["tanggal"])))
            self.table.setItem(row_index, 3, QTableWidgetItem(str(row_data["jumlah"])))
            self.table.setItem(row_index, 4, QTableWidgetItem(str(row_data["tipe"])))

    def tambah_transaksi(self):
        try:
            id_barang = self.cmb_barang.currentData()
            tanggal = self.date_input.date().toString("yyyy-MM-dd")
            jumlah = int(self.input_jumlah.text())
            tipe = self.cmb_tipe.currentText()

            tambah_transaksi(id_barang, tanggal, jumlah, tipe)
            self.load_data()
            self.input_jumlah.clear()
        except Exception as e:
            print("❌ Gagal tambah transaksi:", e)
