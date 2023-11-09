function conformPassword()
        {
            let password = document.getElementById("password").value;
            let cpassword = document.getElementById("cpassword").value;
            console.log(password,cpassword);

            let message = document.getElementById("message");

            if(password.length != 0)
            {
                if(password == cpassword)
                {
                    alert("Password match");
                    message.textContent = "Password Match";
                    message.style.backgroundColor = "#3ae374";
                              
                }
                else
                {
                    alert("Password does not match");
                    message.textContent = "Password does not match";
                    message.style.backgroundColor = "red";
                    tab.document.close();                 
                }
            }
            else
            {
                alert("Password can't be empty!");
                message.textContent = "cannot be empty";
                message.style.backgroundColor = "yellow";
                tab.document.close();
            }

        }
        