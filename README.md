# README #

## Food recipes test ##

#### REQUIREMENTS ####

Docker installed on your machine

##### SETUP #####

Makemigrations using this command:

```
make django-makemigrations
```

Migrate changes using this command:
```
make django-migrate
```

Create superuser for admin panel:

```
make django-createsuperuser
```

Run tests:

```
make test
```

Run app:
```
make docker
```

##### Access admin panel #####

On your favorite browser go to:

localhost:8000/admin/

and login using the superuser credidentials you created in createsuperuser step

##### ENDPOINTS #####
              
_/api/account/token/_ - Get JWT token

_/api/account/create/_ - Create account

_/api/account/token/refresh/_ - Refresh JWT token

_/api/account/<int:pk>/_ - Get users info

_/api/recipes/_ - List of all recipes

_/api/ingredients/_ - List/Create ingredients

_/api/recipes/create/_ - Create recipe

_/api/recipes/rate/_ - Rate recipe

_/api/recipes/?search=STRING_ - Search recipes that contain STRING in name, recipe_text or ingredients

_/api/recipes/?max_ing_num=INT_ - Show recipes with INT max num of ingredients

_/api/recipes/?min_ing_num=INT_ - Show recipes with INT min num of ingredients


###### AUTHOR ######

Ivan Miletic
