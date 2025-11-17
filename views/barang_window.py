# views/barang_window.py
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem,
    QPushButton, QLineEdit, QLabel, QMessageBox
)
from PyQt6.QtCore import Qt
from models.barang_model import get_all_barang, tambah_barang, ubah_barang, hapus_barang


class BarangWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kelola Barang")
        self.resize(700, 500)

        # --- Layout utama ---
        layout = QVBoxLayout()
        form_layout = QHBoxLayout()

        # --- Input field ---
        self.input_nama = QLineEdit()
        self.input_kategori = QLineEdit()
        self.input_stok = QLineEdit()
        self.input_harga = QLineEdit()

        form_layout.addWidget(QLabel("Nama:"))
        form_layout.addWidget(self.input_nama)
        form_layout.addWidget(QLabel("Kategori:"))
        form_layout.addWidget(self.input_kategori)
        form_layout.addWidget(QLabel("Stok:"))
        form_layout.addWidget(self.input_stok)
        form_layout.addWidget(QLabel("Harga:"))
        form_layout.addWidget(self.input_harga)

        layout.addLayout(form_layout)

        # --- Tombol ---
        button_layout = QHBoxLayout()
        self.btn_tambah = QPushButton("Tambah")
        self.btn_ubah = QPushButton("Ubah")
        self.btn_hapus = QPushButton("Hapus")
        self.btn_refresh = QPushButton("Refresh")

        button_layout.addWidget(self.btn_tambah)
        button_layout.addWidget(self.btn_ubah)
        button_layout.addWidget(self.btn_hapus)
        button_layout.addWidget(self.btn_refresh)
        layout.addLayout(button_layout)

        # --- Tabel Barang ---
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Nama Barang", "Kategori", "Stok", "Harga"])
        layout.addWidget(self.table)

        self.setLayout(layout)

        # --- Hubungkan tombol ke fungsi ---
        self.btn_tambah.clicked.connect(self.tambah_data)
        self.btn_ubah.clicked.connect(self.ubah_data)
        self.btn_hapus.clicked.connect(self.hapus_data)
        self.btn_refresh.clicked.connect(self.load_data)
        self.table.cellClicked.connect(self.isi_form_dari_tabel)

        # --- Load awal ---
        self.load_data()

    # ======================================================
    # FUNGSI CRUD
    # ======================================================

    def load_data(self):
        self.table.setRowCount(0)
        data = get_all_barang()
        for row_idx, row_data in enumerate(data):
            self.table.insertRow(row_idx)
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(row_data["id"])))
            self.table.setItem(row_idx, 1, QTableWidgetItem(row_data["nama_barang"]))
            self.table.setItem(row_idx, 2, QTableWidgetItem(row_data["kategori"]))
            self.table.setItem(row_idx, 3, QTableWidgetItem(str(row_data["stok"])))
            self.table.setItem(row_idx, 4, QTableWidgetItem(str(row_data["harga"])))

    def tambah_data(self):
        try:
            tambah_barang(
                self.input_nama.text(),
                self.input_kategori.text(),
                int(self.input_stok.text()),
                float(self.input_harga.text())
            )
            QMessageBox.information(self, "Sukses", "Barang berhasil ditambahkan.")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal menambah barang: {e}")

    def ubah_data(self):
        try:
            selected_row = self.table.currentRow()
            if selected_row == -1:
                QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin diubah dulu.")
                return
            id_barang = int(self.table.item(selected_row, 0).text())

            ubah_barang(
                id_barang,
                self.input_nama.text(),
                self.input_kategori.text(),
                int(self.input_stok.text()),
                float(self.input_harga.text())
            )
            QMessageBox.information(self, "Sukses", "Barang berhasil diubah.")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal mengubah barang: {e}")

    def hapus_data(self):
        try:
            selected_row = self.table.currentRow()
            if selected_row == -1:
                QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin dihapus dulu.")
                return
            id_barang = int(self.table.item(selected_row, 0).text())

            hapus_barang(id_barang)
            QMessageBox.information(self, "Sukses", "Barang berhasil dihapus.")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal menghapus barang: {e}")

    # ======================================================
    # FUNGSI BANTUAN
    # ======================================================

    def isi_form_dari_tabel(self, row, column):
        self.input_nama.setText(self.table.item(row, 1).text())
        self.input_kategori.setText(self.table.item(row, 2).text())
        self.input_stok.setText(self.table.item(row, 3).text())
        self.input_harga.setText(self.table.item(row, 4).text())

    def clear_form(self):
        self.input_nama.clear()
        self.input_kategori.clear()
        self.input_stok.clear()
        self.input_harga.clear()
