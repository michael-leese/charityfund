var map;
var basepath = window.location.protocol + "//" + window.location.host;
var thisPosition = {};

function getCurrentLocation() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(showPosition);
    } else { 
      alert("Geolocation is not supported by this browser.");
    }
  }
  function showPosition(position) {
      if (thisPosition === null || thisPosition === undefined){
        thisPosition = {lat: 53.579461, lng: -3.539079};
      } else {
        thisPosition = {lat: position.coords.latitude, lng: position.coords.longitude};
      }
  }

function getAppealsMapData(){

    getCurrentLocation();

    $.ajax({
        type: "get",
        url: basepath + "/appeals/all_appeal_map_data",
        dataType: "json",
        success: function(){
        },
        error: function(){
            alert("ERROR: Cannot retrieve map data at this time.");
        }
    }).done(function(data){
        initMap(data);
    });  
}

function setMarkers(map, allLocations) {

    var markers = allLocations.map(function(appeal, i) {
        var myLatLng = new google.maps.LatLng(appeal.latitude, appeal.longitude);
        var marker = new google.maps.Marker({
            map: map,
            position: myLatLng,
            title: appeal.title,
            url: basepath + "/appeals/single_appeal/?id=" +  appeal.id
        });
        google.maps.event.addListener(marker, 'click', function() {
            window.location.href = this.url;
        });
        return marker;
    });

    return markers;
}

function initMap(data) {
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 6,
        center: thisPosition
    });
    
    var markers = setMarkers(map, data);

    var markerCluster = new MarkerClusterer(map, markers, { imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m' });

}

