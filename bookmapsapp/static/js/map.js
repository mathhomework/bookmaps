function initialize() {
    var mapOptions = {
        center: new google.maps.LatLng(-34.397, 150.644),
        zoom: 10
    };
    var map = new google.maps.Map(document.getElementById("map-canvas"),
        mapOptions);

    addMarker(map);


}

function addMarker(map){
    var myLatLng = new google.maps.LatLng(-34.2, 150.69);

    var marker = new google.maps.Marker({
        position:myLatLng,
        map:map,
        title: "map marka!"
    });

    var bookLatLng = new google.maps.LatLng(-34.2, 150.39);

    var bookmarker = new google.maps.Marker({
        position: bookLatLng,
        draggable:true,
        title: "Book Title"
    });
    bookmarker.setMap(map);
    addInfoWindow(map, bookmarker);
}

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

google.maps.event.addDomListener(window, 'load', initialize);