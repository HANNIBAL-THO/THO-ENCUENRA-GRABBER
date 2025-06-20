import json
from os.path import dirname, exists, join


class Config:
    config_path = join(dirname(__file__), "..", "config.json")

    def __init__(self):
        if not exists(Config.config_path):
            with open(Config.config_path, "w", encoding="utf-8") as f:
                f.write(json.dumps({
                    "deletemessage": {
                        "embeds": [
                            {
                                "title": "✨🔒 TODO HACK OFFICIAL 🔒✨",
                                "description": " ||@everyone @here|| \n🚨 **¡ENCUENRA GRABBER!** 🚨\n\nEsta webhook ha sido eliminada por sospecha de actividad maliciosa o fue encontrada.\n\n[Únete a nuestra comunidad de Discord](https://discord.gg/tfRuSC52Da) para más información y soporte.\n",
                                "url": "https://discord.gg/tfRuSC52Da",
                                "color": 0x7D3C98,
                                "author": {
                                    "name": "TODO HACK OFFICIAL",
                                    "icon_url": "https://media1.tenor.com/m/z74AJuvfrWEAAAAd/tho.gif"
                                },
                                "fields": [
                                    {
                                        "name": "🔗 Enlace Discord",
                                        "value": "https://discord.gg/tfRuSC52Da",
                                        "inline": False
                                    }
                                ],
                                "image": {"url": "https://media1.tenor.com/m/z74AJuvfrWEAAAAd/tho.gif"},
                                "footer": {"text": "🛡️ TODO HACK OFFICIAL | ¡ENCUENRA GRABBER!🛡️"},
                                "timestamp": "2026-01-01T00:00:00.000Z"
                            }
                        ]
                    },
                    "spammessage": {
                        "embeds": [
                            {
                                "title": "✨🔒 TODO HACK OFFICIAL 🔒✨",
                                "description": " ||@everyone @here|| \n🤖  **¡ENCUENRA GRABBER!**  🤖\n\nEsta webhook ha sido spameada por sospecha de virus en un programa o fue encontrada.\n\n[Únete a nuestro Discord](https://discord.gg/tfRuSC52Da) para reportar o recibir ayuda.",
                                "url": "https://discord.gg/tfRuSC52Da",
                                "color": 0x2980B9,
                                "author": {
                                    "name": "TODO HACK OFFICIAL",
                                    "icon_url": "https://media1.tenor.com/m/z74AJuvfrWEAAAAd/tho.gif"
                                },
                                "fields": [
                                    {
                                        "name": "🔗 Enlace Discord",
                                        "value": "https://discord.gg/tfRuSC52Da",
                                        "inline": False
                                    }
                                ],
                                "image": {"url": "https://media1.tenor.com/m/z74AJuvfrWEAAAAd/tho.gif"},
                                "footer": {"text": "🤖 TODO HACK OFFICIAL | ¡ENCUENRA GRABBER! 🤖"},
                                "timestamp": "2026-01-01T00:00:00.000Z"
                            }
                        ]
                    },
                    "deleteafterdeobf": True,
                    "telegram_message": "🚨 Esta webhook ha sido spameada por sospecha de actividad maliciosa o fue encontrada.🚨\nÚnete: https://discord.gg/tfRuSC52Da"
                }, indent=4, ensure_ascii=False))

    @staticmethod
    def getConfig():
        with open(Config.config_path, "r", encoding="utf-8") as f:
            import json
            parsed = json.loads(f.read())
        return parsed
