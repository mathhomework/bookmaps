$(document).ready(function(){

var map;
var myLon;
var myLat;
var infowindow;



function initialize() {
    console.log("sdfjksldfksdjfkldsfdsfjkdsfjksdlfj");
    console.log(myLon);
    console.log(myLat);
    var mapOptions = {
        center: new google.maps.LatLng(myLat, myLon),
        // -34.397, 150.644
        zoom: 10
    };
    map = new google.maps.Map(document.getElementById("map-canvas"),
        mapOptions);

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

var getData = function() {
    $.ajax({
        url: '/get_data/',
        type: "GET",
        success: function(data){
            console.log(data);
            for(var x = 0; x<data.length; x++){
                var title = data[x]["fields"]["title"];
                var lat = data[x]["fields"]["place"]["lat"];
                var lng = data[x]["fields"]["place"]["lng"];
                var place = data[x]["fields"]["place"]["name"];
                var info = data[x]["fields"]["info"];
                var image = data[x]["fields"]["image"];

                var bookmarker = addMarker(map, lat, lng, place);
                addInfoWindow(map, bookmarker, title, info, image);
            }
        },
        error: function(data){
            console.log("error");
        }
    }).complete(function(){

    });
};


function addInfoWindow(map, marker, title, info, image){
    var contentString = "<h1>"+title+"</h1><p>"+info+"</p><img src ="+ image+">";



        google.maps.event.addListener(marker, 'click', function(){
        if (infowindow){
            console.log("EEHEHES");
            infowindow.close();
        }

        infowindow = new google.maps.InfoWindow({
            maxWidth:400,
            content: contentString
        });
        infowindow.open(map,marker);

    })
}

    function geosuccess(position) {
        var crd = position.coords;
        console.log(crd);
        myLon = position.coords.longitude;
        myLat = position.coords.latitude;
        console.log("LAT" + myLat);
        console.log("LONG" + myLon);
        initialize();
    }



    console.log("hay");


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
