# Elo light control #

## But : ##

Le but de ce project est de controller les lumières de l'atelier avec un interface graphique sur l'écran tactile du Raspberry Pi 3B+.

## Requirement ##

pip install -U -r requirements.txt

## Test ##

./test/flask_test.py

Lancer ce fichier pour tester le serveur flask.

## Doc ##

./doc/

main.html

Fichier contenant la doc du code auto générée par [Pdoc3](https://pypi.org/project/pdoc3/).

### Pdoc3 ###

```
pip install pdoc3
pdoc -o doc --html main.py
```

ou

```
pdoc -o doc --html main.py --force
```

## launching the app ##

sudo python3 main.py

/!\ sudo est utilisé (sur linux) pour authoriser l'utilisaton du port 80.

Pour utiliser le server complétement référez vous aux XWiki.

## Liens ##

[Gitlab](http://172.16.32.230/Forestier/controle-des-lumieres-knx)

[XWiki](https://xwiki.serverelo.org/xwiki/bin/view/Centre%20de%20Formation%20ELO/Projets/Controle%20des%20lumières%20KNX/)

## ##

Robin Forestier 2021 / 2022
