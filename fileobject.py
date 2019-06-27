# Open file
# f = open('test.txt', 'r')

# Open file with context manager

# with open ('test.txt', 'r') as f:
    # f_contents = f.read()
    # f_contents = f.readlines()
    # f_contents = f.readline()
    # print(f_contents, end='')

    # f_contents = f.readline()
    # print(f_contents, end='')
    # for line in f: 
    #     print(line, end='')

    # size_to_read = 10
    # f_contents = f.read(size_to_read)

    # while len(f_contents) > 0:
    #     print(f_contents, end='')
    #     f_contents = f.read(size_to_read)

# with open('test2.txt', 'w') as f:
#     f.write('Text')
#     f.seek(0)
#     f.write('R')

# Copy data dari test.txt ke test_copy.txt
# with open('test.txt', 'r') as rf:
#     with open('test_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

# Copy file gambar menggunakan fungsi b = binary
# with open('neonretro.jpg', 'rb') as rf:
#     with open('neonretro_copy.jpg', 'wb') as wf:
#         for line in rf:
#             wf.write(line)

# Copy file gambar menggunakan fungsi chunk
with open('neonretro.jpg', 'rb') as rf:
    with open('neonretro_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
# f.close()