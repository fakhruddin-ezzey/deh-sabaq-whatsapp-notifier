document.getElementById('alertbox').style.display = 'none';


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

const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
document.cookie = "csrftoken="+csrftoken;

function validate_deh_admin(){

    process_flag = true;

    var validating_email = document.getElementById('validating_email').value;
    var validating_password = document.getElementById('validating_password').value;

    if(!validateEmail(validating_email)){
        alertIssue('Email format is invalid. Please check the email inserted and try again')
        process_flag = false;
    }

    if(process_flag){
        $.ajax({
            type: "POST",
            url: "/validate_deh_admin",
            data:{
                "csrfmiddlewaretoken": csrftoken,
                "authenticate_email":validating_email,
                "authenticate_password":validating_password,
            },
            success: function(data){
                if(data.is_validated){
                    window.location.href = "/mumin"
                }else{
                    alertIssue("Email or password seems incorrect. You can recheck and try it again.")
                }
            },
            error: function(xhr){
                console.log(xhr);
                alertIssue("Some server error occured.Please try after sometime or contact developer@ahhaa.com")
            }
        });
    }

}