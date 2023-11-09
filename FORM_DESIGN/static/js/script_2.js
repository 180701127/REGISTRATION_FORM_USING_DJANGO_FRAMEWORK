var is_visible = false;

function hide() {
    var input = document.getElementById("cpassword");
    var hide = document.getElementById("hide");

    if(is_visible)
    {
        input.type = "password";
        is_visible = false;
        hide.style.color = 'red';
    }
    else
    {
        input.type = 'text';
        is_visible = 'true';
        hide.style.color = '#262626';
    }
}
