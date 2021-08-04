import os
str = os.listdir('/Volumes/TF_Card/源文件/图片收集&灵感图片/广告收集/suoyuetu')
print(str)
print(len(str)-1)
for i in str:
	print('<li><div class="thumbnail"><a href="https://foxlibs.oss-cn-hangzhou.aliyuncs.com/file/images/titlemap_img/%s" target="_blank"><img data-original="https://foxlibs.oss-cn-hangzhou.aliyuncs.com/file/images/titlemap_img/%s?x-oss-process=style/preview_image" src="https://foxlibs.oss-cn-hangzhou.aliyuncs.com/file/images/titlemap_img/%s?x-oss-process=style/preview_image" style="display: inline;"></a></div></li>' %(i,i,i))
	print('')