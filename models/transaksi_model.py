# models/transaksi_model.py
from db import get_connection

def tambah_transaksi(id_barang, tanggal, jumlah, tipe):
    conn = get_connection()
    cursor = conn.cursor()

    # Tambah transaksi
    sql_transaksi = "INSERT INTO transaksi (id_barang, tanggal, jumlah, tipe) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql_transaksi, (id_barang, tanggal, jumlah, tipe))

    # Update stok barang
    if tipe == 'masuk':
        sql_update = "UPDATE barang SET stok = stok + %s WHERE id = %s"
    else:  # keluar
        sql_update = "UPDATE barang SET stok = stok - %s WHERE id = %s"

    cursor.execute(sql_update, (jumlah, id_barang))
    conn.commit()
    conn.close()

def get_all_transaksi():
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
        SELECT t.id, b.nama_barang, t.tanggal, t.jumlah, t.tipe
        FROM transaksi t
        JOIN barang b ON t.id_barang = b.id
        ORDER BY t.tanggal DESC
    """
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    return rows
