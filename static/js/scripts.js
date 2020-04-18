$(document).ready(function(){
    //ensure the bottom nav div for collapsed list is hidden when not showing
    if (!$("#bottomNav > .collapse").not(".show")){
        $("#bottomNav").css("visibility", "hidden");
    }
    
});