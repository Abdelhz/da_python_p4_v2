# da_python_p4_v2

# Project : le logiciel "Programme d'échecs" écris en Python, est une application de gestion de tournois de jeux d'échecs fonctionnant avec le modèle suisse.

# Création d'un environnement virtuel (env) pour le programme d'échecs  :

Nous devons tout d'abord créer un environnement virtuel python.

**NOTE :** Nous utilisons *python 3.9*

*Création d'un répertoir pour le projet :*

On ouvre d'abord un terminal (Si sous windows utiliser Git bash ou similaire pour les commandes unix)

**mkdir programme_echecs**

Création de l'env avec *venv*

**cd programme_echecs**

**python -m venv env_programme_echecs**

A ce moment l'env est créé et il nous suffit de l'activer.

# Activer l'env :

Il faut pour cela naviguer dans le dossier *scrips* ou appelé "*bin*" sous linux, contenu dans le répertoir env_programme echecs;

**cd env_programme_echecs/scripts**

**source activate**

L'env est maintenant activé.

# Installation des bibliothèques requises dans l'env :

Nous n'installerons en plus que le module TinyDB.

*Revenir au répertoire du projet.*
*Mettre le fichier "requirements.txt" dans ce répertoire.*

*Lancer la commande :*

**pip install -r requirements.txt**

# Lancerment et execution du programme :

Après avoir téléchargé les fichiers, créer un répertoire qui contiendra les fichier du programme téléchargés;
**cd path-to/programme_echecs**
**mkdir programme**
*Mettre le fichier "main_chess.py" et le répertoire "app_files" dans le répertoire "programme"
Via le terminal, acceder au répertoire programme;
**cd programme**
**Le lancement du programme se fait avec la commande suivante**
**python main_chess.py**

# Utilisation du programme

Au lancement di programme, un menu est affiché avec 3 option différentes:

*l'option 1 nous permet de créer un nouveau tournoi*

Durant cettre procedure il nous est demandé d'introduire un nombre d'informations specifique dont la liste des joueurs participant au tournoi.
Il est possible de stopper le tournoi en cours mais seulement après la fin d'un tour (round).
Dans ce cas les informations du tournoi sont sauvegardé pour une reprise ulterieur.

*l'option 2 nous permet de reprendre un tournoi passé*

Durant cette procedure il est possible de reprendre un tournoi passé, sachant qu'il peut y avoir plus d'un tournoi interrompu (une liste de ces tournoi non achevé sera affichée), il faudra donc saisir le nom du tournoi à finir.
Comme pour l'option 1, il est aussi possible d'interromptre un tournoi après sa reprise mais toujour seulement après la fin d'un tour.

**Pour l'option 1 et 2 :**

Si un tournoi est achevé il nous est donnée la possibilité de mettre à jour le rang de chaque joueur ayant participé au tournoi.


*l'option 3 nous permet de mettre à jour le rang des joueur*

Une liste de tout les joueurs ayant participé aux tournois est affichée,il nous sera alors demandé si nous voulons proceder à des modification, si oui, nous avons alors la possibilité de modifier le rang d'un joueur en introduisant sont nom.
Après chaque modification nous avons la mossibilité de continuer ou de revenir au menu principale.

*l'option 4 nous permet de fermer le programme.*

#Liste des fichiers :

*Dans "programme_echecs/programme/" :*
**main_chess.py**

*Dans "programme_echecs/programme/app_files/" :*

**controller_chess.py**
**initialisation.py**
**model_chess.py**
**services_chess.py**
**view_chess.py**


**Souvegarde des données**

La souvegarde des donnée se fait dans un fichier db.json dans "programme_echecs/programme/data/" 

**Verification du programme avec flake8 :**

En utilisant le terminal sur le répertoire "programme_echecs/programme/"
executer la commande suivante :

**flake8 --format=html --htmldir=flake-report**

un repertoire nommé "flake-report" sera créé, dedans sera contenu un fichier "index.html" qui temoignera du respect ou non de la PEP8 sur l'ecriture de tout les fichiers du programme.
