# berisi "key" dan "value"
datakaryawan = {"nama" : ["Adi", "Ucup", "Mansyur"], "umur": [29, 30, 35], "jabatan": ["Manager", "karyawan", "operator"]}
print(datakaryawan["jabatan"])
nomor = {1:"a", 2:"a"} # key tidak boleh sama tapi value boleh sama
nomor[2] = "b" # cara mengubah value 
print(nomor.get(2))
print(datakaryawan.keys())    # mengakses semua key pada dictionary
print(datakaryawan.values())   # mengakses semua value 