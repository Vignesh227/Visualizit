function load(){
    /* Loader */
    $('#loader').addClass('ring');
    $('#innerloader').addClass('innerring');
    $('#loader').fadeIn(1000); 
    $('#innerloader').fadeIn(1000); 
    /* Loader */

    $('#plotlinks').remove();
}
jQuery(document).ready(function() {
    /* Loader */
    $('#loader').addClass('ring');
    $('#innerloader').addClass('innerring');
    $('#loader').fadeOut(200);
    $('#innerloader').fadeOut(200);
    /* Loader */

    $('#plotlinks').fadeIn(4000);
    
});
