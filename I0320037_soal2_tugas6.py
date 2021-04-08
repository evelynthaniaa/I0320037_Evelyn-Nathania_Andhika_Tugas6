#memasukkan data
n = int(input("Banyaknya data :"))
data = []
jumlah = 0

#menghitung rata-rata data
for i in range(0,n):
    x = int(input("Masukkan data ke-%d:" %(i+1)))
    data.append(x)
    jumlah += data[i]
    rata2 = jumlah / n
print("Rata-rata = %0.2f" %rata2)