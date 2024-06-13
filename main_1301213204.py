#Import library untuk dapat membaca file eksternal
import csv

#Fungsi untuk mendapatkan nama penjualan dengan penjualan tertinggi dalam seminggu
def tertinggi(dict_jualan):

  #Inisialisasi variabel list
  data_perminggu = []
  nama_penjual = []

  #Perulangan untuk mendapatkan jumlah penjualan dalam satu minggu per orang
  for key, value in dict_jualan.items():
    total_penjualan = int(value['senin']) + int(value['selasa']) + int(value['rabu']) + int(value['kamis']) + int(value['jumat'])
    data_perminggu.append(total_penjualan)
    nama_penjual.append(value['nama'])

  #Mendapatkan nilai tertinggi dari jumlah penjualan
  max_jual = max(data_perminggu)
  max_index = data_perminggu.index(max_jual)
  return nama_penjual[max_index]

#Fungsi untuk mendapatkan rata-rata penjualan dalam satu minggu per orang
def report(dict_jualan):

  #Inisialisasi variabel list
  rata_penjual = []

  #Perulangan untuk mendapatkan rata-rata per orang
  for key, value in dict_jualan.items():
    total_penjualan = int(value['senin']) + int(value['selasa']) + int(value['rabu']) + int(value['kamis']) + int(value['jumat'])
    rata_rata = total_penjualan / 5
    rata_penjual.append(rata_rata)
  return rata_penjual

#Inisialisasi variabel
semua_data = []

#Membuka file tekstubes.txt dan memasukkannya ke dalam list
with open('tekstubes.txt', newline = '') as data_penjualan:
  data_reader = csv.reader(data_penjualan, delimiter = '\t')
  for jual in data_reader:
    semua_data.append(jual)

#Inisialisasi 'judul' sebagai key untuk dictionary
judul = ['nama', 'senin', 'selasa', 'rabu', 'kamis', 'jumat']

#Inisialisasi dictionary
dict_penjualan = {}

#Inisialisasi penanda uruta
i = 1

#Perulangan untuk memasukkan data dalam list ke dalam dictionary
for data_jual in semua_data:
  dict_penjualan_temp = dict(zip(judul, data_jual))
  dict_penjualan[i] = dict_penjualan_temp
  i += 1

#Memanggil fungsi tertinggi dan mencetak hasil
nama_penjual = tertinggi(dict_penjualan)
print('Nama penjual dengan penjualan tertinggi selama seminggu adalah', nama_penjual)

print()

#Memanggil fungsi report dan mencetak hasil
rata_rata_perminggu = report(dict_penjualan)
urut = 0
for key, value in dict_penjualan.items(): 
  print('Rata-rata penjualan perbulan', value['nama'], 'adalah', rata_rata_perminggu[urut])
  urut += 1
