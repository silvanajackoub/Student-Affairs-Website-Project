document.addEventListener('DOMContentLoaded', function()
{
    let system = document.querySelector('input[name="stud_system"]')
    if(system)
    {
        system = system.value;
        if(system === 'MainStream')
            document.querySelector('optgroup[label="Credit"]').setAttribute('style', 'display: none');
        else if(system==='Credit')
            document.querySelector('optgroup[label="MainStream"]').setAttribute('style', 'display: none');
    }

    document.querySelector('#dept-form').onsubmit = function()
    {
        alert("Department Assigned Successfully");
    };
});