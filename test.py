# list_name = ['刘备', '关羽', '张飞', '张三', '李四', '杨戬', '诸葛亮']
# for name in list_name:
#     with open('dataname.txt', 'a+', encoding='utf8') as fp:
#         fp.write(name + ' ')
# with open('dataname.txt', 'r', encoding='utf8') as fp:
#     mn = fp.read()
#     name = mn.split('\n')
#     print(name)

import pyttsx3
listen = pyttsx3.init()
listen.say("输出语音")
listen.runAndWait()
