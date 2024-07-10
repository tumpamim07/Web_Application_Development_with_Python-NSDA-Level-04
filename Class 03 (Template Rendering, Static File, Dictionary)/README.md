
# Third Class

<details>
<summary><b>Displaying HTML Templates in Django</b></summary>

To show an HTML page in your browser using Django, follow these steps:

1. **Setup Directories:**
   - Create two folders in your main project directory: `template` and `static`.

2. **Configure Static Files:**
   - Open `settings.py` and find the `STATICFILES_DIRS` section.
   - Remove any paths except `BASE_DIR / "static"` so it looks like this:
     ```python
     STATICFILES_DIRS = [
         BASE_DIR / "static",
     ]
     ```

3. **Configure Templates:**
   - In `settings.py`, find the `TEMPLATES` setting.
   - Update the `DIRS` line to include your `templates` folder:
     ```python
     'DIRS': [BASE_DIR / "template"],
     ```

4. **Create an HTML File:**
   - Inside the `template` folder, create a file called `table.html`.
   - Add some HTML code to this file. For example, a table to display data.

5. **Set Up the View:**
   - Create a `views.py` file 
   - Import the `render` function:
     ```python
     from django.shortcuts import render
     ```
   - Define a function to handle the view:
     ```python
     def table(request):
         return render(request, 'table.html')
     ```

6. **Update URLs:**
   - Open `urls.py`.
   - Import your view function:
     ```python
     from myproject.views import table
     ```
   - Add a URL pattern to link to your view:
     ```python
     urlpatterns = [
         path('table/', table, name="table"),
     ]
     ```

7. **Run Your Server:**
   - Start your Django server with:
     ```bash
     python manage.py runserver
     ```
   - Visit the page in your browser at `http://127.0.0.1:8000/table/`.

In this way, you can create multiple views and corresponding URLs.

</details>

<details>
<summary><b>Passing Data from Views to Templates</b></summary>

To send data from your Django view to an HTML template, follow these steps:

1. **Render the View with Data:**
   - Update your view function in `views.py` to pass data:
     ```python
     def table(request):
         mydict = {
             'Name': 'Tumpa',
             'Department': 'CSE',
             'Semester': '5th',
             'Name1': 'Urmi',
             'Department1': 'CSE',
             'Semester1': '5th',
         }
         return render(request, 'table.html', mydict)
     ```

2. **Update the HTML Template:**
   - In your `table.html` file, use the Django template language to display the data:
     ```html
     <table id="customers">
         <tr>
           <th>Name</th>
           <th>Department</th>
           <th>Semester</th>
         </tr>
         <tr>
           <td>{{ Name }}</td>
           <td>{{ Department }}</td>
           <td>{{ Semester }}</td>
         </tr>
         <tr>
           <td>{{ Name1 }}</td>
           <td>{{ Department1 }}</td>
           <td>{{ Semester1 }}</td>
         </tr>
     </table>
     ```

3. **Make Sure URL is Mapped:**
   - Ensure your `urls.py` file maps the URL to the view:
     ```python
     urlpatterns = [
         path('my-url/', table, name='table'),
     ]
     ```

## Key Concepts:
- Rendering HTML templates.
- Passing data using a dictionary.
- Creating and modifying HTML tables.
- Updating view functions and URL mappings.

</details>