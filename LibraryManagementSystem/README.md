##README - Documentation des requêtes SQL##

Ce document décrit les requêtes SQL utilisées pour gérer une base de données d'étudiants, de cours et d'inscriptions.

Les tables principales de la base de données sont Students, Courses, et Enrollments. La table Students contient les informations sur les étudiants, telles que l'identifiant, le nom, l'âge et le genre. La table Courses contient les détails des cours, y compris l'identifiant du cours, son nom, le nombre de crédits associés et la capacité maximale. La table Enrollments sert à enregistrer les inscriptions des étudiants aux différents cours, en reliant les identifiants des étudiants et des cours avec des clés étrangères pour assurer l'intégrité référentielle.

Les données sont insérées dans ces tables via des requêtes INSERT. Par exemple, des informations sur les étudiants, les cours et les inscriptions sont ajoutées, avec chaque étudiant pouvant être inscrit à plusieurs cours. Les inscriptions sont ensuite enregistrées dans la table Enrollments, créant ainsi des relations entre les étudiants et les cours auxquels ils sont inscrits.

Des requêtes de sélection sont également utilisées pour récupérer des informations, telles que la liste des étudiants inscrits dans des cours, le nombre total de crédits pour chaque étudiant, ou les cours qui n'ont pas encore d'inscription. Des filtres et des regroupements sont appliqués pour extraire des données spécifiques, comme les étudiants inscrits au plus grand nombre de cours ou ceux inscrits dans des cours dépassant une certaine capacité.

Enfin, des actions de suppression sont utilisées pour supprimer des étudiants ou des inscriptions, tout en garantissant que l'intégrité des données est maintenue, par exemple en supprimant les étudiants qui ne sont inscrits à aucun cours.

Les requêtes SQL sont conçues pour garantir la cohérence des données, optimiser les performances avec des jointures et des agrégations, et gérer les contraintes telles que la capacité des cours.











Système de Gestion de Bibliothèque
Ce projet implémente un système de gestion de bibliothèque en utilisant la Programmation Orientée Objet (POO) en Python. Le système permet de gérer des livres, d'ajouter de nouveaux livres, de les emprunter, de les rendre et de les rechercher. Il inclut également un mécanisme de persistance des données permettant de sauvegarder et de charger les informations des livres à partir d'un fichier texte.

Fonctionnalités
Ajouter un livre : Permet d'ajouter un livre à la bibliothèque en précisant son titre et son auteur.
Lister les livres : Affiche tous les livres disponibles dans la bibliothèque.
Rechercher un livre : Recherche un livre par son titre ou son auteur.
Emprunter un livre : Permet à un étudiant d'emprunter un livre s'il est disponible.
Rendre un livre : Permet à un étudiant de rendre un livre emprunté.
Limiter les emprunts : Chaque étudiant peut emprunter un maximum de 3 livres à la fois.
Sauvegarder et charger les livres : Sauvegarde les livres dans un fichier texte et charge les livres à partir de ce fichier lors du démarrage du système.