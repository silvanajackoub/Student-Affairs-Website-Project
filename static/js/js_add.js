// Some Validation functions for input
function ValidateName(nameP)
{
    const letters = /^[A-Za-z]+(\s[A-Za-z]+)+$/;

    if(letters.test(nameP))
        return true;
    else
    {
        alert('The Name must be two or more space-seperated words.');
        return false;
    }
}

function ValidateID(ID)
{
    const ident = /^[0-9]{8}$/;
    if(ident.test(ID))
        return true;
    else
    {
        alert("The ID must consists of exactly 8 numbers.");
        return false;
    }
}

function ValidatePhoneNumber(nom)
{
    if(nom.length>=10 && nom.length<=13)
    {
        return true;
    }
    else{
        alert('Mobile Number Should be Between 10 and 13 Number long');
        return false;
    }
}

function ValidateGPA(gpa)
{
    if (gpa > 4 && gpa < 0)
    {
        alert('The GPA should be Between "0" and "4" ');
        return false;
    }
    return true
}

function ValidateYear(year)
{
    const d = new Date (year);
    const y = d.getFullYear();
    if (y > 1970 && y < 9999)
    {
        return true;
    }
    else
    {
        alert('Not A valid Year');
        return false;
    }
}


document.addEventListener("DOMContentLoaded" , function()
{
    document.querySelector("form").onsubmit = function ()
    {
        const name = document.querySelector("#username").value;
        const ID = document.querySelector("#ID").value;
        const gpa = document.querySelector("#gpa").value;
        const mobile = document.querySelector("#mobile").value;
        const dateVal = document.querySelector("#Date").value;

        // If all validations go through, the form is executed
        if (ValidateName(name) && ValidateID(ID) && ValidatePhoneNumber(mobile) && ValidateGPA(gpa) &&
             ValidateYear(dateVal))
         {
             alert("Student Added Successfully.\n");
             return true;
         }
        // else it returns false
        return false;
    }
});