# Blog Django - M485 BLOC 6

## Introducció

Blog desenvolupat amb Django com a projecte d'aprenentatge del mòdul de Programació (M485). L'objectiu principal és crear una aplicació web de blog amb posts, autors i etiquetes, utilitzant el patró MVT (Model-Vista-Template) de Django.

## Requisits previs

- Python 3.12 o superior
- pip

## Instal·lació ràpida

1. Clona el repositori:
```bash
git clone https://github.com/oscarbenitez25/Projecte-DJANGO.git
cd Projecte-DJANGO
```

2. Instal·la les dependències:
```bash
pip install -r requirements.txt
```

3. Executa les migracions:
```bash
python manage.py migrate
```

4. Crea un superusuari (opcional, per accedir al panell d'administració):
```bash
python manage.py createsuperuser
```

## Execució del projecte

```bash
python manage.py runserver
```

Obre el navegador a: http://127.0.0.1:8000/

## Rutes disponibles

| Ruta | Descripció |
|------|------------|
| `/` | Pàgina d'inici amb els 3 darrers posts |
| `/posts` | Llistat de tots els posts |
| `/posts/<slug>` | Detall d'un post |
| `/authors` | Llistat de tots els autors |
| `/authors/<id>` | Detall d'un autor amb els seus posts |
| `/tags` | Llistat de totes les etiquetes |
| `/tags/<id>` | Posts d'una etiqueta |
| `/admin` | Panell d'administració |

## Models

- **Post** — títol, excerpt, contingut, data, slug, imatge, autor i etiquetes
- **Author** — nom, cognom, email i imatge
- **Tag** — nom i imatge

## Tests

```bash
python manage.py test
```

## Documentació

La documentació dels fitxers Python es genera automàticament amb Pydoc. Pots consultar-la aquí: [Documentació](#)
