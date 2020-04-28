$(document).ready(function(){
    //ensure the bottom nav div for collapsed list is hidden when not showing
    if (!$("#bottomNav > .collapse").not(".show")){
        $("#bottomNav").css("visibility", "hidden");
    }

    if ($("#messages").show()) {
        setTimeout(function(){
            $("#messages").hide();
        }, 1000);
    }
    
    //get searchParameters functionality from https://stackoverflow.com/questions/5448545/how-to-retrieve-get-parameters-from-javascript
    function getSearchParameters() {
        var prmstr = window.location.search.substr(1);
        return prmstr != null && prmstr != "" ? transformToAssocArray(prmstr) : {};
    }
  
    function transformToAssocArray( prmstr ) {
        var params = {};
        var prmarr = prmstr.split("&");
        for ( var i = 0; i < prmarr.length; i++) {
            var tmparr = prmarr[i].split("=");
            params[tmparr[0]] = tmparr[1];
        }
        return params;
    }
  
    var params = getSearchParameters();
    //if the url on all appeals page contains a filter param, set the dropdown-item to active
    if (params.filter != undefined){
        switch (params.filter) {
            case '-money_target':
                $('a.dropdown-item[name="low-high"]').addClass('active');
                break;
            case 'money_target':
                $('a.dropdown-item[name="high-low"]').addClass('active');
                break;
            case '-created_date':
                $('a.dropdown-item[name="newest"]').addClass('active');
                break;
            case 'created_date':
                $('a.dropdown-item[name="oldest"]').addClass('active');
                break;
        }
    }

});