
# Fifth Class 

<details>
<summary><b>Multiple Apps and Models</b></summary>

### 1. Project Setup
 You need to add your apps, `myapp` and `yourapp`, to the `INSTALLED_APPS` list in the `settings.py` file. This tells Django to include these apps in the project.To ensure that Django recognizes and uses the specified applications in the project.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'yourapp',
]
```

### 2. Defining Models
Create model classes in `models.py` files within your apps. Each class represents a database table, and each attribute within the class represents a column in that table.To define the database structure through Django models.

#### `myapp/models.py`
The `myapp` includes models for students, teachers, workers, subjects, and classes. Each model has attributes representing various fields and a `__str__` method to define how the objects are displayed as strings.

```python
from django.db import models

class studentModel(models.Model):
    name = models.CharField(max_length=50)
    stdid = models.CharField(max_length=20)

    def __str__(self):
        return self.name + "-" + self.stdid

class teacherModel(models.Model):
    name1 = models.CharField(max_length=50)
    tchid = models.CharField(max_length=50)

    def __str__(self):
        return self.name1

class workerModel(models.Model):
    name2 = models.CharField(max_length=20)
    workid = models.CharField(max_length=20)

    def __str__(self):
        return self.name2

class subjectModel(models.Model):
    name3 = models.CharField(max_length=20)
    subid = models.CharField(max_length=20)

    def __str__(self):
        return self.name3

class classModel(models.Model):
    name4 = models.CharField(max_length=20)
    classid = models.CharField(max_length=50)

    def __str__(self):
        return self.name4
```

#### `yourapp/models.py`
The `yourapp` includes models for blogs and lists, each with relevant attributes and a `__str__` method.

```python
from django.db import models

class blogModel(models.Model):
    name11 = models.CharField(max_length=20)
    blid = models.CharField(max_length=20)

    def __str__(self):
        return self.name11

class listModel(models.Model):
    name12 = models.CharField(max_length=20)
    liid = models.CharField(max_length=20)

    def __str__(self):
        return self.name12
```

</details>

<details>
<summary><b>Registering Models in Admin Panel</b></summary>

### 3. Registering Models in Admin Panel
Register each model in `admin.py` so they appear in the admin panel for management.To make your models accessible through the Django admin interface.

#### `myapp/admin.py`
This file registers the models from `myapp` to the admin interface.

```python
from django.contrib import admin
from myapp.models import studentModel, teacherModel, workerModel, subjectModel, classModel

admin.site.register(studentModel)
admin.site.register(teacherModel)
admin.site.register(workerModel)
admin.site.register(subjectModel)
admin.site.register(classModel)
```

#### `yourapp/admin.py`
This file registers the models from `yourapp` to the admin interface.

```python
from django.contrib import admin
from yourapp.models import blogModel, listModel

admin.site.register(blogModel)
admin.site.register(listModel)
```

</details>

<details>
<summary><b>Apply Changes to Database</b></summary>

### 4. Applying Migrations
Run these commands in your terminal to make and apply migrations. To create and apply changes to your database schema based on the defined models.
```sh
python manage.py makemigrations
python manage.py migrate
```

### 5. Running the Server
Run this command in your terminal,To start the Django development server and view your application.
```sh
python manage.py runserver
```

</details>

<details>
<summary><b>Accessing the Admin Panel</b></summary>

### 6. Accessing the Admin Panel
 Open a web browser and go to `http://127.0.0.1:8000/admin/`, then log in with your superuser account. You will see your registered models and can add, edit, or delete records.To use the Django admin interface to manage your data.

</details>

<details>
<summary><b>Viewing Data in SQLite</b></summary>

### 7. Viewing Data in SQLite
Use a tool like DB Browser for SQLite to open `db.sqlite3`, the database file located in your Django project's root directory. This allows you to see the data stored in your models.To directly view and manage your database tables.

</details>

<details>
<summary><b>Class Topic Review</b></summary>

- [x] Setup `INSTALLED_APPS` in `settings.py`
- [x] Define models in `myapp/models.py`
- [x] Define models in `yourapp/models.py`
- [x] Register models in `myapp/admin.py`
- [x] Register models in `yourapp/admin.py`
- [x] Apply migrations (`makemigrations`, `migrate`)
- [x] Run the development server (`runserver`)
- [x] Access the Django admin panel
- [x] View data in SQLite using DB Browser

</details>