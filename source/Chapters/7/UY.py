with open('Video_7.1.rst', 'r') as f:
    a = f.read()

file_name = input('请输入文件名称:')
title = input('请输入题目：')
links = input('请输入连接：')

po = links.find('.mp4')
links = links[:po + 4]

a = a.replace('Antibiotics - What You Need To Know', title)
a = a.replace(
    r'https://outin-0fed40cae50711eaa61200163e1c94a4.oss-cn-shanghai.aliyuncs.com/sv/1edeeecf-1751fa532ae/1edeeecf-1751fa532ae.mp4',
    links)
file_name = 'Video_' + file_name + '.rst'
with open(file_name, 'w') as f:
    f.write(a)
