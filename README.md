# Bienvenue sur Reflex !

Ceci est le modèle de base Reflex - installé lorsque vous exécutez `reflex init`.

Si vous souhaitez utiliser un modèle différent, passez le drapeau `--template` à `reflex init`.
Par exemple, si vous voulez un point de départ plus basique, vous pouvez exécuter :

```bash
reflex init --template blank
```

## À propos de ce modèle

Ce modèle présente la structure de répertoire suivante :

```bash
├── README.md
├── assets
├── rxconfig.py
└── {votre_app}
    ├── __init__.py
    ├── components
    │   ├── __init__.py
    │   ├── navbar.py
    │   └── sidebar.py
    ├── pages
    │   ├── __init__.py
    │   ├── about.py
    │   ├── index.py
    │   ├── profile.py
    │   ├── settings.py
    │   └── table.py
    ├── styles.py
    ├── templates
    │   ├── __init__.py
    │   └── template.py
    └── {votre_app}.py
```

Consultez la [documentation sur la structure du projet](https://reflex.dev/docs/getting-started/project-structure/) pour plus d'informations sur la structure générale d'un projet Reflex.

### Ajout de pages

Dans ce modèle, les pages de votre application sont définies dans `{votre_app}/pages/`.
Chaque page est une fonction qui renvoie un composant Reflex.
Par exemple, pour modifier cette page, vous pouvez modifier `{votre_app}/pages/index.py`.
Consultez la [documentation sur les pages](https://reflex.dev/docs/pages/routes/) pour plus d'informations sur les pages.

Dans ce modèle, au lieu d'utiliser `rx.add_page` ou le décorateur `@rx.page`,
nous utilisons le décorateur `@template` de `{votre_app}/templates/template.py`.

Pour ajouter une nouvelle page :

1. Ajoutez un nouveau fichier dans `{votre_app}/pages/`. Nous recommandons d'utiliser un fichier par page, mais vous pouvez également regrouper les pages dans un seul fichier.
2. Ajoutez une nouvelle fonction avec le décorateur `@template`, qui prend les mêmes arguments que `@rx.page`.
3. Importez la page dans votre fichier `{votre_app}/pages/__init__.py` et elle sera automatiquement ajoutée à l'application.
4. Organisez les pages dans `{votre_app}/components/sidebar.py` et `{votre_app}/components/navbar.py`.

### Ajout de composants

Pour garder votre code organisé, nous recommandons de placer les composants qui sont
utilisés sur plusieurs pages dans le répertoire `{votre_app}/components/`.

Dans ce modèle, nous avons un composant de barre latérale dans `{votre_app}/components/sidebar.py`.

### Ajout d'état

Lorsque votre application grandit, nous recommandons d'utiliser les [sous-états](https://reflex.dev/docs/substates/overview/)
pour organiser votre état.

Vous pouvez soit définir les sous-états dans leurs propres fichiers, soit si l'état est
spécifique à une page, vous pouvez le définir dans le fichier de la page elle-même.
