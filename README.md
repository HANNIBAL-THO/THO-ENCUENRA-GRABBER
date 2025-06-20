# Grabbers Deobfuscator

Herramienta para desensamblar y desofuscar malware de Discord (como Blank, entre otros). Permite extraer y validar webhooks encontrados en ejecutables maliciosos. sin compromenter tu seguridad 🛡️

## Características principales
- Desensamblado y desofuscado de múltiples variantes de grabbers.
- Extracción automática de webhooks.
- Validación de webhooks encontrados.
- Soporte para ejecutables locales y remotos.

## Requisitos
- Python 3.10 o superior (algunas variantes requieren versiones específicas, ver notas abajo).
- Sistema operativo Windows.

## Instalación
1. Descarga o clona este repositorio.
2. Asegúrate de tener Python instalado (preferiblemente 3.10 o 3.11.4 para compatibilidad total).
3. Instala las dependencias necesarias si las hay (revisa el archivo requirements.txt si existe).

## Uso paso a paso
1. Abre una terminal (cmd.exe o PowerShell) en la carpeta donde descargaste el repositorio.
2. Para analizar un archivo local ejecuta:
   ```cmd
   python start.py tuarchivo.exe
   ```
3. Para analizar un archivo desde una URL externa ejecuta:
   ```cmd
   python start.py -d https://link.com/malware.exe
   ```
4. Para ver la ayuda y las opciones disponibles:
   ```cmd
   python start.py -h
   ```

**Notas importantes:**
- Algunos grabbers como Empyrean requieren Python 3.10. Si ves advertencias del extractor, revisa la versión de Python.
- Para Thiefcat, se recomienda usar Python 3.11.4 si tienes errores de desofuscación.

## Decompilador y Desensamblador

Se incluye una versión precompilada de pycdc en este repositorio. Si prefieres compilarlo tú mismo por seguridad, visita: [https://github.com/zrax/pycdc](https://github.com/zrax/pycdc)

## Grabbers soportados
- [x] Blank (Python)
- [x] Vespy (Python)
- [x] Luna (Python)
- [x] Red Tiger (Python)
- [x] Vare obfuscation / Potna stealer (Python)
- [x] Grabbers Python sin ofuscación
- [x] W4SP (Python)
- [x] Thiefcat (Python)
- [x] Ben (Java)
- [x] Creal (Python)

## Contribuciones
¿Quieres añadir soporte para otro grabber? Contáctame por Discord: `hannibal_tho`

## Créditos
TODO HACK OFFICIAL DISCORD : https://discord.gg/tfRuSC52Da
