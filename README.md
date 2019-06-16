EVirus - Création de virus libre d'accès
==========================================

Ce module est conçu pour rendre plus facile d'accès la création de virus.
Ne pas utiliser ce module sans l'accord de la victime.

Vous pouvez l'installer avec pip:

    > pip install evirus

Exemple d'usage:

    >>> from evirus import Virus,on_startup
    >>> app = Virus(on_startup(), "name")

Documentation:
	
	DOCUMENTATION.md

Ce code est sous licence WTFPL.