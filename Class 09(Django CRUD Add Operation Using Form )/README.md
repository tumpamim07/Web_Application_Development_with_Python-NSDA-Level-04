# Ninth Class

<details>
<summary><b>Working Procedure of CRUD Add Operation</b></summary>

Here, we are focusing on the "Add" operation of CRUD (Create, Read, Update, Delete) using Django. Here, we demonstrate how to create a student record and display it on the webpage.

#### Models (`models.py`)

The `models.py` file defines the structure of the `studentModel` model, which represents the student entity in our database.

```python
from django.db import models

class studentModel(models.Model):
    FirstName=models.CharField(max_length=50,null=True)
    LastName=models.CharField(max_length=50,null=True)
    Department=models.CharField(max_length=50,null=True)
    City=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.FirstName
```

- **Fields**: Each student has a first name, last name, department, and city.
- **__str__**: The `__str__` method returns the first name of the student when the object is printed.
- **`null=True`**: This option allows the database column to accept NULL values, meaning it is optional to provide a value for these fields when creating a new student record.

#### Views (`views.py`)

The `views.py` file handles the logic for rendering templates and processing user input.

```python
from django.shortcuts import render,redirect,HttpResponse
from myapp.models import *

def studentpage(request):
    student=studentModel.objects.all()

    mydic={
        'std':student
    }
    return render(request,'studentpage.html',mydic)

def addstudentpage(request):

    if request.method=='POST':
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        dep=request.POST.get('department')
        cit=request.POST.get('city')

        student=studentModel(
            FirstName=fname,
            LastName=lname,
            Department=dep,
            City=cit,
        )

        student.save()

        return redirect ("studentpage")
    return render(request,'addstudentpage.html')
```

- **studentpage**: Retrieves all student records from the database and passes them to `studentpage.html` for rendering.
- **addstudentpage**: Handles the GET and POST requests for adding a new student.
  - **GET**: Renders the form for adding a new student.
  - **POST**: Retrieves data from the form, creates a new `studentModel` object, saves it to the database, and redirects to the `studentpage`.

#### Templates

##### `addstudentpage.html`

This template provides a form to add a new student.

```html
{% extends "home.html" %}
{% block content %}
  
<!DOCTYPE html>
<html>
<style>
input[type=text], select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type=submit] {
  width: 100%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}

div {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}
</style>
<body>

<h3>Student Form</h3>

<div>
  <form action="{% url 'addstudentpage' %}" method="POST">
    {% csrf_token %}
    <label for="fname">First Name</label>
    <input type="text" id="fname" name="firstname" placeholder="Your name..">

    <label for="lname">Last Name</label>
    <input type="text" id="lname" name="lastname" placeholder="Your last name..">

    <label for="department">Department</label>
    <input type="text" id="lname" name="department" placeholder="Your department name..">

    <label for="city">Last Name</label>
    <input type="text" id="lname" name="city" placeholder="Your city name..">
  
    <input type="submit" value="Add Student">
  </form>
</div>

</body>
</html>

{% endblock content %}
```

##### `studentpage.html`

This template displays the list of students.

```html
{% extends "home.html" %}
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

<h1>A Fancy Table</h1>

<table id="customers">
  <tr>
    <th>First Name</th>
    <th>Last Name</th>
    <th>Department</th>
    <th>City</th>
  </tr>

  {% for i in std %}
 
  <tr>
    <td>{{i.FirstName}}</td>
    <td>{{i.LastName}}</td>
    <td>{{i.Department}}</td>
    <td>{{i.City}}</td>
  </tr>
  {% endfor %}
</table>

</body>
</html>
{% endblock content %}
```

#### Methods and Their Use in CRUD

- **GET**: Retrieves data from the server. In our example, the `studentpage` view uses the GET method to retrieve and display all student records.
- **POST**: Submits data to be processed to a specified resource. In our example, the `addstudentpage` view uses the POST method to submit new student data to the server.
- **Redirect**: Redirects the user to a different URL. In our example, after saving the student data, the user is redirected to the `studentpage`.
- **Action Attribute**: Specifies where to send the form data when the form is submitted. In our `addstudentpage.html` file, the form's `action` attribute points to the `addstudentpage` URL, which handles the form submission.

</details>
<details>
<summary><b>Class Topic Review</b></summary>

- [x] Models
- [x] Views
- [x] CRUD Add Operation 
- [x] Create HTML templates (`addstudentpage.html`, `studentpage.html`)
- [x] Add data via Django admin panel
- [x] View data rendered on frontend pages

</details>