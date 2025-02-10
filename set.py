# input yang dikeluarkan tdk berurutan
a = {"a",1, "b",2}
b= {1,2,3,4,5,6}
print(f"{a}")

# set operation
print(a|b) #(|) / print(a.union(b)) untuk menambahkan data set a dan set b 
print(a.intersection(b)) # (&) / print(a.intersection(b)) unntuk menemukan element yg sama
print(a-b) # (-) / print(a-b) menemukan element yg ada di set 1, tapi tdk ada di set 2
print(a.symmetric_difference (b)) # (^) / print(a.symmetric_difference (b)) menemukan elemet yg hanya ada pada element 1

# metod
b.add(100)
print(f"{b}") # menambahkan anggota set
b.update((200,300,400)) # menambakan beberapa anggota sekaligus
b.remove(6) # menghapus anggota set

c = [5,6,7,8,9]
d = set(c) # mengubah tipe data menjadi set
print(f"{d}")

# frozenset (datanya tetap tdk bisa di ubah)
e = frozenset(c) #  mengubah tipe data menjadi forzenset
print(f"{e}")