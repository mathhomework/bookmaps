function createBook(){
    $.ajax({
        url:/user_create_book/,
        type:"POST",
        data: user_data,
        dataType:"json",
        success:function(data){

        },
        error: function(data){

        }
    })
}

$(document).ready(function(){

function addPlaceTimeAjax(ddata){
    console.log("HAAAAAAY");
     $.ajax({
        url:"/add_place_time/",
        type:"POST",
        data:ddata,
        dataType:"json"
     });
}

    $("#addBookButton").on("click", function(){
//        yo();
        var book = $("#addBook").val();
        $('#addBook').attr("value", "");
        var data = {book:book};
        var new_data = JSON.stringify(data);
        $.ajax({
            url:/add_book/,
            type:"POST",
            data:new_data,
            dataType:"json",
            success: function(data){
                //data returned should have an object with everything but image and info populated,
                //everything populated, or nothing populated at all.
                var title = data[0]["fields"]["title"];
                var info = data[0]["fields"]["info"];
                var image = data[0]["fields"]["image"];
                var author = data[0]["fields"]["author"]["name"];



                console.log(data[0]["fields"]["title"]);
                if(data[0]["fields"]["time"] && data[0]["fields"]["place"]){
                    //cases that fall into this conditional include new objs or old objs with full data.
                    var lat = data[0]["fields"]["place"]["lat"];
                    var lng = data[0]["fields"]["place"]["lng"];
                    var place = data[0]["fields"]["place"]["name"];
                    var foundMarker = addMarker(map, lat, lng, place);
                    addInfoWindow(map, foundMarker, title, author, info, image);
                    map.setCenter(foundMarker.getPosition());
                    map.setZoom(7);
                    $("#bookInfo").empty();
                    $("#bookInfo").append("<h5>"+title + " by " + author + "added</h5>");
                    //*****the problem here is that marker copies can be made for an already existing book
                }
                else{
                $("#bookInfo").empty();
                $("#bookInfo").append("<p>Did you mean "+ title +
                    " by " + author + "?</p><button class = 'yes "+
                    data[0]["pk"]+"'>Yes</button><button class = 'no "+
                    data[0]["pk"]+"'>No</button>");
//                $('body').on("click", ".no", function(){
//                    $("bookInfo").empty();
//                    for( var x =1; x<data.length; x++){
//                        console.log(title);
//                    }
//                });

                $('body').on("click", ".yes", function(){ // actually yes.onclick works
//                  console.log(data);
//                  console.log(title);
                    $("#bookInfo").empty();
                    $("#bookInfo").append("<p>Year: <input type = 'text' id='user_time'>" +
                        "Place: <input type = 'text' id= 'user_place'><button id='user_submit'>Submit</button></p>");

                    $("#user_submit").on("click", function(){
                        //ifstatement here to make sure time is a number format
                        var user_time = parseInt($("#user_time").val());
                        var user_place = $("#user_place").val();
                        user_place = user_place.replace(/ /g,"+");
//                        $("#user_time").attr("value", "");
//                        $("#user_place").attr("value", "");
                        $("#bookInfo").empty();
                        console.log(user_time);
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
                                addInfoWindow(map, newMarker, title, author, info, image);
                                map.setCenter(newMarker.getPosition());

                                map.setZoom(7);

                                var user_geodata ={
                                    title: title,
                                    place: user_place,
                                    lat: lat,
                                    lng: lng,
                                    time: user_time
                                };

                                var user_geodata_json = JSON.stringify(user_geodata);
                                console.log(user_geodata_json);
                                addPlaceTimeAjax(user_geodata_json);


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
//            .complete(function(data){
//            $(".result").on("click", function() {
//                console.log(data);
////                console.log(title);
//                $("#bookInfo").empty();
//                $("#bookInfo").append("<p>Year: <input type = 'text' id='user_time'>" +
//                    "Place: <input type = 'text' id= 'user_place'><button id='user_submit'>Submit</button></p>");
//
//                $("#user_submit").on("click", function(){
//                    var user_year = $("#user_time").val();
//                    var user_place = $("#user_place").val();
//                    console.log(user_year);
//                    //ifstatement here to make sure year is a number format
//                     $.ajax({
//                        url:/user_create_book/,
//                        type:"POST",
//                        data: user_data,
//                        dataType:"json",
//                        success:function(data){
//
//                        },
//                        error: function(data){
//
//                        }
//                     })
//                })
//            })
//            });


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