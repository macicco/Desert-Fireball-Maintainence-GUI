jQuery(document).ready(function(){
    // Function makes an AJAX request to the server, with the clicked button's ID as input.
    jQuery(".commandbutton").click(function(){
        jQuery.get("/runcommand", { buttonID : $(this).attr('id') }, function(result){
            jQuery("#feedbackText").append(result);
          });
        });
    });