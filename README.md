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

Run app:
```
make docker
```

##### Access admin panel #####

On your favorite browser go to:

localhost:8000/admin/

and login using the superuser credidentials you created in createsuperuser step

##### ENDPOINTS #####
              
/api/account/token/             Get JWT token

/api/account/create/            Create account

/api/account/token/refresh/     Refresh JWT token

/api/account/<int:pk>/          Get users info

/api/recipes/                   List of all recipes

/api/ingredients/               List/Create ingredients

/api/recipes/create/            Create recipe

/api/recipes/rate/              Rate recipe

/api/recipes/?search=STRING     Search recipes that contain STRING in name, recipe_text or ingredients

/api/recipes/?max_ing_num=INT   Show recipes with INT max num of ingredients

/api/recipes/?min_ing_num=INT   Show recipes with INT min num of ingredients


###### AUTHOR ######

Ivan Miletic
