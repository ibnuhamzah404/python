import pymysql
import os

db = pymysql.connect(
  host="localhost",
  user="root",
  password="",
  database="pythoncrud"
)

def insert_data(db):
    try:
        print("\n\t" , 5* "==", "INSERT DATA MAHASISWA" , 5*"==")
        nim = int(input("\n\t Masukan nim mahasiswa\t\t: "))
        nama = input("\n\t Masukan nama mahasiswa\t\t: ")
        jurusan = input("\n\t Masukan jurusan mahasiswa\t: ")
        gender = input("\n\t Masukan gender\t\t\t: ")
    except ValueError:
        print("\n\t Anda memasukan variable , silakan input ulang kembali!!")
    else:
        value = (nim, nama, jurusan, gender)
        cursor = db.cursor()
        sql = "INSERT INTO mahasiswa (`nim`, `nama`, `jurusan`, `gender`) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, value)
        db.commit()
        print("\n\t", "{} Data berhasil disimpan".format(cursor.rowcount))
    finally:
        cursor.close()


def show_data(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM mahasiswa")
    rows = cursor.fetchall()

    no = 1

    for row in rows:
        print("\n\t" , 5*"===", "DATA MAHASISWA KE-",no, 5*"===")
        print("\n\t ID \t\t: ", +row[0])
        print("\t NIM \t\t: ", + row[1])
        print("\t NAMA \t\t: ", row[2])
        print("\t JURUSAN \t: ",row[3])
        print("\t GENDER \t: ", row[4])
        print("\n\t", 9*"======")
        no += 1

    print("\n\t Jumblah banyaknya mahasiswa : ", no-1)
    cursor.close()

def update_data(db):
    try:

        print("\n\t",5*"=====", "UPDATE DATA MAHASISWA", 5 * "=====")
        id = int(input("\n\t  Masukan id mahasiswa yang ingin diupdate\t: "))
        jurusan = input("\n\t   Masukan jurusan mahasiswa yang baru\t\t: ")
    except ValueError:
        print("anda memasukan variable!!")
    except ZeroDivisionError:
        print("anda memasukan angka 0!!")
    else:
        cursor = db.cursor()
        sql = "UPDATE mahasiswa SET jurusan = %s WHERE id = %s"
        val = (jurusan, id)
        cursor.execute(sql, val)
        db.commit()
        print("\n\t", "{} Data berhasil disimpan".format(cursor.rowcount))
    finally:
        cursor.close()

def delete_data(db):
    try:
        print("\n\t", 5 * "===", "UPDATE DATA MAHASISWA", 5 * "===")
        id = int(input("\n\tMasukan id mahasiswa yang ingin didelete\t: "))
        nim = input("\n\tMasukan delete nim mahasiswa\t\t: ")
    except ValueError:
        print("anda memasukan variable!!")
    except ZeroDivisionError:
        print("anda memasukan angka 0!!")
    else:
        cursor = db.cursor()
        sql = "DELETE FROM mahasiswa WHERE id = %s AND nim = %s"
        val = (id, nim)
        cursor.execute(sql, val)
        db.commit()
        print("{} data diubah".format(cursor.rowcount))
    finally:
        cursor.close()


def many_data(db):
    try:
        id1 = int(input("delete data dari id ke : "))
        id2 = int(input("samapai id ke : "))
    except ValueError:
        print("anda memasukan variable!!")
    except ZeroDivisionError:
        print("anda memasukan angka 0!!")
    else:
        cursor = db.cursor()
        sql = "DELETE FROM mahasiswa WHERE id BETWEEN %s AND %s"
        val = (id1, id2)
        cursor.execute(sql, val)
        db.commit()
        print("{} data diubah".format(cursor.rowcount))
    finally:
        cursor.close()


def search_data(db):
    try:
        id = int(input("\n\tMasukan id mahasiswa yang ingin dicari\t: "))
    except ValueError:
        print("anda memasukan variable!!")
    except ZeroDivisionError:
        print("anda memasukan angka 0!!")
    else:

        cursor = db.cursor()
        sql = "SELECT * FROM mahasiswa WHERE id = %s"
        cursor.execute(sql, id)
        rows = cursor.fetchall()
        record = cursor.fetchall()

        for row in record:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            print("Join Date = ", row[2])
            print("Salary  = ", row[3], "\n")

    no = 1

    for row in rows:
        print("\n\t" , 5*"===", "DATA MAHASISWA KE-",no, 5*"===")
        print("\n\t ID \t\t: ", +row[0])
        print("\t NIM \t\t: ", + row[1])
        print("\t NAMA \t\t: ", row[2])
        print("\t JURUSAN \t: ",row[3])
        print("\t GENDER \t: ", row[4])
        print("\n\t", 9*"======")
        no += 1

    cursor.close()


def reset_increment(db):
    cursor = db.cursor()
    cursor.execute( "SET @num = 0;")
    cursor.execute("UPDATE mahasiswa SET id = @num := (@num+1);")
    cursor.execute("ALTER TABLE mahasiswa AUTO_INCREMENT =1;")

def jumblah_data(db):
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(id) FROM mahasiswa;")
    print("{} banyak data : ".format(cursor.rowcount))

def show_menu(db):
    print("\n\t=== APLIKASI DATABASE PYTHON ===")
    print("\n\t1. Insert Data")
    print("\t2. Tampilkan Data")
    print("\t3. Update Data")
    print("\t4. Hapus Data")
    print("\t5. Cari Data")
    print("\t6. Delete Many Data")
    print("\t7. Reset Auto Increment")
    print("\t0. Keluar")
    print("\n\t------------------")
    menu = input("\n\tPilih menu> ")

    os.system("cls")

    if menu == "1":
        insert_data(db)
    elif menu == "2":
        show_data(db)
    elif menu == "3":
        update_data(db)
    elif menu == "4":
        delete_data(db)
    elif menu == "5":
        search_data(db)
    elif menu == "6":
        many_data(db)
    elif menu == "7":
        reset_increment(db)
    elif menu == "8":
        jumblah_data(db)
    elif menu == "0":
        exit()
    else:
        print("Menu salah!")

if __name__ == "__main__":
  while(True):
    show_menu(db)

