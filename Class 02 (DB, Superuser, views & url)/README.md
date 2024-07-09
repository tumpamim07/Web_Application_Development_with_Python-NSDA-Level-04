# Second Class

---

### Default database:
- `db.sqlite3`

### Database migrations

**Migrations in Django**

Migrations help you manage changes to your models and update your database structure accordingly.

- **Generate migrations:**
  ```bash
  python manage.py makemigrations
  ```

- **Apply migrations:**
  ```bash
  python manage.py migrate
  ```

**Using SQLiteBrowser**

Django uses db.sqlite3 as its default database. You can view its contents using tools like [DB Browser for SQLite].

### Super user:

**Creating a Super User**

To manage your Django application:

1. Open the command prompt in your project's root folder.
2. Activate your virtual environment:
   ```bash
   .\environmentname\Scripts\activate
   ```
3. Navigate to your Django project directory:
   ```bash
   cd path/to/your/project
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set a username, email (optional), and password.
   
6. Start the Django server:
   ```bash
   python manage.py runserver
   ```
   Access the admin panel at:
   ```bash
   http://127.0.0.1:8000/admin/
   ```


### Creating views.py:
1. Create `views.py` in your project folder:
   ```python
   from django.shortcuts import HttpResponse
   
   def Homepage(request):
       return HttpResponse("Hello")
   ```

2. Link the view function to `urls.py`:
   ```python
   from myProject.views import Homepage
   
   urlpatterns = [
       path('Homepage/', Homepage, name='Homepage'),
   ]
   ```

3. Run the Django server:
   ```bash
   python manage.py runserver
   ```

4. Access the URL in your browser:
   ```bash
   http://127.0.0.1:8000/home/
   ```
  
## Topics:
- db.sqlite3 ( Default database )
- make migrations
- migrate
- Create superuser
- views.py
- urls.py

## Note: 
- Use import * to import everything from a module.
- Use from module_name import function_name to import a specific function from a module.
- Importing all (import *) brings in all functions and variables from a module, while importing specific functions (from module_name import function_name) brings in only the function you specify.
