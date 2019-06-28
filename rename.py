# Tutorial dari https://youtu.be/ve2pmm5JqmI

import os

os.chdir('/home/aei/Documents/codes/python/coreyms/autorename')

# print directory
# print(os.getcwd())

for f in os.listdir():
	# print(f)
    file_name, file_ext = (os.path.splitext(f))
    f_title, f_course, f_num = (file_name.split('-'))
    # print(f_title)

    # Strip white space antara variable
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)
    
    # Versi lama
    # print('{}-{}-{}{}'.format(f_num, f_course, f_title, file_ext))

    # Versi Baru
    new_name = f'{f_num}-{f_course}-{f_title}{file_ext}'
    # print(new_name)

    os.rename(f, new_name)