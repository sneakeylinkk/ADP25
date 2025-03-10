nama = str(input("Masukkan nama anda : "))
umur = int(input("Masukkan umur anda : "))
jenis_kelamin = str(input("Masukkan jenis kelamin (L/P) : "))

print ("\n3012 Padang-Jakarta")
print ("4015 Padang-Batam")
print ("4050 Padang-Bandung")
kode_maskapai = int(input("Silakan pilih kode maskapai (3012/4015/4050) : "))
if kode_maskapai == 3012 :
    Tujuan_Maskapai = ("Padang-Jakarta")
    Ekonomi = 800000
    Bisnis = 850000
    First = 900000
    print("Anda akan membeli tiket penerbangan dengan tujuan", Tujuan_Maskapai)
elif kode_maskapai == 4015 :
    Tujuan_Maskapai = ("Padang-Batam")
    Ekonomi = 500000
    Bisnis = 550000
    First = 700000
    print("Anda akan membeli tiket penerbangan dengan tujuan", Tujuan_Maskapai)
elif kode_maskapai == 4050 :
    Tujuan_Maskapai = ("Padang-Bandung")
    Ekonomi = 700000
    Bisnis = 750000
    First = 850000
    print("Anda akan membeli tiket penerbangan dengan tujuan", Tujuan_Maskapai)
else :
    print ("Maaf kode tidak valid")

print ("\n1. Ekonomi")
print ("2. Bisnis")
print ("3. First Class")
Kelas_maskapai = int(input("pilih kelas yang anda inginkan(1/2/3) : "))
if Kelas_maskapai == 1 :
    Kelas = "Ekonomi"
    Harga = Ekonomi
    print ("Kelas :", Kelas)
elif Kelas_maskapai == 2 :
    Kelas = "Bisnis"
    Harga = Bisnis
    print ("Kelas :", Kelas)
elif Kelas_maskapai == 3 :
     Kelas = "First Class"
     Harga = First
     print ("Kelas :", Kelas)
else : 
    print ("Maaf kelas yang anda pilih tidak valid")

Jumlah_tiket = int(input("\nMasukkan jumlah tiket : "))
if Jumlah_tiket > 3 :
    Total_harga = Jumlah_tiket * Harga
    Diskon = Total_harga * 0.2
    Total_harga = int(Total_harga - Diskon)
    print ("Total harga : Rp", Total_harga)
else :
    Total_harga = int(Jumlah_tiket * Harga)
    print ("Total harga : Rp", Total_harga)

print ("\n========= STRUK PEMBELIAN TIKET =========")
print ("\n |NAMA           : ", nama)
print (" |UMUR           : ", umur)
print (" |JENIS KELAMIN  : ", jenis_kelamin)
print ("\n=========================================")
print ("\n |KODE MASKAPAI  :", kode_maskapai, Tujuan_Maskapai)
print (" |JENIS MASKAPAI :", Kelas)
print (" |JUMLAH TIKET   :", Jumlah_tiket)
print (" |TOTAL HARGA    : Rp", Total_harga)
print ("\n================TERIMAKASIH==============")