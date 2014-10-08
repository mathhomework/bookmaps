//function createBook(){
//    $.ajax({
//        url:/user_create_book/,
//        type:"POST",
//        data: user_data,
//        dataType:"json",
//        success:function(data){
//
//        },
//        error: function(data){
//
//        }
//    })
//}

$(document).ready(function(){

$(function(){
    $('#contact').popover({
        placement:'bottom',
        title:'Contact',
        content: 'Andrew can be reached at andrewshum@alumni.ucsd.edu'
    });
});

function addPlaceTimeAjax(ddata){
    console.log("Now adding place time");
     $.ajax({
        url:"/add_place_time/",
        type:"POST",
        data:ddata,
        dataType:"json"
     });
}

    $("#addBookButton").on("click", function(){
        var book = $("#addBook").val();
        $('#addBook').attr("value", "");

        var new_data = JSON.stringify({'book':book});
        console.log("WHOAAAAAAA");
        console.log(new_data);
        $.ajax({
            url:"/add_book/",
            type:"POST",
            data:new_data,
            dataType:"json",
            timeout: 20000,
            success: function(data){
                $("#bookInfoResult").empty();
                console.log("ADD_BOOK SUCCESS FUNCTION BEGINS");
                //data returned should have an object with everything but image and info populated,
                //everything populated, or nothing populated at all.
                var title = data[0]["fields"]["title"];
                var info = data[0]["fields"]["info"];
                var image = data[0]["fields"]["image"];
                var author = data[0]["fields"]["author"]["name"];



                console.log(data[0]["fields"]["title"]);
                console.log(data[0]["fields"]);
                if(data[0]["fields"]["place"]){
                    //cases that fall into this conditional include new objs or old objs with full data.
                    var lat = data[0]["fields"]["place"]["lat"];
                    var lng = data[0]["fields"]["place"]["lng"];
                    var place = data[0]["fields"]["place"]["name"];
                    var foundMarker = addMarker(map, lat, lng, place);
                    addInfoWindow(map, foundMarker, title, author, info, image, place);
                    map.setCenter(foundMarker.getPosition());
                    map.setZoom(7);
                    console.log("SKSSKSKS");
                    $("#bookInfo").empty();
                    console.log("KSKSKSKSKS");
                    $("#bookInfoResult").append("<p>"+title + " by " + author + " is located right here!</p>");
                    //*****the problem here is that marker copies can be made for an already existing book
                }
                else{
                $("#bookInfo").empty().append("Did you mean "+ title +
                    " by " + author + "? &nbsp;&nbsp;&nbsp;<span class='yesorno'><button type='button' class = 'yes btn btn-default "+
                    data[0]["pk"]+"'>Yes</button>");
                    //copy and paste right after Yes</button>the below for no feature.
                    //<button type = 'button' class = 'no btn btn-default "+
                    //data[0]["pk"]+"'>No&nbsp;</button></span>
//                $('body').on("click", ".no", function(){
//                    $("bookInfo").empty();
//                    for( var x =1; x<data.length; x++){
//                        console.log(title);
//                    }
//                });

                $('body').on("click", ".yes", function(){ // actually yes.onclick works
//                  console.log(data);
//                  console.log(title);
                    //"for time, put this into append beginning: <p>Year: </p> <input type = 'text' id='user_time'>" +
                    $("#bookInfo").empty().append("<span class='input-group'><input type = 'text' id= 'user_place' class = 'form-control' placeholder = 'Add Setting'><span class = 'input-group-btn'><button class = 'btn btn-default' id='user_submit'>Submit</button></span></span>");

                    $("#user_submit").on("click", function(){
                        //ifstatement here to make sure time is a number format
//                        var user_time = parseInt($("#user_time").val());
                        var user_place = $("#user_place").val();
                        user_place = user_place.replace(/ /g,"+");
//                        $("#user_time").attr("value", "");
//                        $("#user_place").attr("value", "");
//                        $("#bookInfo").empty();

                        $.ajax({
                            url:"https://maps.googleapis.com/maps/api/geocode/json?address="+user_place+"&key=AIzaSyDTM4fGWQ4C83C3WtC6ml7kZgmRhI0wgVk",
                            type:"GET",
                            success: function(geodata){
                                console.log(title);
                                var lat = geodata["results"][0]["geometry"]["location"]["lat"];
                                var lng = geodata["results"][0]["geometry"]["location"]["lng"];
                                console.log(lat);
                                console.log(lng);
                                console.log(user_place);
                                var newMarker = addMarker(map, lat, lng, user_place);
                                addInfoWindow(map, newMarker, title, author, info, image, user_place);
                                map.setCenter(newMarker.getPosition());

                                map.setZoom(7);
                                $("#bookInfo").empty();
                                $("#bookInfoResult").append("Book added!");
                                var user_geodata ={
                                    title: title,
                                    place: user_place,
                                    lat: lat,
                                    lng: lng,
//                                    time: user_time
                                };

                                var user_geodata_json = JSON.stringify(user_geodata);
                                console.log(user_geodata_json);
                                addPlaceTimeAjax(user_geodata_json);
                                console.log("WHOA WHOA WHOA");


                            },
                            error: function(geodata){
                                console.log("request error with gugggle");
                            }
                        });

                    });

                });
                }//else matching bracket
            },
            error: function(data){
                console.log("ERROROROROROR");
            }

        });
        });
    });
//    $("#addBookButton").bind('keypress', function(e){
//        var code = e.keyCode || e.which;
//        if (code==13){
//            console.log("enter pressed");
//        $("#addBookButton").click();
//        }
//    });

//})