//Set global variable and objects
var map;
var appealsData;
var basepath = window.location.protocol + "//" + window.location.host;
var mapSetup = {position: {lat: undefined, lng: undefined}, zoom: undefined}
var defaultLat = 54.546580;
var defaultLng = -4.188547;
var defaultZoom = 5;

//checks the geolocation permission status
function geoLocation(){
    waiting = true;
    navigator.permissions.query({name:'geolocation'}).then(function(result) {
    if (result.state === 'granted') {
        //if granted then only need the success callback
        navigator.geolocation.getCurrentPosition(showPosition);
    } else if (result.state === 'prompt') {
        if (navigator.geolocation) {
            //if prompt then we need success and deny callbacks
            navigator.geolocation.getCurrentPosition(showPosition, showDefaultMap);
          } else {
            alert("Geolocation is not supported by this browser.");
          }
    } else  {
        //if denied or undefined then show default map view only
        showDefaultMap();
    }
  });
}
//if permission is granted mapSetup is populated with the users position and zooms in slightly to their area
function showPosition(position){
    //only show zoomed in position if user is logged in
    var authUser = $('#map').attr('name');
    if (authUser == "Auth-User-Map") {
        mapSetup.position.lat = position.coords.latitude; 
        mapSetup.position.lng = position.coords.longitude; 
        mapSetup.zoom = 9;
        //Once mapSetup is populated call the initMap()
        initMap();
    } else {
        showDefaultMap();
    }
}
//if permission is denied mapSetup is populated with the default position(center of UK & Ireland) zoom set out to see all of mainland UK and Ireland
function showDefaultMap(){
    mapSetup.position.lat = defaultLat; 
    mapSetup.position.lng = defaultLng; 
    mapSetup.zoom = defaultZoom;
    //Once mapSetup is populated call the initMap()
    initMap();
}

//Initial function to retrieve appeals data from DB
function getAppealsMapData(){
    
    $.ajax({
        type: "get",
        url: basepath + "/appeals/all_appeal_map_data",
        dataType: "json",
        success: function(data){
            //set global appealsData to returned data object
            appealsData = data;
        },
        error: function(){
            alert("ERROR: Cannot retrieve map data at this time.");
        }
    }).done(function(){
        //when done with Ajax call get geolocation setup data
        geoLocation();
    });  
}

//Sets up the markers for the map using the map object created and the appealsData from DB
function setMarkers(map, allLocations) {
    //map each appeal and create a marker based on data
    var markers = allLocations.map(function(appeal, i) {
        var myLatLng = new google.maps.LatLng(appeal.latitude, appeal.longitude);
        var marker = new google.maps.Marker({
            map: map,
            position: myLatLng,
            title: appeal.title,
            url: basepath + "/appeals/single_appeal/?id=" +  appeal.id
        });
        //add on click event to each marker so takes you to the page for the appeal
        google.maps.event.addListener(marker, 'click', function() {
            window.location.href = this.url;
        });
        return marker;
    });
    return markers;
}
//Initialize the map object and set marker clusters
function initMap() {

    map = new google.maps.Map(document.getElementById("map"), {
        zoom: mapSetup.zoom,
        center: {lat: mapSetup.position.lat, lng: mapSetup.position.lng}
    });

    //create the array of marker objects
    var markers = setMarkers(map, appealsData);

    var markerCluster = new MarkerClusterer(map, markers, { imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m' });

    
}
