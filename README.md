# P13-blog

## Problématique
Dans le cadre d'un blog, l'auteur ne souhaite pas rédiger en ligne les différents articles et tutoriels mis à la disposition des visiteurs.

Il souhaite rédiger sur son ordinateur un fichier de type markdown et l’importer à l’aide de l’application web afin qu’elle génère immédiatement la page web correspondante et la rende disponible à la consultation.

## Objectifs
- Prérequis : Créer un site web présentant un canevas simple de type blog, à savoir :
    -	Page d’accueil proposant un menu de navigation et la présentation de l’auteur.
    -	Possibilité de consulter les catégories d’article et de naviguer entre celles-ci.
    -	Possibilité de consulter ces articles.
    -	Possibilité d’envoyer un e-mail au bloggeur pour réagir à ces articles.
    -	Possibilité d’activer ou de désactiver un mode sombre.

- Objectif principal : Implémenter une fonctionnalité accessible au super utilisateur, lorsqu’il est connecté, qui autorise :
    -	d’importer un fichier de type Markdown (.md) répondant à des exigences définies.
    -	de parser son contenu et d’en extraire les différents éléments.
    -	de vérifier la compatibilité de ces éléments ainsi que leur unicité.
    -	d’implémenter la page web correspondante.
    -	de la rendre immédiatement accessible à la consultation.

- Finalité : Mettre en ligne ce site web sur https://blog.slb-fullweb.tech :
    -	Framework utilisé : Django.
    -	Serveur WSGI : Gunicorn.
    -	Serveur et reverse-proxy : NginX.
    -	Conteneurisation des différents éléments à l’aide de Docker.
    -	Stockage des images Docker sur un repository AWS ECR.
    -	Mise en ligne sur une instance AWS EC2 pointée par une adresse Elastic IP fixe.
    -	Dissociation de la base de données PostgreSQL sur une instance AWS RDS

