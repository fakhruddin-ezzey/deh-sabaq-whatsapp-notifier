document.getElementById('alertbox').style.display = 'none'

const alertIssue = (message) => {
    alertbox.style.display = 'block';
    alertbox.innerHTML = '';
    alertbox.innerHTML = '<button class="delete"></button>\n'+message;
    return -1;
};

function verify_authtoken() {

    proceed_flag = true;

    var tokenval = document.getElementById('token_val').value;

    if(tokenval=="" || tokenval==" " || tokenval==null){
        alertIssue('Token cannot be empty. Please check the value');
        proceed_flag = false;
    }

    if(proceed_flag){
        $.ajax({
            type: "PUT",
            url: "/verify_deh_admin",
            data:{
                csrfmiddlewaretoken:"{{ csrf_token }}",
                "tokenkey":tokenval
            },
            success: function(data){
                if(data.is_verified){
                    window.location.href = "/verify_success"
                }else{
                    alertIssue("Token must be wrong or expired. Please contact developer@ahhaa.com")
                }
                
            },
            error: function(xhr){
                alertIssue("Some server error occured.Please try after sometime or contact developer@ahhaa.com")
            }
        });        
    }


}