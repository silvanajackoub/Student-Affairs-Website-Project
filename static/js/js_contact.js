function ValidateName(nameP)
{
    const letters = /^[A-Za-z]+(\s[A-Za-z]+)+$/;

    if(letters.test(nameP))
        return true;
    else
    {
    alert('Please input alphabet characters only in the Name');
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

document.addEventListener("DOMContentLoaded" , function()
{
    document.querySelector("form").onsubmit = function ()
    {
        const name = document.querySelector("#name").value;
        const num = document.querySelector("#num").value;

        if(ValidatePhoneNumber(num) && ValidateName(name))
        {
            alert("Thanks for your Feedback");
            return true;
        }
        return false;
        
    }
});