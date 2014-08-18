var map;

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
    console.log(place);
    console.log(lat);
    console.log(lng);
    bookmarker.setMap(map);
//    addInfoWindow(map, bookmarker);
};

var getData = function() {
    $.ajax({
        url: '/get_data/',
        type: "GET",
        success: function(data){
            console.log(data);
            for(var x = 0; x<data.length; x++){

                    var lat = data[x]["fields"]["place"]["lat"];
                    var lng = data[x]["fields"]["place"]["lng"];
                    var place = data[x]["fields"]["place"]["name"];
                    addMarker(map, lat, lng, place);
            }
        },
        error: function(data){
            console.log("error");
        }
    }).complete(function(){

    });
};


function addInfoWindow(map, marker){
    var contentString = "<p>Howdy jack, how are you doing today?</p>" +
        "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque sed nunc leo. Nulla lacus purus, varius non ullamcorper et, hendrerit et est. Donec non dolor sed dolor pharetra condimentum vel sed turpis. Phasellus dignissim lorem tortor, ut tempor quam venenatis vitae. Interdum et malesuada fames ac ante ipsum primis in faucibus. Etiam lobortis, libero ac imperdiet tristique, tellus orci tempus mi, id fermentum neque est id lectus. Vestibulum euismod felis ac nunc mattis, non lobortis massa placerat. Praesent pharetra dui vel magna tincidunt, eget eleifend ante blandit. Nunc a sapien elit. Ut laoreet volutpat fringilla. Pellentesque mi nulla, placerat eget pellentesque ac, ultricies sed ante. Curabitur interdum neque id diam sagittis, accumsan tincidunt neque aliquet.</p>";

    var infowindow = new google.maps.InfoWindow({
        content: contentString,
        maxWidth:400
    });

    google.maps.event.addListener(marker, 'click', function(){
        infowindow.open(map,marker);
    })
}


function initialize() {

    var mapOptions = {
        center: new google.maps.LatLng(-34.397, 150.644),
        zoom: 10
    };
    var map = new google.maps.Map(document.getElementById("map-canvas"),
        mapOptions);


    addMarker(map);
    addMarker(map, -34.2, 150.3, "ICE CREAM");

    console.log("addeddedde");
}


$(document).ready(function(){

    google.maps.event.addDomListener(window, 'load', initialize);
    getData();
    console.log("hay");
    addMarker(map, -34.3, 150, "SETMAP");


});
