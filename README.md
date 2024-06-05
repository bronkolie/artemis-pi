Dit is de github repo voor alle code voor project 1.4 groep Artemis

# Hoe te gebruiken:

Alle nodige bestanden voor de RGM bevinden zich in ~/Artemis/RGM

## Virtual environment
Je moet in de juiste virtual environment zitten om de libraries te kunnen gebruiken. Dit doe je met het commando "source env/bin/activate" uit te voeren wanneer je in de Artemis/ directory zit.

## Config file:
De configuration file is rgm.conf. Deze kan je gebruiken om de pinnummers te veranderen, af te stellen hoe lang de hovercraft zal bewegen, en af te stellen hoe gevoelig de licht- en ir-sensoren zijn. Als je hier pinnummers verandert, denk eraan om de wiring schematic te updaten.

## Wiring schematic:
Alle informatie voor de wiring schematic staat in wiring.txt. De pinnummers kunnen geupdatet orden met updatewiring.py

## Sensoren afstellen:
De sensoren kunnen afgesteld worden met tune_ir_sensor.py en lune_light_sensor.py


## RGM activeren:
De RGM kan geactiveerd worden met rgm.py