import argparse
import json
import os
import shutil
import sys
import time
from os.path import join, dirname, exists

from methods.ben import BenDeobf
from methods.blank import BlankDeobf
from methods.empyrean import VespyDeobf
from methods.luna import LunaDeobf
from methods.notobf import NotObfuscated
from methods.other import OtherDeobf
from utils.decompile import unzipJava, checkUPX
from utils.download import TryDownload
from utils.pyinstaller.pyinstaller import ExtractPYInstaller
from utils.pyinstaller.pyinstallerExceptions import ExtractionError
from utils.webhookspammer import Webhook
from utils.telegram import Telegram
from utils.config import Config
from utils.display import updateDisplayDiscord

argparser = argparse.ArgumentParser(
        description="THO ENCUERA GRABBER DISCORD : https://discord.gg/tfRuSC52Da",
        epilog="BY TODO HACK OFFICIAL"
    )
argparser.add_argument(
    "filename",
    help="File to deobfuscate"
)
argparser.add_argument(
    "-d", "--download",
    help="Download the file from a link",
    action="store_true"
)
argparser.add_argument(
    "-j", "--json",
    help="output details in a json format",
    action="store_true"
)
args = argparser.parse_args()


def ifprint(message):
    if not args.json:
        print(message)


def main():
    JSON_EXPORT = {
        "type": None,
        "webhook": None,
        "pyinstaller_version": "0",
        "python_version": "0"
    }
    if args.download:
        ifprint("[+] Downloading file")
        filename = TryDownload(args.filename)
        ifprint("[+] File downloaded")
    else:
        if not os.path.exists(args.filename):
            ifprint("[-] This file does not exist")
            exit(1)
        filename = args.filename
    filename = os.path.abspath(filename)
    webhook = ""
    if not (exists(join(dirname(__file__), "temp"))):
        os.makedirs(join(dirname(__file__), "temp"))
    if ".jar" in filename:
        ifprint("[+] Java grabber suspected, scanning strings...")
        javadir = unzipJava(filename)
        ben = BenDeobf(javadir)
        webhook = ben.Deobfuscate()
        JSON_EXPORT["type"] = "java grabber"
    else:
        if checkUPX(filename):
            print("[!] File packed with UPX")
        try:
            archive = ExtractPYInstaller(filename)
            JSON_EXPORT["pyinstaller_version"] = str(archive.pyinstVer)
            JSON_EXPORT["python_version"] = "{0}.{1}".format(archive.pymaj, archive.pymin)
        except ExtractionError as e:
            ifprint(e)
            exit(1)

        extractiondir = join(os.getcwd())
        obfuscators = [
            BlankDeobf,
            LunaDeobf,
            VespyDeobf,
            OtherDeobf,
            NotObfuscated
        ]
        for deobfuscator in obfuscators:
            try:
                ifprint(f"[!] Trying {deobfuscator.__name__} method")
                deobf = deobfuscator(extractiondir, archive.entrypoints)
                webhook = deobf.Deobfuscate()
                if webhook:
                    JSON_EXPORT["type"] = deobfuscator.__name__
                    break
            except:
                continue
    
    if webhook == "" or webhook is None:
        ifprint("[-] No webhook found.")
        sys.exit(1)

    JSON_EXPORT["webhook"] = webhook
    if args.json:
        print(json.dumps(JSON_EXPORT))
        exit(0)
    if type(webhook) != str:
        ifprint(f"[+] Found multiple webhooks")
        for web in webhook:
            webh = Webhook(web)
            if webh.CheckValid(web):
                ifprint(f"[+] Valid webhook: {web}")
            else:
                ifprint(f"[-] Invalid webhook: {web}")
    elif type(webhook) == str and "discord" in webhook:
        web = Webhook(webhook)
        if not web.CheckValid(webhook):
            ifprint(f"[-] Invalid webhook: {webhook}")
        else:
            web.GetInformations()
            ifprint(f"[+] Valid webhook: {webhook}")
            i = 0
            while True:
                choice = input(
                    """
                      ████████╗██╗  ██╗ ██████╗ 
                      ╚══██╔══╝██║  ██║██╔═══██╗
                         ██║   ███████║██║   ██║
                         ██║   ██╔══██║██║   ██║
                         ██║   ██║  ██║╚██████╔╝
                         ╚═╝   ╚═╝  ╚═╝ ╚═════╝ 
                    """
                    + "\nPor favor, seleccione una opción:\n"
                    + "[1] - Eliminar webhook\n"
                    + "[2] - Enviar spam al webhook\n"
                    + "quit - Salir\n-> "
                )
                if choice == 'quit':
                    sys.exit(0)
                choice = int(choice)
                match choice:
                    case 1:
                        try:
                            web.DeleteWebhook()
                            ifprint("[+] Webhook Deleted")
                        except IOError as e:
                            ifprint(e)
                        break
                    case 2:
                        while True:
                            try:
                                web.SendWebhook()
                                i += 1
                                updateDisplayDiscord(i, web)
                                time.sleep(0.8)
                            except IOError as e:
                                ifprint(e)
                                break
    else:
        webhook, chat_id = webhook.split('$')
        web = Telegram(webhook)
        if not Telegram.CheckValid(webhook):
            ifprint("[-] Invalid Telegram bot token")
        else:
            web.GetInformations()
            ifprint("[+] Valid Telegram bot found")
            ifprint(f"Token: {web.token}")
            ifprint(f"Username: {web.username}")
            ifprint(f"First Name: {web.firstName}")
            ifprint(f"Can dump messages?: {web.dump}")
            ifprint("[-] Spamming not yet implemented")
            # I need to test telegram, but I forgot my telegram password 💀
            # index = 0
            # while True:
            #     try:
            #         #web.SendMessage(chat_id)
            #         index += 1
            #         updateDisplayTelegram(index, web)
            #     except IOError as e:
            #         print(e)
            #         break


if __name__ == '__main__':
    cfg = Config()
    main()
    if Webhook.GetDeleteConfig():
        shutil.rmtree(join(dirname(__file__), "temp"))
