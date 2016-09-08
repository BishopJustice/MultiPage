function toggler(id){
    $(id).toggle()
}

$(document).ready(function() {
                $('#dtable').DataTable();
            } );

function check_project_len(){
    item = document.getElementById('addproject').value;
    item_len = item.length;
    if (item_len > 50){
        alert("Project names must be under 50 characters. Please try again.");
    }
}