import json
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import *
from .models import *
from django.forms.utils import ErrorList
from django.http import JsonResponse, HttpResponse
from django.core.mail import send_mail


# For default page ----> home page
def home(request):
    return render(request, 'index.html')


# For Contact us page
def contact(request):
    if request.method == "POST":
        # Gathers the information from the form, saves it to the DB, and sends an email to one of the admins

        name = request.POST["name"]
        email = request.POST["email"]
        mobile = request.POST["num"]
        message = request.POST["msg"]

        msg = 'New Message From ' + name + '\n' + 'Email: ' + email + '\n' + 'Phone: ' + mobile + '\n' + 'Message: ' + message

        send_mail("Student Affairs", msg, email, ['yaramuhammad762@gmail.com'])

        data = ContactUs(FullName=name, Email=email, Mobile=mobile, Message=message)
        data.save()
    return render(request, 'html/contact-us.html')


# For Department Assignment page
def dept(request):
    # When Opened before assignment
    if request.method == 'GET':
        # gets the id
        my_id = request.GET['id']

        # checks if the id exists and the student is eligible
        existing = AddStudent.objects.filter(pk=my_id, StudentLevel=3).exists()

        # if not, redirects to the search page and displays an error
        if not existing:
            return render(request, 'html/search.html', {'error': 'Invalid Student'})

        # if eligible, opens the page normally and display the student's info
        obj = AddStudent.objects.filter(pk=my_id, StudentLevel=3)
        context = {
            'student': obj[0],
        }
        return render(request, 'html/dept.html', context)
    # When the submit button is clicked
    elif request.method == 'POST':
        # gets the dept and id, finds the student and updates their dept, and redirects to the search page
        new_dept = request.POST['department']
        stu_id = request.POST['student_id']
        AddStudent.objects.filter(pk=stu_id).update(Department=new_dept)
        return render(request, 'html/search.html')


# For Edit & delete page
def table_view(request):
    # If the page is opened normally, displays all students
    result = get_update('All', 'All')

    # When the search button is clicked
    if request.method == 'POST':
        # gets the query and filter
        query = request.POST.get('search', 'All')
        filter_val = request.POST.get('filterVal', 'All')
        # returns the appropriate results from the DB
        result = get_update(query, filter_val)

    # passes the result to the edit delete page in both cases
    return render(request, 'html/edit-delete.html', {'result': result})


# For Registration page (adding a new student)
def regist(request):
    # when the add button is clicked
    if request.method == "POST":
        # get the student info
        name = request.POST["username"]
        st_id = request.POST["ID"]
        gpa = request.POST["gpa"]
        gender = request.POST["gender"]
        birth = request.POST["Date"]
        level = request.POST["Level"]
        active = request.POST["os"]
        system = request.POST["system"]
        prog = request.POST["prog"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]

        # creates an object for it in the db
        data = AddStudent(FullName=name, StudentID=st_id, Gpa=gpa
                          , Gender=gender, Birth=birth, StudentLevel=level,
                          Status=active, System=system, Department=prog,
                          Email=email, Mobile=mobile
                          )
        data.save()

    # in both cases, renders the page
    return render(request, 'html/Registration.html')


# For Search page
def search(request):
    return render(request, 'html/search.html')

# class used for errors during sign up
class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<div class="error-field">%s</div>' % e for e in self])


# For Sing-up page
def sign_up(request):
    # when the signup button is pressed
    if request.method == "POST":
        # fills a user form
        form = NewUserForm(data=request.POST, error_class=DivErrorList)
        # if the data is valid, creates a new user and logs them in, and returns to the home page
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'html/student-affairs-home.html')
        # if not valid, re-renders the same page and displays errors
        else:
            return render(request, 'html/sign-up.html', {"form": form})

    # in case of GET (page opened normally), displays and empty form
    form = NewUserForm(data=None, error_class=DivErrorList)
    return render(request, 'html/sign-up.html', {"form": form})


# For Student Affair Home page
def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('affairs-home')
        else:
            messages.error(request, "Invalid Username or Password", extra_tags='inv-user-pass')
    return render(request, 'html/student-affairs-home.html')


# Log out view, logs the user out and redirects to the homepage
def log_out(request):
    logout(request)
    return redirect('affairs-home')


# A view called in the search page using an ajax request, to get data from the DB for the table of students
def get_search(request):
    # gets the search query
    query = request.GET['query']

    # if empty, displays all ACTIVE students
    if query == 'All':
        result = AddStudent.objects.filter(Status='Active')
    # in case a query exists:
    else:
        # first searches by name
        result = AddStudent.objects.filter(FullName__icontains=query, Status='Active')

        # if no results are found, searches by id
        if not result.exists():
            result = AddStudent.objects.filter(StudentID__icontains=query, Status='Active')

            # if no results are found, displays all
            if not result.exists():
                result = AddStudent.objects.filter(Status='Active')

    # returns the result as a json to the ajax request
    # NOTE: ID and Name are of different domains, (numerical vs alphabetical), so a query will never yield
    # results for both
    data = {'result': list(result.values())}
    return JsonResponse(data)


# A view used to search and filter in the edit-delete page
def get_update(query='All', filterVal='All'):
    # by default, displays all students
    result = AddStudent.objects.all()
    filterAttr = 'All'

    # determining the attribute to filter by based on the value of the filter
    # Student Level if filter is in [1, 2, 3, 4]
    # Status if filter is in ['Active', 'InActive']
    # System if filter is in ['MainStream', 'Credit']
    # Department if the filter is two space seperated words (departments are passed with their system)
    # for example: "CS MainStream"
    if '1' <= filterVal <= '4':
        filterAttr = 'StudentLevel'
    elif filterVal == 'Active' or filterVal == 'InActive':
        filterAttr = 'Status'
    elif filterVal == 'MainStream' or filterVal == 'Credit':
        filterAttr = 'System'
    elif len(str(filterVal).split(' ')) == 2:
        filterAttr = 'Department'

    # applying search
    if query != 'All':
        result = AddStudent.objects.filter(FullName__icontains=query)
        if not result.exists():
            result = AddStudent.objects.filter(StudentID__icontains=query)

    # applying filter
    if filterAttr != 'All':
        if filterAttr == 'StudentLevel':
            result = result.filter(StudentLevel=filterVal)
        elif filterAttr == 'System':
            result = result.filter(System=filterVal)
        elif filterAttr == 'Status':
            result = result.filter(Status=filterVal)
        elif filterAttr == 'Department':
            departm = str(filterVal).split(' ')[0]
            print(departm)
            systm = str(filterVal).split(' ')[1]
            print(systm)
            result = result.filter(Department=departm, System=systm)
    return result

# A view that takes the id of a student and deletes them
def del_student(request):
    id_to_delete = request.GET['id_to_del']
    obj = AddStudent.objects.get(pk=id_to_delete)
    obj.delete()
    return HttpResponse(f"Student with ID: {id_to_delete} deleted successfully.")

# A view that takes student info and updates it
def edit_student(request):
    student = json.loads(request.GET['student'])

    AddStudent.objects.filter(pk=student['StudentID']).update(
        FullName=student['FullName'], Status=student['Status'],
        StudentLevel=student['StudentLevel'], Gpa=student['Gpa'], System=student['System'])
    return HttpResponse('Successfully Edited')
