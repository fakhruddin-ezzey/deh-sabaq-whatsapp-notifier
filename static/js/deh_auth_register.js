document.getElementById('alertbox').style.display = 'none'

const validateEmail = (email) => {
    return String(email)
      .toLowerCase()
      .match(
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    );
};


const alertIssue = (message) => {
    alertbox.style.display = 'block';
        alertbox.innerHTML = '';
        alertbox.innerHTML = '<button class="delete"></button>\n'+message;
        return -1;
};


function auth_validate_register(){
    
    var alertbox = document.getElementById('alertbox');

    const auth_register_vals = document.getElementsByTagName('input');

    var process_request_flag = true;

    if(!validateEmail(auth_register_vals[0].value)){
        alertIssue("Email syntax is not correct. Please enter proper email. Eg: dehadmin@gmail.com, dehsabaq@hotmail.com, etc");
        process_request_flag = false;
    }

    if(['',' ',null].includes(auth_register_vals[1].value) || ['',' ',null].includes(auth_register_vals[2].value) || auth_register_vals[2].value != auth_register_vals[1].value){
        alertIssue("Either password is empty or doesn\'t match. Please check and try again");
        process_request_flag = false;
    }

    if(process_request_flag){
        $.ajax({
            type: "POST",
            url: "/register_deh_admin",
            data:{
                csrfmiddlewaretoken:"{{ csrf_token }}",
                "username":"",
                "email":auth_register_vals[0].value,
                "password":auth_register_vals[1].value,
                "is_active":null
            },
            success: function(data){
                if(data.is_created){
                    window.location.href = "/verify_authtoken"
                }else{
                    alertIssue("Some server error occured. Please try again some time.")
                }
                
            },
            error: function(xhr){
                document.getElementById('alertbox').innerHTML = 'Some server error occured. Try again';
            }
        });
    }

}

