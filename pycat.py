#!/usr/bin/env python
import time
import socket
import sys

__version__ = "0.0.1"
lhost = "0.0.0.0"
lport = 4444
charset = "utf-8"
wait_time = 0.5
start_index = 1
# config
args = sys.argv
if len(args) <= 1 or "--help" in args:
    print("    __     ___ _    _     ",
          "    \ \   / (_) | _(_)_ __ __ _     ",
          "     \ \ / /| | |/ / | '__/ _` |    ",
          "      \ V / | |   <| | | | (_| |    ",
          "       \_/  |_|_|\_\_|_|  \__,_|    ",
          sep="\n"
          )
    print("usage：python pycat.py -p port [-h host]  [-c charset]  [-t wait_time]")
    print("       default:host 0.0.0.0    charset utf-8    wait_time 0.5")
    print("press --help to get help")
    print("Version:%s" % __version__)
    exit(0)

if '-p' in args:
    lport = int(args[args.index('-p') + 1])
else:
    print("please input your lport with -p")
    print("press --help to get help")
    exit(0)
if '-h' in args:
    lhort = args[args.index('-h') + 1]

if '-c' in args:
    charset = args[args.index('-c') + 1]
if '-t' in args:
    wait_time = args[args.index('-t') + 1]

first_flag = True
current_banner = "Please input Something:"


def resp() -> bytes:
    global tar
    while True:
        rev_content = tar.recv(4096)
        if len(rev_content) < 4096:
            break
    return rev_content


def beautify(text: str) -> str:
    """
     text[0] : command that inputted before eg ：dir  Microsoft Windows [版本 10.0.22621.1265]
     text[1:-2] : result of sent command eg : win/Administrator  (c) Microsoft Corporation。保留所有权利。
     text[-1] : System path or banner? eg : C:\\Users\\85850\\Desktop\\netcat>
    """
    global first_flag
    global start_index
    global current_banner
    result = ""

    if "\n\n" in text:
        text = text.split("\n\n")
    elif "\r\n" in text:
        text = text.split("\r\n")

    current_banner = text[-1]

    if first_flag:
        first_flag = False
        start_index = 0

    for i in text[start_index:-1]:
        result += (i + "\n")

    return result


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((lhost, lport))
server.listen()
tar, addr = server.accept()
print(tar, addr)

while True:
    time.sleep(wait_time)
    # content = resp().decode("GBK")
    content = beautify(resp().decode(charset))
    print(content, end="")
    print(current_banner, end="")
    m_input = input() + "\n"
    m_input = m_input.encode()
    tar.send(m_input)

# server.close();
