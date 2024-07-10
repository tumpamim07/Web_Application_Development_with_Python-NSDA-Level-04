# Fourth Class
<details>
<summary><b>Template Mastering, Include, Extend, Block Content</b></summary>
</details>

#### 1. Creating HTML Templates

- **Create HTML Pages**: Start by creating HTML pages (`Base.html` and `Home.html` etc) within the `template` directory of my Django project.

#### 2. Define Views

- **Define View Functions**: In my project's `views.py`, define view functions to render these HTML templates.

   ```python
   # views.py
   
   from django.shortcuts import render,redirect,HttpResponse

    def Base(request):
        return render(request,'Base.html')

    def Home(request):
        return render(request,'Home.html')

    def News(request):
        return render(request,'News.html')

    def Contact(request):
        return render(request,'Contact.html')

    def About(request):
        return render(request,'About.html')

    def Location(request):
        return render(request,'Location.html')
   ```

#### 3. URL Mapping

- **URL Configuration**: Map these view functions to URLs in `urls.py` of my project.

   ```python
   # urls.py
   
   from django.urls import path
   from myproject.views import *
   
   urlpatterns = [
        path('admin/', admin.site.urls),
        path('Base',Base,name="Base"),
        path('Home',Home,name="Home"),
        path('News',News,name="News"),
        path('Contact',Contact,name="Contact"),
        path('About',About,name="About"),
        path('Location',Location,name="Location"),
   ]
   ```

#### 4. Creating a Navbar

- **HTML Navbar**: Implement a navbar in a separate HTML file (`navigator.html`). This file will be included in other templates.

   ```html
   <!-- navigator.html -->
   <ul>
    <li><a href="{% url 'Home' %}">Home</a></li>
    <li><a href="{% url 'News' %}">News</a></li>
    <li><a href="{% url 'Contact' %}">Contact</a></li>
    <li><a href="{% url 'Location' %}">Location</a></li>
    <li style="float:right"><a class="active" href="{% url 'About' %}">About</a></li>
  </ul>
  
   ```

   - Use `{% url 'name' %}` to dynamically generate URLs.
  

#### 5. Including Navbar in Templates

- **Include Navbar**: Include the navbar in `Base.html` using Django's `{% include %}` tag.

   ```html
   <!-- Base.html -->
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Home</title>
   </head>
   <body>
       {% include 'navigator.html' %}
   </body>
   </html>
   ```

#### 6. Extending Templates

- **Template Inheritance**: Extend `Base.html` in `Home.html` to maintain consistent structure and styles.

   ```html
   <!-- Home.html -->
   {% extends "Base.html" %} 
    {% block content %}

    <h1>This is Home Page</h1>

    {% endblock content %}
   ```

   - `{% block content %}` allows you to override content specific to each page while keeping the overall structure from `Base.html`.

### Note

This step-by-step guide helps you implement navigation using a navbar and master template structure using include and extend techniques in Django. Ensure consistency in naming conventions, HTML structure, and Django template tags for smooth navigation and efficient template management.