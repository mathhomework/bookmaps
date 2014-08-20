$(document).ready(function(){
    $("#addBookButton").on("click", function(){
        console.log("add book");
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
                var title = data[0]["fields"]["title"];
                var info = data[0]["fields"]["info"];
                var image = data[0]["fields"]["image"];
                console.log(data);
                console.log(data[0]["fields"]["title"]);
                $("#bookInfo").empty();
                $("#bookInfo").append("<p>Did you mean "+ title +
                    " by " + data[0]["fields"]["author"]["name"]+ "?</p><button class = 'result'id = '"+
                    data[0]["pk"]+"'>Choose Book</button>");

                $('body').on("click", ".result", function(){ // actually result.onclick works
//                  console.log(data);
//                  console.log(title);
                    $("#bookInfo").empty();
                    $("#bookInfo").append("<p>Year: <input type = 'text' id='user_time'>" +
                        "Place: <input type = 'text' id= 'user_place'><button id='user_submit'>Submit</button></p>");

                    $("#user_submit").on("click", function(){
                        var user_year = $("#user_time").val();
                        var user_place = $("#user_place").val();
                        user_place = user_place.replace(/ /g,"+");
//                        $("#user_time").attr("value", "");
//                        $("#user_place").attr("value", "");
                        $("#bookInfo").empty();
                        console.log(user_year);
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
                                addInfoWindow(map, newMarker, title, info, image);
                                

                            },
                            error: function(geodata){
                                console.log("request error with gugggle");
                            }
                        });

//                        addMarker(map, lat, lng, place);

                        //ifstatement here to make sure year is a number format
//                        $.ajax({
//                            url:/user_create_book/,
//                            type:"POST",
//                            data: user_data,
//                            dataType:"json",
//                            success:function(data){
//
//                            },
//                            error: function(data){
//
//                            }
//                        })
                    })

                })

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