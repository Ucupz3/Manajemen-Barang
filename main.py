from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox
)
from PyQt6.QtCore import Qt
import sys
import traceback

# Import window dari views
from views.barang_window import BarangWindow
from views.transaksi_window import TransaksiWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📦 Aplikasi Inventaris Barang")
        self.setGeometry(200, 100, 420, 300)
        self.setStyleSheet("""
            QPushButton {
                padding: 20px;
                font-size: 14px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #e6f2ff;
            }
        """)

        # Layout utama
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        btn_barang = QPushButton("📋 Kelola Barang")
        btn_transaksi = QPushButton("💰 Kelola Transaksi")

        layout.addWidget(btn_barang)
        layout.addWidget(btn_transaksi)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Event tombol
        btn_barang.clicked.connect(self.open_barang_window)
        btn_transaksi.clicked.connect(self.open_transaksi_window)

    # ======================================================
    # FUNGSI UNTUK MEMBUKA WINDOW
    # ======================================================

    def open_barang_window(self):
        try:
            print("🔹 Membuka modul BarangWindow...")
            self.barang_window = BarangWindow()
            self.barang_window.show()
        except Exception as e:
            print("❌ Gagal membuka BarangWindow:", e)
            QMessageBox.critical(self, "Error", f"Gagal membuka modul Barang:\n{e}")

    def open_transaksi_window(self):
        try:
            print("🔹 Membuka modul TransaksiWindow...")
            self.transaksi_window = TransaksiWindow()
            self.transaksi_window.show()
        except Exception as e:
            print("❌ Gagal membuka TransaksiWindow:", e)
            QMessageBox.critical(self, "Error", f"Gagal membuka modul Transaksi:\n{e}")


# ======================================================
# ENTRY POINT PROGRAM
# ======================================================
if __name__ == "__main__":
    print("🚀 Aplikasi Inventaris Barang berjalan...")

    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()

        print("🕐 GUI aktif — aplikasi menunggu input pengguna...")
        sys.exit(app.exec())

    except Exception as e:
        print("❌ Terjadi error fatal:")
        traceback.print_exc()
        input("Tekan ENTER untuk menutup...")
