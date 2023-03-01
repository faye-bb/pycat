# pycat
a simple Reverse Shell listener, support charset config
苦于中文环境下windows的webshell因为字符集原因乱码，索性自己写了半个
支持字符集设置
中文windows环境下的朋友们可以把字符集设置成GBK

eg：python pycat.py -p 4444 -h 0.0.0.0 -c GBK -t 0.5 

usage：python pycat.py -p port [-h host]  [-c charset]  [-t wait_time]

       default:host 0.0.0.0    charset utf-8    wait_time 0.5
       
press --help to get help

Version:0.0.1


![image](https://user-images.githubusercontent.com/26599551/222226679-f56731da-f2b5-4a49-be68-dd9b1adb838b.png)


![image](https://user-images.githubusercontent.com/26599551/222226368-86013099-ea3a-4524-8b44-17be88da6839.png)
