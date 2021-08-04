#pip install baidu-aip
from aip import AipSpeech
APP_ID = '14383620'
API_KEY = 'CUL1QMDpG6c4bXcz6RVS9EZ0'
SECRET_KEY = 'IDTdH3FO6vFIVStIYsXIkux41lynhCg9'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
text="我弄死你，你这个大笨蛋，大坏蛋，讨厌" 
#需要合成语音的文字内容    
result = client.synthesis(text,'zh',1,{
	'vol':10,
	'per':4,
	'spd':9,   #语速
});
# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result,dict):
	with open('auido.mp3', 'wb') as f:
		f.write(result)
	