import os

os.chdir('/home/aei/Documents/codes/python/coreyms')

# membuat folder
# os.mkdir tidak bisa membuat folder dengan subfolder didalamnya jika
# folder tersebut belum ada
# os.mkdir('name-folder/sub-folder')
# os.makedirs bisa digunakan jika ingin membuat folder beserta subfolder (disarankan menggunakan ini)
# os.makedirs('name-folder/sub-folder')

# fungsinya hampir mirip dengan mkdir dan makedirs
# os.rmdir() can't delete intermediate directory
# it's more save to use os.rmdir() rather than os.removedirs()
# os.rmdir()
# os.removedirs()

# rename file, parameter pertama nama file awal, kedua nama file yang mau diubah.
# os.rename('file-awal', 'fileubah')

# menampilkan data dari sebuah file
# os.stat('name-file')