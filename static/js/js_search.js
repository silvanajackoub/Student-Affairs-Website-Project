// Function that converts a string to Title Case
function toTitleCase(str)
{
    let names = str.toLowerCase().split(' ')
    let res = "";
    for(let i=0;i<names.length;i++)
    {
        let name = names[i];
        name = name.charAt(0).toUpperCase()+name.substring(1, name.length);
        if(i!==0) res+=" ";
        res+=name;
    }
    return res;
}

// Checks the level of a particular student to determine if they are eligible for dept assignment
function checkLvl(e)
{
    let level = e.parentElement.previousElementSibling.innerHTML;
    if(level!=3)
    {
        alert("Not Eligible");
    }
    else
    {
        //if the student is eligible, gets its id and passes it via GET to the dept assignment page
        let idToAssign = e.parentElement.parentElement.children[1].innerHTML;
        window.location.href = document.querySelector('input[name="dept-url"]').value+`?id=${idToAssign}`;
    }
}

function fill_table(query="All")
{
    // Calls the get_search view that takes a query string (name or id) and returns the results from the DB
    let my_url = document.querySelector('input[name="res-url"]').value;

    // Sends an AJAX GET request to that view with the query
        $.ajax({
            type: 'GET',
            url: my_url,
            data: {
                'query': query,
            },
            dataType: 'json',
            success: function(response)
            {
                // In case the data is fetched successfully, the table is emptied then filled with it
                let tbdy = document.querySelector('tbody');
                tbdy.innerHTML = '';
                for(let student of response['result'])
                {
                    student['FullName'] = toTitleCase(student['FullName']);
                    let tr = document.createElement('tr');
                    for(let key of ['FullName', 'StudentID', 'StudentLevel'])
                    {
                        let td = document.createElement('td');
                        td.innerHTML = student[key];
                        tr.append(td);
                    }
                    let td = document.createElement('td');
                    td.innerHTML = `<a onclick="checkLvl(this)">ASSIGN DEPARTMENT</a>`
                    tr.append(td);
                    tbdy.append(tr);
                }

            },
            error: function()
            {
                alert("Error While Fetching Data");
            }
        });
}

document.addEventListener('DOMContentLoaded', function()
{
    // When the page is loaded, the table is filled with all active students
    fill_table();

    // When the Search button is clicked, the query is passed to fill_table()
    document.querySelector('#search-button').onclick = function()
    {
        let query = document.querySelector('#search-bar').value;
        fill_table(query);
    };

    // If the user enters an Invalid ID in the url of the assign dept page,
    // they are redirected to the search page and an error is shown to them
    let err = document.querySelector('input[name="dept-fail"]');
    if(err)
        alert(err.value)
});