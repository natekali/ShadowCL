from conf.config import conf_param
from tqdm import tqdm
import argparse
import requests
import logging
import random
import time
import os


def banner():
    print("\033[95m"+r"   _____ __              __              ________ "+"\033[0m")
    print("\033[95m"+r"  / ___// /_  ____ _____/ /___ _      __/ ____/ / "+"\033[0m")
    print("\033[95m"+r"  \__ \/ __ \/ __ `/ __  / __ \ | /| / / /   / /  "+"\033[0m")
    print("\033[95m"+r" ___/ / / / / /_/ / /_/ / /_/ / |/ |/ / /___/ /___"+"\033[0m")
    print("\033[95m"+r"/____/_/ /_/\__,_/\__,_/\____/|__/|__/\____/_____/"+"\033[0m")
    print("")
    print("\033[97m"+r"           https://github.com/natekali"+"\033[0m")
    print("")


def chooser(src_filename):
    with open(src_filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    return random.choice(lines).strip()


def formatter(country):
    username = chooser('src/user.txt')
    password = chooser('src/pass.txt')

    if country == 'worldwide':
        domain = chooser('src/dom.txt')
    elif country == 'fr':
        domain = chooser('src/country/FR_dom.txt')
    elif country == 'uk':
        domain = chooser('src/country/UK_dom.txt')
    elif country == 'pl':
        domain = chooser('src/country/PL_dom.txt')
    elif country == 'ru':
        domain = chooser('src/country/RU_dom.txt')
    elif country == 'ch':
        domain = chooser('src/country/CH_dom.txt')
    elif country == 'us':
        domain = chooser('src/country/US_dom.txt')
    elif country == 'mix':
        domain = chooser('src/country/MIX_dom.txt')
    else:
        print('\r')
        print('\033[91m[x]\033[0m When using -c, you must provide a valid country code (mix, fr, uk, pl, ru, ch, us)')
        print('')
        exit(0)

    payload = f"{username}@{domain}:{password}"

    return payload


def writer(payload, dst_filename):
    with open(dst_filename, 'a') as file:
        file.write(payload + '\n')


def help(parser):
    parser.print_help()
    print("")


def webhook(webhook_url, message):
    payload = {'content': message}
    requests.post(webhook_url, json=payload)


def pixeldrain(filename):
    pixeldrain_url = 'https://pixeldrain.com/api/file/'
    with open(filename, 'rb') as file:
        files = {'file': (os.path.basename(filename), file)}
        response = requests.post(pixeldrain_url, files=files)
    return response.json()


def setup_logs():
    logging.basicConfig(filename='logs/logs.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--length', type=int, help='desired number of entries (required)')
    parser.add_argument('-o', '--output', type=str, default='result.txt', help='desired output filename or filepath')
    parser.add_argument('-c', '--country', type=str, default='worldwide', help='desired mail domain by country (mix, fr, uk, pl, ru, ch, us)')

    parser.set_defaults(func=help)

    args = parser.parse_args()

    if args.length:
        x = 0
        dst_filename = args.output
        country = args.country
        length = args.length

        start_time = time.time()
        setup_logs()
        logging.info(f'ShadowCL generation started ({dst_filename})')

        with tqdm(total=length, desc="Generating", unit="line") as pbar:
            while x < length:
                payload = formatter(country)
                writer(payload, dst_filename)
                x += 1
                pbar.update(1)
                time.sleep(0.01)

        logging.info(f'ShadowCL generation finished ({dst_filename})')
        end_time = time.time()
        print('')
        print(f'\033[92m[✓]\033[0m {dst_filename} successfully created')
        print('')

        total_exec = end_time - start_time
        if total_exec < 60:
            time_unit = 'seconds'
            formatted_time = total_exec
        elif total_exec < 3600:
            time_unit = 'minutes'
            formatted_time = total_exec / 60
        else:
            time_unit = 'hours'
            formatted_time = total_exec / 3600

        logging.info(f'Total execution time : {formatted_time:.2f} {time_unit} ({dst_filename})')

        webhook_url = conf_param['discord_webhook_url']
        user_id = conf_param['discord_user_id']
        pixeldrain_resp = pixeldrain(dst_filename)

        if pixeldrain_resp.get('success', True):
            pixeldrain_id = pixeldrain_resp.get('id')
            pixeldrain_link = f'https://pixeldrain.com/u/{pixeldrain_id}'
            msg = f'{user_id} \r{dst_filename} generation completed ! \rlength : {length} \rcountry : {country} \rlink : {pixeldrain_link}'
            webhook(webhook_url, msg)
            os.remove(dst_filename)
        else:
            msg = f'{user_id} \r{dst_filename} generation completed ! \rlength : {length} \rcountry : {country} \rupload to pixeldrain failed :/'
            webhook(webhook_url, msg)

        exit(0)

    elif args.output != 'result.txt' and not args.length:
        print('\033[91m[x]\033[0m When using -o, you must also provide -l for the desired number of entries')
        print('')
        exit(0)

    elif args.country != 'worldwide' and not args.length:
        print('\033[91m[x]\033[0m When using -c, you must also provide -l for the desired number of entries')
        print('')
        exit(0)

    if hasattr(args, 'func'):
        args.func(parser)
        exit(0)



if __name__ == "__main__":
    try:
        banner()
        main()
    except Exception as e:
        logging.error(f'Error : {e}')
        print('')
        print('\033[91m[x]\033[0m Error :', e)
        print('')
    except KeyboardInterrupt:
        logging.info('ShadowCL aborted by user')
        print('')
        exit('\033[91m[x]\033[0m ShadowCL stopped')
