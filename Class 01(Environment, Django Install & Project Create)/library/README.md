# First Class
---

## Getting Started with Django

### 1. Install Python
   - Django is based on Python, so you need to install Python first.

### 2. Create a Root Folder
   - This will be your main project folder 

### 3. Open Command Prompt
   - Navigate to your project folder using the Command Prompt (CMD).

### 4. Set Up Virtual Environment
   - Create a virtual environment to manage dependencies:
     ```cmd
     python -m venv myenv
     ```
   - Activate the virtual environment:
     ```cmd
     .\myenv\Scripts\activate
     ```

### 5. Install Django
   - Use pip to install Django:
     ```cmd
     pip install django
     ```

### 6. Create a Django Project
   - Initialize a Django project inside your project folder:
     ```cmd
     django-admin startproject myproject
     ```

### 7. Navigate to Your Project
   - Enter your Django project directory:
     ```cmd
     cd myproject
     ```

### 8. Run the Development Server
   - Start the Django server:
     ```cmd
     python manage.py runserver
     ```

   - Your local server will be running at `http://127.0.0.1:8000/`.
    ![runserver](/assets/runserver.png)