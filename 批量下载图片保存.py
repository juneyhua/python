import requests
r = requests.get(url='https://alpha.wallhaven.cc/search?q=naruto&atleast=1920x1080&sorting=relevance&order=desc&page=1') 
print(r.url)
#print(r.text)

def save_to_file(file_name, contents):
	fh = open(file_name, 'w')
	fh.write(contents)
	fh.close()
#把读取的html字符串保存为文件
save_to_file('1.html', r.text)