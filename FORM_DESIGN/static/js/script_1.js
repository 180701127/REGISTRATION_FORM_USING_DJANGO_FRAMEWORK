var is_visible = false;

function see() {
    var input = document.getElementById("password");
    var see = document.getElementById("see");

    if(is_visible)
    {
        input.type = "password";
        is_visible = false;
        see.style.color = 'red';
    }
    else
    {
        input.type = 'text';
        is_visible = 'true';
        see.style.color = '#262626';
    }
}