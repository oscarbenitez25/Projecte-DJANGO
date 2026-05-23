# Blog Django - M485 BLOC 6

Blog desenvolupat amb Django com a projecte d'aprenentatge.

## Descripció

Aplicació web de blog amb posts, autors i etiquetes. Permet veure els darrers posts, 
llistar tots els posts, veure el detall de cada post, llistar autors i etiquetes.

## Instal·lació

1. Clona el repositori:
```bash
git clone <url-del-repositori>
cd geeks_site
```

2. Instal·la les dependències:
```bash
pip install django
```

3. Executa les migracions:
```bash
python manage.py migrate
```

4. Crea un superusuari:
```bash
python manage.py createsuperuser
```

## Execució

```bash
python manage.py runserver
```

Obre el navegador a `http://127.0.0.1:8000/`

## Rutes disponibles

- `/` — Pàgina d'inici amb els 3 darrers posts
- `/posts` — Llistat de tots els posts
- `/posts/<slug>` — Detall d'un post
- `/authors` — Llistat de tots els autors
- `/authors/<id>` — Detall d'un autor
- `/tags` — Llistat de totes les etiquetes
- `/tags/<id>` — Posts d'una etiqueta
- `/admin` — Panell d'administració

## Tests

```bash
python manage.py test
```

## Models

- **Author** — Nom, cognom i email
- **Tag** — Etiqueta amb nom únic
- **Post** — Títol, excerpt, contingut, data, slug, autor i etiquetes