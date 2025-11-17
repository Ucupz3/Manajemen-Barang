import pymysql

def get_connection():
    print("🧩 (db.py) Memulai koneksi MySQL (pymysql)...")

    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="",  # kosong karena MySQL-mu tanpa password
            database="db_inventaris",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor  # 🔹 ubah jadi DictCursor
        )
        print("✅ (db.py) Koneksi MySQL berhasil!")
        return conn

    except Exception as e:
        print("❌ (db.py) Gagal koneksi:", e)
        return None
