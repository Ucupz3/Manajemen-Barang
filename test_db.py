import mysql.connector

print("🧩 Mencoba koneksi ke database...")

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db_inventaris"
    )
    print("✅ Koneksi berhasil!")
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    for (tbl,) in cursor.fetchall():
        print("📦 Tabel:", tbl)
    conn.close()

except mysql.connector.Error as err:
    print("❌ Terjadi error:", err)
