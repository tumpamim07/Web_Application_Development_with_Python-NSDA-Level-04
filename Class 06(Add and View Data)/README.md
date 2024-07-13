# Sixth Class (Add & View Data)

<details>
<summary>Install Django, Create Project and App</summary>

### Step 1: Install Django

Ensure Django is installed in your Python environment using pip:

```bash
pip install django
```

### Step 2: Start a New Django Project

Create a new Django project named `myproject`:

```bash
django-admin startproject myproject
```

This command initializes a new Django project with a default directory structure and necessary configuration files.

### Step 3: Create a New Django App

Generate a new app named `myApp` within your project:

```bash
python manage.py startapp myApp
```

Creating an app in Django organizes related functionalities such as models, views, and templates into modular components.
</details>

<details>
<summary>Settings</summary>

### Step 4: Configure Settings

In `settings.py`, configure the `INSTALLED_APPS` list to include your app (`myApp`) and define the template directory:

```python
# settings.py

INSTALLED_APPS = [
    ...
    'myApp',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'template'],  # Adjust 'template' to your actual template directory
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                ...
            ],
        },
    },
]
```

- **INSTALLED_APPS**: Includes all Django applications used in the project. Adding `'myApp'` ensures Django recognizes the app and its components.
  
- **TEMPLATES**: Defines the configuration for Django's template engine. `DIRS` specifies where Django should look for HTML templates.
</details>

<details>
<summary>Models and Admin Register</summary>

### Step 5: Define Models

Define your models (`StudentModel` and `TeacherModel`) in `models.py` within `myApp`:

```python
# myApp/models.py

from django.db import models

class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    stdid = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)

    def __str__(self):
        return self.name+"-"+self.stdid+"-"+self.dept

class TeacherModel(models.Model):
    tecname = models.CharField(max_length=50)
    tecid = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.tecname+"-"+self.tecid+"-"+self.subject
```

- **Models**: Models are Python classes that define the structure and behavior of data stored in the database. Each model class corresponds to a database table.

### Step 6: Register Models in Admin

Register your models in `admin.py` to manage them via the Django admin interface:

```python
# myApp/admin.py

from django.contrib import admin
from myApp.models import *

admin.site.register(StudentModel)
admin.site.register(TeacherModel)
```

- **Admin**: Django admin is a built-in application for managing the project's data models via a web interface. Registering models allows CRUD operations (Create, Read, Update, Delete) through the admin site.
</details>

<details>
<summary>Migrations and Migrate</summary>

Before using your models, you need to apply migrations to create the database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```
</details>

<details>
<summary>Views</summary>

### Step 7: Define Views

Create views in `views.py` to handle HTTP requests and render HTML templates:

```python

from django.shortcuts import render, redirect, HttpResponse
from myApp.models import *

def Home(request):
    return HttpResponse("Hello")

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def studentpage(request):
    student = StudentModel.objects.all()
    dict = {
        'std': student 
    }
    return render(request, 'studentpage.html', dict)

def teacherpage(request):
    teacher = TeacherModel.objects.all()
    mydict = {
        'teach': teacher
    }
    return render(request, 'teacherpage.html', mydict)
```

- **Views**: Views are Python functions or classes that receive web requests and return web responses. They fetch data from models and pass it to HTML templates for rendering.
</details>

<details>
<summary>Urls</summary>

### Step 8: Configure URLs

Define URL patterns in `urls.py` to map views to URLs within your Django project:

```python
# myproject/urls.py

from django.contrib import admin
from django.urls import path
from myApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('index/', index, name='index'),
    path('studentpage/', studentpage, name='studentpage'),
    path('teacherpage/', teacherpage, name='teacherpage'),
]
```

- **URLs**: URLs in Django map web requests to specific views. Each path in `urlpatterns` defines a URL pattern, associating a URL with a corresponding view function.
</details>

<details>
<summary>Templates</summary>

### Step 9: Create HTML Templates

Develop HTML templates to display content rendered by views. Use Django's template language for dynamic content:

- **index.html**

```html
<!DOCTYPE html>
<html>
<head>
<style>
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}

li {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

li a:hover:not(.active) {
  background-color: #111;
}

.active {
  background-color: #04AA6D;
}
</style>
</head>
<body>

{% include 'navbar.html' %}

{% block content %}

{% endblock content %}

</body>
</html>
```

- **index.html**: The `index.html` file in this Django project serves as the main landing page for users accessing the site. Here’s a breakdown of its components and how it fits into the overall project structure:

1. **Purpose**: 
   - The `index.html` acts as the introductory page when users visit the root URL (`index/`). It typically provides an overview or navigational hub for accessing other sections of the site.

2. **Structure**:
   - **Navigation Bar**: 
     - A static navigation bar (`navbar.html`) is included using Django template's `{% include 'navbar.html' %}`. This bar provides links for easy navigation across different sections of the site.

     ```html
     {% include 'navbar.html' %}
     ```

   - **Content Block**:
     - The `{% block content %}` and `{% endblock content %}` tags define where dynamic content specific to the `index.html` page would be inserted. This allows for flexibility in updating and customizing the page content.

     ```html
     {% block content %}
     <!-- Content specific to index.html goes here -->
     {% endblock content %}
     ```


- **home.html**

```html
{% extends 'index.html' %}

{% block content %}
<h1>Homepage</h1>
<!-- Your homepage content here -->
{% endblock content %}
```

- **studentpage.html**

```html
{% extends "index.html" %}
{% block content %}
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
</head>
<body>

<h1>This is Student Page</h1>

<table id="customers">
  <tr>
    <th>Name</th>
    <th>Student Id</th>
    <th>Department</th>
  </tr>
  {% for i in std %}
  <tr>
    <td>{{i.name}}</td>
    <td>{{i.stdid}}</td>
    <td>{{i.dept}}</td>
  </tr>
  {% endfor %}
</table>

</body>
</html>
{% endblock content %}
```

- **teacherpage.html**

```html
{% extends "index.html" %}
{% block content %}
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
</head>
<body>

<h1>This is Teacher Page</h1>

<table id="customers">
  <tr>
    <th>Name</th>
    <th>Teacher Id</th>
    <th>Subject</th>
  </tr>
  {% for i in teach %}
  <tr>
    <td>{{i.tecname}}</td>
    <td>{{i.tecid}}</td>
    <td>{{i.subject}}</td>
  </tr>
  {% endfor %}
</table>

</body>
</html>
{% endblock content %}
```

- **HTML Templates**: Django templates are HTML files with embedded Django template language tags (`{% ... %}` and `{{ ... }}`). They allow dynamic rendering of data passed from views.
</details>

<details>
<summary>Add Data (Admin Panel) and View Data (Frontend)</summary>

### Step 10: Adding Data via the Django Admin Panel

The Django admin panel provides a convenient way to manage the data in your database through a web interface. Here’s a step-by-step guide on how to add data using the admin panel:

#### Step 1: Create a Superuser

Before you can access the admin panel,

 you need to create a superuser. This is an admin account that has full access to the Django admin interface. Run the following command and follow the prompts to set up the superuser:

```bash
python manage.py createsuperuser
```

Provide a username, email address, and password when prompted.

#### Step 2: Start the Development Server

Start the Django development server if it is not already running:

```bash
python manage.py runserver
```

#### Step 3: Access the Admin Panel

Open your web browser and navigate to the Django admin panel by going to `http://127.0.0.1:8000/admin/`. You will be prompted to log in. Use the superuser credentials you created earlier.

#### Step 4: Add Data

Once logged in, you will see the admin dashboard. You will see the `StudentModel` and `TeacherModel` that you registered in the admin interface.

1. **Adding a Student**:
    - Click on `StudentModels` in the admin dashboard.
    - Click the “Add Student Model” button.
    - Fill out the form with the student's `name`, `stdid`, and `dept`.
    - Click the “Save” button.

2. **Adding a Teacher**:
    - Click on `TeacherModels` in the admin dashboard.
    - Click the “Add Teacher Model” button.
    - Fill out the form with the teacher's `tecname`, `tecid`, and `subject`.
    - Click the “Save” button.

The data you enter will be saved to the database and can be viewed on the respective student and teacher pages (`http://127.0.0.1:8000/studentpage/` and `http://127.0.0.1:8000/teacherpage/`).

</details>
<details>
<summary>Class Topic Review</summary>

- [x] Install Django and create a new project (`myproject`)
- [x] Create a new Django app (`myApp`)
- [x] Configure `INSTALLED_APPS` in `settings.py`
- [x] Define models (`StudentModel` and `TeacherModel`) in `models.py`
- [x] Register models in `admin.py`
- [x] Apply migrations (`makemigrations`, `migrate`)
- [x] Define views (`index`, `home`, `studentpage`, `teacherpage`) in `views.py`
- [x] Configure URLs (`urls.py`) for project routing
- [x] Create HTML templates (`index.html`, `home.html`, `studentpage.html`, `teacherpage.html`, `navbar.html`)
- [x] Add data via Django admin panel
- [x] View data rendered on frontend pages

</details>

