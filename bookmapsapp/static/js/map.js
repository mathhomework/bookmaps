var map;


$(document).ready(function(){


var myLon;
var myLat;
var infowindow;
var myCenter;
var currentBounds;
var bounds;


function initialize() {
//    console.log("sdfjksldfksdjfkldsfdsfjkdsfjksdlfj");
//    console.log(myLon);
//    console.log(myLat);
    var mapOptions = {
        center: new google.maps.LatLng(myLat, myLon),
        // -34.397, 150.644
        zoom: 6
    };
    map = new google.maps.Map(document.getElementById("map-canvas"),
        mapOptions);
    myCenter = map.getCenter();
    console.log(myCenter);
    //returns latLng object

    google.maps.event.addListenerOnce(map, 'tilesloaded', function(){
        console.log("Hay");
        currentBounds = map.getBounds();
        console.log(currentBounds);
        //returns LatLngBounds object

        var query_lat = myCenter.lat();
            var query_lng = myCenter.lng();
            $.ajax({
                url: "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + query_lat + "," + query_lng + "&location_type=ROOFTOP&result_type=street_address&key=AIzaSyDTM4fGWQ4C83C3WtC6ml7kZgmRhI0wgVk",
                type: "GET",
                success: function(data){
                    console.log(data);
                    console.log(data["results"][0]["address_components"][3]["long_name"]);
                    console.log(data["results"][0]["address_components"][5]["long_name"]);
                },
                error: function(data){
                    console.log(data);
                }
            });


        google.maps.event.addListener(map, 'bounds_changed', function(){
            console.log(currentBounds.getNorthEast());
            console.log(currentBounds.getSouthWest());
            console.log(myCenter);
            myCenter = map.getCenter();


            if(currentBounds.contains(myCenter)){
                console.log("inside");



            }
            else{
                console.log("out of the box!");
//                currentBounds = new google.maps.LatLngBounds(myCenter);
                console.log(currentBounds);
            }

        });
    });









//    console.log(currentBounds);


    getData();
    addMarker(map);
    addMarker(map, -34.2, 150.3, "ICE CREAM");
    addMarker(map, -34.3, 150, "SETMAP");
}

var geoerror = function(err){
//
//	$('#refresh').on("click", function(){
//		location.reload();
//	});

};



var yo = function(){
    console.log("js map works");
};
window.yo = yo;
var addMarker = function(map, lat, lng, place){
    //test case
    var myLatLng = new google.maps.LatLng(-34.2, 150.69);

    var marker = new google.maps.Marker({
        position:myLatLng,
        map:map,
        title: "map marka!"
    });

    var bookLatLng = new google.maps.LatLng(lat, lng);

    var bookmarker = new google.maps.Marker({
        position: bookLatLng,
        draggable:true,
        title: place
    });
    bookmarker.setMap(map);
    return bookmarker;
//    addInfoWindow(map, bookmarker);
};
window.addMarker = addMarker;

var getData = function() {
    $.ajax({
        url: '/get_data/',
        type: "GET",
        success: function(data){
            console.log(data);
            var marker_title_list = data[0]["fields"]["title"];
            for(var x = 0; x<data.length; x++){
                var title = data[x]["fields"]["title"];
                var lat = data[x]["fields"]["place"]["lat"];
                var lng = data[x]["fields"]["place"]["lng"];
                var place = data[x]["fields"]["place"]["name"];
                var info = data[x]["fields"]["info"];
                var image = data[x]["fields"]["image"];
                var author = data[x]["fields"]["author"]["name"];
                var bookmarker = addMarker(map, lat, lng, place);
                addInfoWindow(map, bookmarker, title,author, info, image);
            }
        },
        error: function(data){
            console.log("error");
        }
    }).complete(function(){

    });
};


function addInfoWindow(map, marker, title, author, info, image){
    var contentString = "<h1>"+title+"</h1><h2>"+author+"</h2><div class = 'cover'><p><img src ='"+ image+"'>"+info+"</p></div>";

    google.maps.event.addListener(marker, 'click', function(){
        if (infowindow){
            infowindow.close();
        }

        infowindow = new google.maps.InfoWindow({
            maxWidth:400,
            content: contentString
        });
        infowindow.open(map,marker);

    })

}
window.addInfoWindow = addInfoWindow;

    function geosuccess(position) {
        var crd = position.coords;
//        console.log(crd);
        myLon = position.coords.longitude;
        myLat = position.coords.latitude;
//        console.log("LAT" + myLat);
//        console.log("LONG" + myLon);
        initialize();


    }


//start of the js starts here


    if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(geosuccess, geoerror,{
	enableHighAccuracy: true,maximumAge:0});

	}
	else {
		geoerror();
        console.log("ERROR");
	}




//    google.maps.event.addDomListener(window, 'load', initialize);

});

