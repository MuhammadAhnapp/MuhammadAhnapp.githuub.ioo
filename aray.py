hobi = ["main bola", "ngoding", "tidur", "hahaha", "huhuhuhu", "anap"]
# cara mengubah tipe data menjadi array
urutan = (1,2,3,4)
hasil = list(urutan)
print(f'{hasil}')
# mencari nilai max dan min
mak = max(urutan)
minn = min(urutan)
# cara menambahkan anggota list
hobi.append("huhuhu") 
print(f"{hobi}")
#cara menghitung data yg paling terakhir
print(hobi[len(hobi) -1]) 
print(f"hobi -> {hobi}")
# #cara memanipulasi data
ubah_hobi = hobi
ubah_hobi[2] = "makan"
# untuk menghilangkan [ ] pada list/array
hobi = " ".join(hobi)
print(hobi)