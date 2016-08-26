function toggler(id){
    $(id).toggle()
}

function openall() {
    var input = someList
    
    for (each in someList) {
        if (someList[each].substring(0, 8) != "https://" && someList[each].substring(0, 7) != "http://") {
            someList[each] = "http://" + someList[each];
        }  
        console.log(someList[each])
        window.open(someList[each]);
    }
}