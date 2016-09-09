$(document).ready(function() {
                $('#dtable').DataTable();
            } );


function toggler(id){
    $(id).toggle()
}

function check_project_len(){
    item = document.getElementById('addproject').value;
    item_len = item.length;
    if (item_len > 50){
        alert("Project names must be under 50 characters. Please try again.");
    }
}

function open_links(){
    it = document.getElementsByClassName("url")
    console.log(it.href)
    var urls = []
    for (each in it){
        item = it[each].href;
        if (item){
        urls.push(item);
        }
    }
    for (url in urls){
        console.log(urls[url]);
        window.open(urls[url]);
    }
}
