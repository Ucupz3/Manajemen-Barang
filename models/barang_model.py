# models/barang_model.py
from db import get_connection

# -------------------------------
# FUNGSI CRUD UNTUK TABEL BARANG
# -------------------------------

def get_all_barang():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM barang ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def tambah_barang(nama_barang, kategori, stok, harga):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO barang (nama_barang, kategori, stok, harga) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nama_barang, kategori, stok, harga))
    conn.commit()
    conn.close()

def ubah_barang(id_barang, nama_barang, kategori, stok, harga):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE barang SET nama_barang=%s, kategori=%s, stok=%s, harga=%s WHERE id=%s"
    cursor.execute(sql, (nama_barang, kategori, stok, harga, id_barang))
    conn.commit()
    conn.close()

def hapus_barang(id_barang):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM barang WHERE id=%s"
    cursor.execute(sql, (id_barang,))
    conn.commit()
    conn.close()
