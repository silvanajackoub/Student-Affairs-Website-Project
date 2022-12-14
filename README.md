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


## Screenshots

#### Homepage

![Homepage](https://user-images.githubusercontent.com/78499278/207459589-6af1e5d0-e938-4f13-afbe-78c2dfe3be09.jpg)

<hr>

#### Login Page

![sign in](https://user-images.githubusercontent.com/78499278/207459755-1f037b2e-aeb8-4cf1-872a-d4b2a1c0a49b.jpg)

<hr>

#### Student Registeration Page

![registeration](https://user-images.githubusercontent.com/78499278/207459862-5a2cec5a-0c8d-4609-9661-da0cb4cc5ebd.jpg)

<hr>

#### Student Edit-Delete Page

![edit-delete](https://user-images.githubusercontent.com/78499278/207459873-e07ffe51-3ec8-4a2a-bf34-77337b606d33.jpg)

#### Student Search Page

![search](https://user-images.githubusercontent.com/78499278/207459889-884a5485-2a38-4fbe-addd-7ebac58494c3.jpg)

<hr>

#### Contact Us Page

![contact us](https://user-images.githubusercontent.com/78499278/207459907-e7133e97-8b96-4a92-8096-d55ac98a4b54.jpg)


<hr>

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

