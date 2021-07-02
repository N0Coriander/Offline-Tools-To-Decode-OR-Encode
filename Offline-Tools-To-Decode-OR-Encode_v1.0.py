#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author : N0Coriander
# address : https://github.com/N0Coriander
# Date : 2021/7/2 10:44
# Desc : 针对常见的base64编码、字符串中含有的ASCII码、ROT13编码进行解码并还原语意。针对需要解码的场景，可提前复制进剪贴板中。

import base64
import re
import pyperclip
from urllib import parse

while 1:
    # URL解码
    def url_decode(data):
        return parse.unquote(data)

    # URL编码
    def url_encode(data):
        return parse.quote(data)

    # Base64解码
    def base64_decode(data):
        missing_padding = 4 - len(data) % 4  # base64的长度必须得是8的倍数
        if missing_padding:
            data += '=' * missing_padding
        base64_decode_info = base64.b64decode(data.encode('utf-8'))
        return str(base64_decode_info, 'utf-8')  # 将base64生成的bytes字符串转换为str类型,不然前面就会出现字母b

    # Base64编码
    def base64_encode(data):
        temp = base64.b64encode(data.encode('utf-8'))
        return str(temp, 'utf-8')

    # ROT13加密与解密
    def rot13_decode_and_encode(data, shift=13):
        data_list = list(data)
        temp = ''
        num = int(shift)
        for i in data_list:
            i = ord(i)
            if ord('a') <= i <= ord('z'):
                i = i + num
                if i > ord('z'):
                    # i = i - num - (26 - num)
                    i -= 26  # 例如你偏移量是13，你就向前移13又13，如果你偏移量是15，你需要向前移11，所以恒移26。
            if ord('A') <= i <= ord('Z'):
                i = i - num
                if i > ord('z'):
                    i -= 26
            a = chr(i)
            temp += a
        return temp

    # ASCII解码
    def ascii_decode(data):
        expression = re.compile(r'(\d+)')
        result = re.findall(expression, data)
        end = ''
        for i in result:
            end = end + chr(int(i))
        return end

    # ASCII编码
    def ascii_encode(data):
        expression = re.compile(r'(.)')
        result = re.findall(expression, data)
        end = ''
        for i in result:
            end = end + str(ord(i)) + '、'
        return end

    print("""—————————————————————————————————————————————————————
URL     编码   1    ｜    Base64  编码   3
        解码   2    ｜            解码   4
————————————————————————————————————————
ROT13   加密   5 __/
        解密   6
———————————————
ASCII   编码   7
        解码   8
———————————————""")
    user_input = input('[+] 输入数字： ')
    if user_input == '1':
        print(f"[!] Look here： {url_encode(input('[+] 请输入要编码的内容： '))}")
    elif user_input == '2':
        info = pyperclip.paste()
        print(f"[!] Look here： {url_decode(info)}")
    elif user_input == '3':
        print(f"[!] Look here： {base64_encode(input('[+] 请输入要编码的内容： '))}")
    elif user_input == '4':
        info = pyperclip.paste()
        print(f"[!] Look here： {base64_decode(info)}")
    elif user_input == '5':
        print(f"[!] Look here： {rot13_decode_and_encode(input('[+] 请输入要编码的内容： '))}")
    elif user_input == '6':
        info = pyperclip.paste()
        print(f"[!] Look here： {rot13_decode_and_encode(info)}")
    elif user_input == '7':
        print(f"[!] Look here： {ascii_encode(input('[+] 请输入要编码的内容： '))}")
    elif user_input == '8':
        info = pyperclip.paste()
        print(f"[!] Look here： {ascii_decode(info)}")
    else:
        print('[ERROR] 瞎几把输！')
