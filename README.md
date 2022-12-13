# Student-Affairs-Website-Project
This is our Project for the Web technology course taken during fall 2022 semester.

<h2> Website Description</h2>
<h3>This website is for the stuff of the student affairs, each user can :</h3>
1. Add a new student to the system. Student information includes id, name,
date of birth, GPA, gender, level, status=”active”, “inactive”, department, email,
mobile number.</br>
2. Update an existing student information ( except department field should be
shown disabled for editing ).</br>
3. Can delete an existing student data through a delete button in edit student
data page with a confirmation dialogue for the action before deletion occurs.</br>
4. Search for “active” students by name in search for students screen and
students with similar names having active status should be rendered as a table.</br>
5. Select a specific student after searching to assign a department through
the student’s department assignment page.(applicable for students if level >= 3)</br>
6. View all active/inactive students in a separate page</br>


Setting up the environment 🛠
--------------------------

#### 1. Make sure python v3.7 or higher is installed:

console
* To get the version Excute:

```
$ python --version
Python 3.9.6
```

#### 2. Make Sure Git is installed:
* To get the version Excute:
```
$ git --version
git version 2.28.0.windows.1
```

#### 3. Execute the following commands in your terminal after changing your directory to the desired path

```
$ mkdir project && cd project
$ python -m venv venv
```

For Windows Users:
```
$ venv\Scripts\activate
```
For Linux Users:
```
$ source venv/bin/activate
```
Then
```
$ git clone https://github.com/silvanajackoub/Student-Affairs-Website-Project.git && cd Student-Affairs-Website-Project
$ pip install -r requirements.txt
```
<b>To test our web site here is a user name and password:</b></br>
username: Silvana_Yacoub</br>
password: 12345



