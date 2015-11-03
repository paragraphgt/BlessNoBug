#python3

import os

imgs={
	"buddha":
	[
	"                   _oo0oo_",
	"                  o8888888o",
	"                  88\" . \"88",
    "                  (| -_- |)",
	"                  0\  =  /0",
	"                ___/`---'\___",
	"              .\' \\\\|     |// \'.",
	"             / \\\\|||  :  |||// \ ",
	"            / _||||| -:- |||||- \ ",
	"           |   | \\\\\  -  /// |   |",
	"           | \_|  \'\'\---/\'\'  |_/ |",
	"           \  .-\__  \'-\'  ___/-. /",
	"         ___\'. .\'  /--.--\  `. .\'___",
	"      .\"\" \'<  `.___\_<|>_/___.\' >\' \"\".",
	"     | | :  `- \`.;`\ _ /`;.`/ - ` : | |",
	"     \  \ `_.   \_ __\ /__ _/   .-` /  /",
	" =====`-.____`.___ \_____/___.-`___.-\'=====",
	"                   `=---=\'",
	" ",
	" ",
	" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
	" ",
	"           佛祖保佑         永无BUG",
	],
	"alpaca":
	[
	"* ┏┓       ┏┓",
	"*┏┛┻━━━━━━━┛┻┓",
	"*┃　　　　　   ┃ ",
	"*┃　　　━　  　┃ ",
	"*┃  ┳┛   ┗┳  ┃ ",
	"*┃　　　　　   ┃",
	"*┃　　　┻　　  ┃",
	"*┃　　　　　   ┃",
	"*┗━┓       ┏━┛",
	"*  ┃　　　  ┃神兽保佑",
	"*  ┃　　　  ┃代码无BUG",
	"*  ┃　　　  ┗━━━┓",
	"*  ┃　　　   　　┣┓",
	"*  ┃　　　　　　　┏┛",
	"*  ┗┓┓┏━━━━━┳┓┏┛",
	"*   ┃┫┫     ┃┫┫",
	"*   ┗┻┛     ┗┻┛",
	"*",
	]
}

comments={
	"others":["/*","*/"],
	".prl":["＝begin","=cut"],
	".ruby":["=begin","=end"],
	".m":["%{","%}"],
	".lua":["--[=[","]=]"],
	".py":["\'\'\'","\'\'\'"],
	".html":["<!--","-->"],
	".sh":["<<!","!"]
}


exist= False
filePath=input("Input your file\'s path:")

while exist == False:
	if os.path.isfile(filePath) == False:
		print("Your file is not there.")
		filePath=input("Input your file\'s path correctly:")
	else:
		fileName=os.path.splitext(filePath)
		exist= True

if fileName[1] in comments:
	cBegin=comments[fileName[1]][0]
	cEnd=comments[fileName[1]][1]
else:
	cBegin=comments["others"][0]
	cEnd=comments["others"][1]


exist=False
while exist==False:
	way=input("chose a way to bless your code:(buddha/alpaca)")
	if way=="buddha" or way=='1':
		printout=imgs["buddha"]
		exist=True
	elif way=="alpaca" or way=='2':
		printout=imgs["alpaca"]
		exist=True
	else:
		print("Error.")

f=open(filePath,'a')
f.writelines(os.linesep)
f.writelines(cBegin)
f.writelines(os.linesep)
for x in printout:
	f.writelines(x)
	f.writelines(os.linesep)
f.writelines(cEnd)

f.close();
print("Done.")
print("Your code has been protected.")
