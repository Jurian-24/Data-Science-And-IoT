
# Data Sience And IoT

## Introductie

Dit project is voor het keuzevak Data Science and IoT, op de Hogeschool Rotterdam. Ik heb dan ook mijn uiterste best gedaan om een goed en werkend project neer te zetten. Hiervoor heb ik een aantal dingen gebruikt namelijk: 




- Raspberry 4
- Python 3
- Een afstand sensor (HC-SR04)
- Male & Female bedradingen
- Ionic (voor de mobile app)
- Gpiozero (librarie voor de afstand sensor)
## De gedachte achter dit project

De afgelopen tijd ben ik steeds meer gaan letten op lichaamstaal bij mensen waar ik een gesprek mee heb. Hier kan ik meestal zien of ze het gesprek leuk vinden of niet. Door wat zelfstandig onderzoek te doen ben ik erachter gekomen dat mensen vaak verder van je af staan als ze het gesprek niet leuk vinden of niet interessant genoeg vinden. Dit wilde ik graag testen!

Ik ben gaan nadenken over hoe ik een afstand sensor kan gaan gebruiken om te bepalen of mensen het gesprek leuk of niet leuk vinden.

## Installaties

**Raspberry Pi**

Als je een Raspberry Pi heb aangeschaft staat er hoogstwaarschijnlijk al een versie van Python op met de bijbehorende libraries. Om dit te checken voeren we een paar commando's uit.

Voor de python versie:
```bash
python --version

Of

python3 --version
```

Nu we weten of Python geinstalleerd is kunnen we kijken wat de versie is van de library van Gpiozero. Maak een bestand aan genaamd: main.py.

Plaats hier de volgende regels code in: 
```python
from pkg_resources import require

print(f'Version -> {require("gpiozero")[0].version}')
```

Voer dit bestand vervolgens uit. Als het goed is moet er iets staan zoals:

```bash
Version -> 1.6.5
```

**Ionic**



Mocht een van de commando's geen versie weergeven scroll dan verder naar wat er mist en voer de stappen uit voor het installatie proces.

**Python**

Voor dit project heb je minimaal Python 3 nodig. Open hiervoor een command prompt/terminal op je computer en voer het volgende commando uit:

Voor windows:
https://phoenixnap.com/kb/how-to-install-python-3-windows

Voor MacOS:
```bash
$ brew install python3
```

Voor Linux:
```bash
$ sudo apt-get install python3.6
```

