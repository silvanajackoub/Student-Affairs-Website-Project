// The function that opens the edit student popup and fills it with the current student's data
function openForm(elem)
{
    document.getElementById("myForm").style.display = "block";
    let stud_info = elem.parentElement.parentElement.children;

    document.querySelector('input[name="Name"]').value = stud_info[1].innerHTML;
    //The ID is saved to find the student in the DB, but can't be changed since it is the primary key
    document.querySelector('input[name="ID"]').value = stud_info[2].innerHTML;
    document.querySelector('#status-slider').checked = stud_info[4].innerHTML === "Active";
    document.querySelector('#level-select').value = stud_info[6].innerHTML;
    document.querySelector('input[name="GPA"]').value = stud_info[5].innerHTML;
    document.querySelector('#system-select').value = stud_info[7].innerHTML;
}

// The function called when the delete button is clicked
function del_func(elem)
{
    if (window.confirm('Are You Sure You Want To Delete This Student?'))
    {
        //The id is passed to an AJAX GET request that calls the del_student view
        let id_to_del = elem.parentElement.parentElement.children[2].innerHTML;
        let del_url = document.querySelector('input[name="del-url"]').value;

        $.ajax({
            type: 'GET',
            url: del_url,
            data: {
                'id_to_del': id_to_del,
            },
            success: function(response)
            {
                // If the student is successfully deleted, a success message is shown
                alert(response);
                window.location.reload();
            },
            error: function()
            {
                alert("Error During Deletion.");
            }
        });
    }
}

// Function that closes the edit form
function closeForm()
{
    document.getElementById("myForm").style.display = "none";
}

document.addEventListener('DOMContentLoaded', function()
{
    document.querySelector('#edit-form').onsubmit = function(e)
    {
        e.preventDefault();
        //When the update button in the form is clicked, the input data is gathered
        let newName = document.querySelector('input[name="Name"]').value;
        let stu_ID = document.querySelector('input[name="ID"]').value;
        let newStatus = document.querySelector('#status-slider').checked;
        let newLevel = document.querySelector('#level-select').value;
        let newGPA = document.querySelector('#gpa').value;
        let newSys = document.querySelector('#system-select').value;

        // The status is taken from the slider as a boolean value and adjusted
        if(newStatus) newStatus = 'Active';
        else newStatus = 'InActive';

        // Creating a JSON object with student data
        let new_stud = {
                    'FullName': newName,
                    'StudentID': stu_ID,
                    'Status': newStatus,
                    'StudentLevel': newLevel,
                    'Gpa': newGPA,
                    'System': newSys,
                }

        let edit_url = document.querySelector('input[name="edit-url"]').value;

        // Sending an AJAX GET request to the edit_Student view, with the updated student info
        $.ajax({
            type: 'GET',
            url: edit_url,
            data:{
                'student': JSON.stringify(new_stud),
            },
            success: function()
            {
                // If the student is edited successfully
                alert('Edited Successfully.');
            },
            error: function()
            {
                alert('Editing Error.');
            }
        });
        window.location.reload();
    }

    window.onclick = function(event)
    {
    let form = document.getElementById("myForm");
    if (event.target == form)
        form.style.display = "none";
    }
});
