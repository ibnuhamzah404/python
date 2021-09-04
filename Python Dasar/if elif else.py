
def pembatas():
    print(100*"=")

nilai = int(input("Masukan nilai kamu\t: "))


if  90 <= nilai <= 100:
    hasil = "A"
elif 80 <= nilai < 90:
    hasil = "B+"
elif 70 <= nilai < 80:
    hasil = "B-"
elif 60 <= nilai <= 70:
    hasil = "C"
else:
    hasil = "Maaf anda tidak lulus:("


print("Nilai Kamu : %s" %hasil)

pembatas()

umur = int(input("masukan umur kamu : "))

if umur is 18:
    print("kamu sudah remaja")
elif umur is not 18:
    print("kamu belum remaja")

pembatas()





