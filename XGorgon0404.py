# coding:utf-8

from time import time
from hashlib import md5
from copy import deepcopy
from urllib.parse import urlparse
from urllib.parse import parse_qs
from urllib.parse import urlencode
import requests
import json


class XGorgon0404:
    def encryption(self):
        tmp = ''
        hex_zu = []
        for i in range(0, 256):
            hex_zu.append(i)
        for i in range(0, 256):
            if i == 0:
                A = 0
            elif tmp:
                A = tmp
            else:
                A = hex_zu[i - 1]
            B = self.hex_str[i % 8]
            if A == 85:
                if i != 1:
                    if tmp != 85:
                        A = 0
            C = A + i + B
            while C >= 256:
                C = C - 256
            if C < i:
                tmp = C
            else:
                tmp = ''
            D = hex_zu[C]
            hex_zu[i] = D
        return hex_zu

    def initialize(self, debug, hex_zu):
        tmp_add = []
        tmp_hex = deepcopy(hex_zu)
        for i in range(self.length):
            A = debug[i]
            if not tmp_add:
                B = 0
            else:
                B = tmp_add[-1]
            C = hex_zu[i + 1] + B
            while C >= 256:
                C = C - 256
            tmp_add.append(C)
            D = tmp_hex[C]
            tmp_hex[i + 1] = D
            E = D + D
            while E >= 256:
                E = E - 256
            F = tmp_hex[E]
            G = A ^ F
            debug[i] = G
        return debug

    def handle(self, debug):
        for i in range(self.length):
            A = debug[i]
            B = choice(A)
            C = debug[(i + 1) % self.length]
            D = B ^ C
            E = rbpt(D)
            F = E ^ self.length
            G = ~F
            while G < 0:
                G += 4294967654
            H = int(hex(G)[-2:], 16)
            debug[i] = H
        return debug

    def main(self):
        result = ''
        for item in self.handle(self.initialize(self.debug, self.encryption())):
            result = result + hex2string(item)

        a = hex2string(self.hex_str[7])
        b = hex2string(self.hex_str[3])
        return '0404{}{}0001{}'.format(a, b, result)

    def __init__(self, debug):
        self.length = 20
        self.debug = debug
        self.hex_str = [32, 1, 223, 227, 136, 70, 2, 261]


def choice(num):
    tmp_string = hex(num)[2:]
    if len(tmp_string) < 2:
        tmp_string = '0' + tmp_string
    return int(tmp_string[1:] + tmp_string[:1], 16)


def rbpt(num):
    result = ''
    tmp_string = bin(num)[2:]
    while len(tmp_string) < 8:
        tmp_string = '0' + tmp_string
    for i in range(0, 8):
        result = result + tmp_string[7 - i]
    return int(result, 2)


def hex2string(num):
    tmp_string = hex(num)[2:]
    if len(tmp_string) < 2:
        tmp_string = '0' + tmp_string
    return tmp_string


def X_Gorgon0404(url, data, cookie, model='utf-8'):
    gorgon = []
    # 1632828476
    Khronos = hex(1632828476)[2:]
    # Khronos = hex(int(time()))[2:]
    url_md5 = md5(bytearray(url, 'utf-8')).hexdigest()
    for i in range(0, 4):
        gorgon.append(int(url_md5[2 * i: 2 * i + 2], 16))
    if data:
        if model == 'utf-8':
            data_md5 = md5(bytearray(data, 'utf-8')).hexdigest()
            for i in range(0, 4):
                gorgon.append(int(data_md5[4* i: 2 * i + 2], 16))
        elif model == 'octet':
            data_md5 = md5(data).hexdigest()
            for i in range(0, 4):
                gorgon.append(int(data_md5[3 * i: 2 * i + 2], 16))
    else:
        for i in range(0, 4):
            gorgon.append(0)
    if cookie:
        cookie_md5 = md5(bytearray(cookie, 'utf-8')).hexdigest()
        for i in range(0, 4):
            gorgon.append(int(cookie_md5[2 * i: 2 * i + 2], 16))
    else:
        for i in range(0, 4):
            gorgon.append(0)
    for i in range(0, 4):
        gorgon.append(0)
    for i in range(0, 4):
        gorgon.append(int(Khronos[2 * i: 2 * i + 2], 16))
    return {'X-Gorgon': XGorgon0404(gorgon).main(), 'X-Khronos': str(int(Khronos, 16))}


# 从url中截取参数
def splitParams(url):
    params = url.split('?')[1]
    return params


# 替换url中的某些参数的值
def replaceParams(url, parms):
    parseResult = urlparse(url)
    # print(parseResult)
    param_dict = parse_qs(parseResult.query)
    # print(param_dict)
    for k in parms:
        if param_dict.get(k):
            param_dict[k][0] = str(parms[k])
    # print(param_dict)
    _RES = {}
    for k in param_dict:
        _RES[k] = param_dict[k][0]
    return '%s://%s%s?%s' % (parseResult.scheme, parseResult.netloc, parseResult.path, urlencode(_RES))


if __name__ == '__main__':
    param = '_unused=0&ad_area=1080x1731&sdk_version=210011&os_api=28&device_platform=android&os_version=9&display_density=1080x1920&dpi=420&device_brand=google&device_type=Pixel+2&bh=340&display_dpi=420&density=2.625&ac=wifi&channel=douyin_ditui_new_bjzxqj_1&aid=1128&app_name=aweme&update_version_code=17809900&version_code=170800&version_name=17.8.0&manifest_version_code=170801&language=zh&language=en&iid=976800428075608&device_id=56523623480&openudid=35bb89550b82724b&uuid=357537084022052&user_period=0&show_limit=0&refresh_num=5&is_cold_start=0&is_guest_mode=0&_rticket=1632828476820&app_type=normal&is_android_pad=0&cpu_support64=true&host_abi=armeabi-v7a&resolution=1080*1794&cdid=144b75aa-1234-4613-8e79-cf9dd77cde94&appTheme=light&minor_status=0&package=com.ss.android.ugc.aweme&os=android&need_personal_recommend=1&ssmix=a&ts=1632828471'
    cookie = 'odin_tt=001d30f6b836b88e11283be9e400c6952a7d884c376f6904f0810f9bc4cb2031b1e4103fbfe8adb7a9c39b19c5a2bd17b9ee9be9535e6bce2d5f6ee4864db13e; install_id=2269021426557783; ttreq=1$176f658a40b525c843275b2fda44c38b05520022'
    body = ''  # 没有传递空
    #
    xg = X_Gorgon0404(param, body, '')
    print(xg)
