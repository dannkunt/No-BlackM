import os
import sys
from time import sleep

try:
    import requests
    from bs4 import BeautifulSoup as Bs
except ImportError:
    n_arr = ['n', 'no', 'н', 'нет']
    des = input('[!] У вас не установлены библиотеки\n'
                'Установить в автоматическом режиме y/n: ').lower()
    while des not in ('y', 'yes', 'д', 'да', *n_arr):
        des = input("Введите y или n: ")

    if des in n_arr:
        print('[!] Библиотеки не установлены')
        sleep(3)
        sys.exit()

    os.exec("python -m pip install -r requirements.txt")
    import requests
    from bs4 import BeautifulSoup as Bs

    del n_arr, des

# Мой Telegram: @FELIX4 - Для вопросов и поддержки (советы и т.д)
# Наш Канал в Telegram: https://t.me/No_BlackM - Там вы можете узнать всё новое о No-BlackMail
# Наш Telegram-Bot: https://t.me/No_BlackMail-bot - Там вы можете проверить номер по базе GetContact и т.д
# Наша Группа в Telegram: https://t.me/No_Black_Mail_chat - Там вы можете предлогать свои идеи и т.д
# Разработчик нашего GetContact Сервера: @Naarek  Онлайн сервис: https://phonebook.space
# 3 Размработчик @Volhebniypisosbot

dataAV = []
RESET = '\033[0m'
UNDERLINE = '\033[04m'
GREEN = '\033[32m'
YELLOW = '\033[93m'
RED = '\033[31m'
CYAN = '\033[36m'
BOLD = '\033[01m'
PINK = '\033[95m'
URL_L = '\033[36m'
LI_G = '\033[92m'
F_CL = '\033[0m'
DARK = '\033[90m'


def banner():
    print(f'{RED}█▄▄ █   █▀█ █▀▀ █▄▀ █▀▄▀█ █▀█ █ █{GREEN}'
          f'█▄█ █▄▄ █▀█ █▄▄ █ █ █ ▀ █ █▀█ █ █▄▄{RESET}{RED}V: 1.0.4\n')


def clear():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


def dup(data_file, country_v):  # Да, называние тупое
    try:
        print(f'{CYAN}{BOLD}[+] {LI_G}Страна:{F_CL} {country_v["name"]}, {country_v["fullname"]}{RESET}')
        data_file.write(f'[+] Страна: {country_v["name"]}, {country_v["fullname"]} \n')
    except KeyError:
        if country_v["country_code3"] == 'UKR':
            print(f'{CYAN}{BOLD}[+] {LI_G}Страна:{F_CL} Украина{RESET}')
            # Если сервис не сможет найти страны, Код Стран в помощь.

            data_file.write(f'[+] Страна: Украина \n')
        else:
            print(f'{YELLOW}{BOLD}[!] {LI_G}Стране:{F_CL} Неизвестно {RESET}')
            # print(f'{CYAN}{BOLD}[!] {RED}Данные о Стране не найдены{RESET}')

    print(f'{CYAN}{BOLD}[+] {LI_G}Код страны:{F_CL} {country_v.get("country_code3")}{RESET}')
    data_file.write(f'[+] Код страны: {country_v["country_code3"]}\n') if "country_code3" in country_v else 0

    print(f'{CYAN}{BOLD}[+] {LI_G}Код номеров:{F_CL} {country_v.get("telcod")}{RESET}')
    data_file.write(f'[+] Код номеров: {country_v["telcod"]}\n') if "country_code3" in country_v else 0

    print(f'{CYAN}{BOLD}[+] {LI_G}Локация:{F_CL} {country_v.get("location")}{RESET}')
    data_file.write(f'[+] Локация: {country_v["location"]}\n') if "location" in country_v else 0

    print(f'{CYAN}{BOLD}[+] {LI_G}Язык:{F_CL} {country_v.get("lang")}{RESET}')
    data_file.write(f'[+] Язык: {country_v["lang"]}\n') if "lang" in country_v else 0


def duplon(num_p):
    print(f'{YELLOW}{BOLD}[+] {LI_G}Широта: {F_CL}{num_p.get("latitude")}{RESET}')
    fileD.write(f'[+] Широта: {num_p["latitude"]}\n') if "latitude" in num_p else 0

    print(f'{YELLOW}{BOLD}[+] {LI_G}Долгота: {F_CL}{num_p.get("longitude")}{RESET}')
    fileD.write(f'[+] Долгота: {num_p["longitude"]}\n') if "longitude" in num_p else 0


def num_mnp_request(num):
    try:
        num_data = requests.post(f'https://htmlweb.ru/json/mnp/phone/{num}').json()

        data_f = open('dataFile.txt', 'a', encoding='utf-8')
        print(f'{PINK}{BOLD}[~] {LI_G}Поиск данных... {RESET}\n')

        try:
            region_v = num_data['region']
            oper = num_data['oper']
            data_f.write(f'\n[-] MNP - Запросы: \n')
            data_f.write(f'[+] Номер: {num}\n')

            print(f'{PINK}{BOLD}[+] {LI_G}Оператор:{F_CL} {oper.get("brand")}, {oper["name"]}{RESET}')
            data_f.write(f'[+] Оператор: {oper["brand"]}, {oper["name"]} \n')

            print(f'{PINK}{BOLD}[+] {LI_G}ID Оператора:{F_CL} {oper.get("id")}{RESET}')
            data_f.write(f'[+] ID Оператора: {oper["id"]} \n')

            print(f'{PINK}{BOLD}[+] {LI_G}URL Оператора:{F_CL} {oper.get("url")}{RESET}')
            data_f.write(f'[+] URL Оператора: {oper["url"]} \n')

            print(f'{PINK}{BOLD}[+] {LI_G}Код страны:{F_CL} {oper.get("country")}{RESET}')
            data_f.write(f'[+] Код страны: {oper["country"]} \n')

            print(f'{PINK}{BOLD}[+] {LI_G}Город:{F_CL} {region_v.get("name")}{RESET}')
            data_f.write(f'[+] Город: {region_v["name"]} \n')

            print(f'{PINK}{BOLD}[+] {LI_G}Округ:{F_CL} {region_v.get("okrug")}{RESET}')
            data_f.write(f'[+] Округ: {region_v["okrug"]} \n')

            print(f"{PINK}{BOLD}[+]{LI_G} Код машин: {F_CL}{region_v.get('autocod').replace(', ', ', ')}{RESET}")
            data_f.write(f'[+] Код машин: {region_v["autocod"]} \n')
        except KeyError:
            print(f'{YELLOW}{BOLD}[!] {LI_G}Оператор/Город:{F_CL} Неизвестно {RESET}')
            # print(f'{PINK}{BOLD}[!] {RED}Данные Оператор/Город не найдены{RESET}')
        print(f'\n{PINK}{BOLD}[!] {RED}Всего лимитов: {num_data["limit"]}{RESET}')
    except (requests.exceptions.RequestException, ValueError):
        print(f'{YELLOW}{BOLD}[!] {RED}Для проверки MNP включите VPN и перезапустите скрипт.{RESET}')
        sleep(3)
        sys.exit()


def save(names):
    with open('dataFile.txt', 'a', encoding='utf-8') as df:
        df.write(f'[-] Номер: +{number}\n')
        for inform in dataAV:
            df.write(inform + '\n')
        if names:
            df.write(f'\n[-] Все имена с ссылок: {", ".join(names)}')
        df.write(f'\n[-] https://api.whatsapp.com/send?phone={number}'
                 '&text=Hello,%20this%20is%20NO-Blackmail - Поиск номера в  WhatsApp\n')
        df.write('[-] https://facebook.com/login/identify/?ctx=recover&ars=royal_blue_bar - Поиск аккаунтов FaceBook\n')
        df.write('[-] https://linkedin.com/checkpoint/rp/request-password-reset-submit - Поиск аккаунтов Linkedin\n')
        df.write('[-] https://twitter.com/account/begin_password_reset - Поиск аккаунтов Twitter\n')
        df.write(f'[-] https://viber://add?number={number} - Поиск номера в Viber\n')
        df.write(f'[-] https://skype:{number}?call - Звонок на номер с Skype\n')
        # f.write(f'[-] https://nuga.app - Поиск аккаунтов Instagram\n')
        df.write(f'[-] tel:{number} - Звонок на номер с телефона\n\n')
        if names:
            print(f"\n{YELLOW}{BOLD}[+]{LI_G} Все имена с ссылок: {RESET}{', '.join(names)}")


if not os.path.exists('.banner_840'):
    clear()
    try:
        banner_tx = open('README.md', encoding='utf-8').read()
        print(banner_tx[219:1541].replace('#', '').replace('*', '').replace('-', '•'))
        print(f'\n{LI_G}Этот текст покажется лишь один раз!{RESET}')
        input(f'{LI_G}Нажмите ENTER чтобы продолжить: {RESET}')
        open('.banner_840', 'w')
        clear()
    except FileNotFoundError:
        print(f'\n{YELLOW}{BOLD}[!] Увас отсуствует {RESET}README.md')
        sleep(1)
        clear()

if os.path.exists('dataFile.txt'):
    clear()
    print(f'{CYAN}{BOLD}[1] {LI_G}Перезаписать данные в файл.{RESET}')
    print(f'{CYAN}{BOLD}[ENTER] {LI_G}Добавить к остальным.{RESET}\n')
    if input(f'{CYAN}{BOLD}[~] {LI_G}Выберите метод: {RESET}') == '1':
        os.remove('dataFile.txt')
        clear()
        print(f'{YELLOW}{BOLD}[+] {LI_G}Данные будут:{RESET} Перезаписаны')
        sleep(1)
    else:
        clear()
        print(f'{YELLOW}{BOLD}[+] {LI_G}Данные будут:{RESET} Добавлены к остальным')
        sleep(1)
else:
    clear()
    print(f'{YELLOW}{BOLD}[#] {LI_G}Подготовка... {RESET}')

try:
    get_version = Bs(requests.get('https://github.com/DataSC3/No-BlackM').text, 'html.parser').find(
        ['span'], class_='d-none d-sm-inline').findNext(['strong']).text
    clear()
    with open('.banner_840', 'r') as fileF:
        try:
            if str(get_version) != str(fileF.read().split(':')[1]):
                with open('.banner_840', 'w') as fileW:
                    fileW.write(f'Version: {get_version}')
                    print(f'{YELLOW}{BOLD}[!] {RED}Доступно обновление!{YELLOW}{BOLD} [!]\n\n')
        except IndexError:
            with open('.banner_840', 'w') as fileW:
                fileW.write(f'Version: {get_version}')
except FileNotFoundError:
    print(f'\n{YELLOW}{BOLD}[!] Увас отсуствует {RESET}README.md')
    sleep(1)
    clear()

banner()
print(f'{YELLOW}{BOLD}[1] {LI_G}IP {CYAN}-{LI_G} Данные{RESET}')
print(f'{YELLOW}{BOLD}[2] {LI_G}MNP {PINK}-{LI_G} Запросы {RESET}')
choice = input(f'{YELLOW}{BOLD}[~] {LI_G}Выберите проверку. ENTER - Базовая проверка: {RESET}')
if choice == '1':
    clear()
    print(f'{CYAN}█▄▄ █   █▀█ █▀▀ █▄▀ █▀▄▀█ █▀█ █ █{PINK}'
          f'█▄█ █▄▄ █▀█ █▄▄ █ █ █ ▀ █ █▀█ █ █▄▄{RESET}{CYAN}V: 1.0.4\n')
    result_ip = requests.get('https://httpbin.org/ip').text.split()[2].strip('"')
    print(f'{CYAN}{BOLD}[#] {LI_G}Ваш IP: {DARK}{result_ip}{RESET}')
    ip = input(f'{CYAN}{BOLD}[~] {LI_G}Введите IP: {RESET}').strip()

    try:
        ip_data = requests.post(f'https://htmlweb.ru/geo/api.php?json&ip={ip}').json()
    except requests.exceptions.RequestException:
        print(f'{YELLOW}{BOLD}[!] {RED}Для проверки IP включите VPN и перезапустите скрипт.{RESET}')
        sleep(3)
        sys.exit()
    # except ValueError:

    with open('dataFile.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n[-] IP - Данные: \n')

        print(f'{CYAN}{BOLD}[~] {LI_G}Поиск данных... {RESET}\n')
        print(f'{CYAN}{BOLD}[+] {LI_G}IP: {RESET}{ip}')
        file.write(f'[+] IP: {ip}\n')

        try:
            strana = ip_data['country']
            reg = ip_data['region']

            dup(file, strana)

            print(f'{CYAN}{BOLD}[+] {LI_G}Город:{F_CL} {reg.get("name")}{RESET}')
            file.write(f'[+] Город: {reg["name"]}\n') if "name" in strana else 0

            print(f'{CYAN}{BOLD}[+] {LI_G}Код машин:{F_CL} {reg.get("autocod")}{RESET}')
            file.write(f'[+] Код машин: {reg["autocod"]}\n') if "autocod" in strana else 0

            duplon(strana)
        except KeyError:
            print(f'{YELLOW}{BOLD}[!] {LI_G}Город/Локация:{F_CL} Неизвестно {RESET}')
            # print(f'{CYAN}{BOLD}[!] {RED}Данные Город/Локация не найдены{RESET}')
        print(f'\n{CYAN}{BOLD}[!] {RED}Всего лимитов: {ip_data.get("limit")}{RESET}')

    sleep(3)
    exit()
elif choice == '2':
    clear()
    print(f'{PINK}█▄▄ █   █▀█ █▀▀ █▄▀ █▀▄▀█ █▀█ █ █{CYAN}'
          f'█▄█ █▄▄ █▀█ █▄▄ █ █ █ ▀ █ █▀█ █ █▄▄{RESET}{PINK}V: 1.0.4\n')
    print(f'{PINK}{BOLD}[#] {LI_G}Пример: {DARK}+7 495 766 11-11{RESET}')
    ch_num = input(f'{PINK}{BOLD}[~] {LI_G}Введите номер телефона: {RESET}').replace('+', '').replace(
        '-', '').replace('(', '').replace(')', '').replace(' ', '')
    if ch_num.isdigit():
        if ch_num[0] == '8':
            num_mnp_request(num_mnp_request('7' + ch_num[1:]))
            sys.exit()
        else:
            num_mnp_request(ch_num)
            sys.exit()
    else:
        exit(f'{PINK}{BOLD}[!] {RED}"{RESET}{ch_num}{RED}" - Не является номером\n{RESET}')
clear()
banner()
print(f'{YELLOW}{BOLD}[#] {LI_G}Пример: {DARK}+7 495 766 11-11{RESET}')
number = input(f'{YELLOW}{BOLD}[~] {LI_G}Введите номер: {RESET}').replace('+', '').replace('-', '').replace(
    '(', '').replace(')', '').replace(' ', '')
if number.isdigit():
    if number[0] == '8':
        number = '7' + number[1:]
else:
    print(f'{YELLOW}{BOLD}[!] {RED}"{RESET}{number}{RED}" - Не является номером\n{RESET}')
    sleep(3)
    exit()

fileD = open('dataFile.txt', 'a', encoding='utf-8')
try:
    data = requests.post(f'https://htmlweb.ru/geo/api.php?json&telcod={number}').json()
    print(f'{YELLOW}{BOLD}[~] {LI_G}Поиск данных... {RESET}\n')
    fileD.write(f'[+] Номер: +{number}\n')
    country = data.get('country')

    try:
        dup(fileD, country)

        print(f'{YELLOW}{BOLD}[+] {LI_G}Длина номера:{F_CL} {country.get("telcod_len")}{RESET}')
        fileD.write(f'[+] Длина номера: {country["telcod_len"]} \n') if "telcod_len" in country else 0
    except KeyError:
        print(f'{YELLOW}{BOLD}[!] {LI_G}Страна/Язык:{F_CL} Неизвестно {RESET}')
        # print(f'{YELLOW}{BOLD}[!] {RED}Данные Страна/Язык не найдены{RESET}')

    try:
        region = data['region']
        endIndex = region['name'].split()

        if endIndex[1] == 'край' and region.get("name") is not None:
            print(f'{YELLOW}{BOLD}[+] {LI_G}Край:{F_CL} {region["name"]}{RESET}')
            fileD.write(f'[+] Край: {region["name"]} \n')

        if endIndex[1] == 'область' and region.get("name") is not None:
            print(f'{YELLOW}{BOLD}[+] {LI_G}Область:{F_CL} {region["name"]}{RESET}')
            fileD.write(f'[+] Область: {region["name"]} \n')
        else:
            print(f'{YELLOW}{BOLD}[+] {LI_G}Неизвестное:{F_CL} {region["name"]}{RESET}')

        print(f'{YELLOW}{BOLD}[+] {LI_G}Округ:{F_CL} {region.get("okrug")}{RESET}')
        fileD.write(f'[+] Округ: {region["okrug"]} \n') if "okrug" in region else 0

    except KeyError:
        print(f'{YELLOW}{BOLD}[!] {LI_G}Область/Край:{F_CL} Неизвестно {RESET}')
        # print(f'{YELLOW}{BOLD}[!] {RED}Данные Область/Край не найдены{RESET}')

    try:
        capital = data['capital']

        print(f'{YELLOW}{BOLD}[+] {LI_G}Столица:{F_CL} {capital.get("name")}{RESET}')
        fileD.write(f'[+] Столица: {capital["name"]} \n') if "name" in capital else 0

        print(f'{YELLOW}{BOLD}[+] {LI_G}Код домашнего номера столицы:{F_CL} '
              f'+{str(capital.get("telcod")).replace(",", ", ")}{RESET}')
        fileD.write(f'[+] Код домашнего номера столицы: +{capital["telcod"]} \n') if "telcod" in capital else 0

    except KeyError:
        print(f'{YELLOW}{BOLD}[!] {LI_G}Код/Столица:{F_CL} Неизвестно {RESET}')
        # print(f'{YELLOW}{BOLD}[!] {RED}Данные Код/Столица не найдены{RESET}')

    try:
        data = data['0']

        print(f'{YELLOW}{BOLD}[+] {LI_G}Город:{F_CL} {data.get("name")}{RESET}')
        fileD.write(f'[+] Город: {data["name"]} \n') if "name" in data else 0

        print(f'{YELLOW}{BOLD}[+] {LI_G}Оператор:{F_CL} {data.get("oper_brand")}{RESET}')
        fileD.write(f'[+] Оператор: {data["oper_brand"]} \n') if "oper_brand" in data else 0

        print(f'{YELLOW}{BOLD}[+] {LI_G}Номера:{F_CL} {data.get("def")}{RESET}')
        fileD.write(f'[+] Номера: {data["def"]} \n') if "def" in data else 0

        duplon(data)

    except KeyError:
        print(f'{YELLOW}{BOLD}[!] {LI_G}Город/Оператор:{F_CL} Неизвестно {RESET}')
        # print(f'{YELLOW}{BOLD}[!] {RED}Данные Город/Оператор не найдены{RESET}')

    if data['limit'] != 0:
        try:
            num_name = []
            for i in Bs(requests.get(f'https://phonebook.space/?number=%2B{number}').text, 'html.parser').find(
                    'div', class_='results').find_all('li'):
                num_name.append(i.text.strip())

            if num_name:
                print(f"{YELLOW}{BOLD}[+]{LI_G} Теги с номера: {F_CL} {', '.join(num_name)}")
                fileD.write('[+] Теги с номера: ' + ', '.join(num_name) + '\n')
            else:
                print(f'{YELLOW}{BOLD}[+] {LI_G}Теги по номеру: {F_CL}Нечего нету{RESET}')

        except requests.exceptions.RequestException:
            print(f'{YELLOW}{BOLD}[!] {RED}Для проверки GetContact включите VPN и перезапустите скрипт.{RESET}')
        except ValueError:
            print(f'{YELLOW}{BOLD}[!] {RED}Для проверки GetContact включите VPN и перезапустите скрипт.{RESET}')

        name = []

        if country.get("country_code3") == 'RUS':
            dataAV = []
            dataOB = []

            # PhoneReview
            try:
                reviews_rev = Bs(requests.get(f'http://phoneradar.ru/phone/{number}').text, 'html.parser').find(
                    'div', class_='alert alert-danger').text.strip()
                print(f'{YELLOW}{BOLD}[+] {LI_G}Рейтинг: {F_CL}{reviews_rev}{RESET}')
                fileD.write(f'[+] Рейтинг: {reviews_rev} \n')
            except AttributeError:
                reviews_rev = 'Рейтинг номера не определен, отзывов о номере еще нет'
                print(f'{YELLOW}{BOLD}[+] {LI_G}Рейтинг: {F_CL}{reviews_rev}{RESET}')
                fileD.write(f'[+] Рейтинг: {reviews_rev} \n')
            except requests.exceptions.RequestException:
                print(f'{YELLOW}{BOLD}[!] {RED}Для проверки отзывов включите VPN и перезапустите скрипт.{RESET}')
            except ValueError:
                print(f'{YELLOW}{BOLD}[!] {RED}Для проверки отзывов включите VPN и перезапустите скрипт.{RESET}')
            try:
                content_av = Bs(requests.get(f'https://mirror.bullshit.agency/search_by_phone/{number}').text,
                                'html.parser')
                h1 = content_av.find('h1')
                if h1.text == '503 Service Temporarily Unavailable':
                    print(f'{YELLOW}{BOLD}[!] {RED}Ваш запрос временно заблокирован. Пожалуйста, подождите 6-15 минут.'
                          f'{RESET}')
                else:
                    count = 0
                    print(f'\n{YELLOW}{BOLD}[~] {LI_G}Поиск данных по Авито: {RESET}')
                    print(f'{YELLOW}{BOLD}[~] {LI_G}Авито: {F_CL}{h1.text.replace("  ", "")}{RESET}')
                    print(f'{YELLOW}{BOLD}[+] {LI_G}------{RESET}-------------------------------------- \n')
                    for oBV in content_av.find_all(['h4', 'span']):
                        print(f'{YELLOW}{BOLD}[+] {LI_G}{oBV.text}{RESET}')
                        dataOB.append(oBV.text)

                    with open('dataFile.txt', 'a', encoding='utf-8') as f:
                        for info in dataOB:
                            f.write(f'[-] {info}\n')

                    for url in content_av.find_all(['a']):
                        count += 1
                        avito_url = requests.get(f"https://mirror.bullshit.agency{url['href']}")

                        link_av = Bs(avito_url.text, 'html.parser').find(['a'])['href']
                        print(f'{YELLOW}{BOLD}[{count}] {URL_L}{UNDERLINE}{link_av}{RESET}')

                        name.append(Bs(avito_url.text, 'html.parser').find('strong').text)
                        dataAV.append(f'[{count}] {link_av}')
                        # except:
                        #     print(f'{YELLOW}{BOLD}[{count}] {RED}{UNDERLINE}{link_av}{RESET}')

                    save(name)

            except requests.exceptions.RequestException:
                print(f'{YELLOW}{BOLD}[!] {RED}Для проверки Avito включите VPN и перезапустите скрипт.{RESET}')
            except ValueError:
                print(f'{YELLOW}{BOLD}[!] {RED}Для проверки Avito включите VPN и перезапустите скрипт.{RESET}')

        save(name)
        print(f'\n{YELLOW}{BOLD}[+] {LI_G}Проверьте эти ссылки ( Мессенджеры и Социальные сети ): {RESET}')
        print(f'{YELLOW}{BOLD}[1] {URL_L}{UNDERLINE}https://api.whatsapp.com/send?phone={number}'
              f'&text=Hello,%20this%20is%20No-BlackMail{RESET} - Поиск номера в  WhatsApp')
        print(f'{YELLOW}{BOLD}[2] {URL_L}{UNDERLINE}https://facebook.com/login/identify/?ctx=recover&ars=royal_blue_bar'
              f'{RESET} - Поиск аккаунтов FaceBook')
        print(f'{YELLOW}{BOLD}[3] {URL_L}{UNDERLINE}https://linkedin.com/checkpoint/rp/request-password-reset-submit'
              f'{RESET} - Поиск аккаунтов Linkedin')
        print(f'{YELLOW}{BOLD}[4] {URL_L}{UNDERLINE}https://twitter.com/account/begin_password_reset{RESET}'
              ' - Поиск аккаунтов Twitter')
        print(f'{YELLOW}{BOLD}[5] {URL_L}{UNDERLINE}https://viber://add?number={number}{RESET} - Поиск номера в Viber')
        print(f'{YELLOW}{BOLD}[6] {URL_L}{UNDERLINE}https://skype:{number}?call{RESET} - Звонок на номер с Skype')
        print(f'{YELLOW}{BOLD}[7] {URL_L}{UNDERLINE}tel:{number} {RESET}- Звонок на номер с телефона')
        # print(f'{YELLOW}{BOLD}[8] {URL_L}{UNDERLINE}https://nuga.app {RESET}- Поиск аккаунтов Instagram')

        print(f'\n{YELLOW}{BOLD}[+] {LI_G}Данные о номере: +{number} добавлены в файл {RESET}dataFile.txt')
    print(f'{YELLOW}{BOLD}[!] {RED}Всего лимитов: {data["limit"]}{RESET}')

except requests.exceptions.RequestException:
    print(f'{YELLOW}{BOLD}[!] {RED}Для проверки номера включите VPN и перезапустите скрипт.{RESET}')
    sys.exit()
except ValueError:  # json.decoder.JSONDecodeError
    pass
    # sys.exit(f'{YELLOW}{BOLD}[!] {RED}Для проверки номера включите VPN и перезапустите скрипт.{RESET}')
