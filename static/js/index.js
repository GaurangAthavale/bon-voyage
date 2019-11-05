$(document).ready(function(){

    $(".search-flights").hide();
    $(".search-trains").hide();
    $(".search-hotels").hide();

    $("#show-flt-srch").click(function(){
        $(".why-choose-us").hide();
        $(".search-trains").hide();
        $(".search-hotels").hide();
        $(".search-flights").show();
    });
});

$(document).ready(function(){

    $(".search-trains").hide();
    $(".search-hotels").hide();

    $("#show-trn-srch").click(function(){
        $(".why-choose-us").hide();
        $(".search-flights").hide();
        $(".search-hotels").hide();
        $(".search-trains").show();
    });
});

$(document).ready(function(){

    $(".search-trains").hide();
    $(".search-flights").hide();

    $("#show-htl-srch").click(function(){
        $(".why-choose-us").hide();
        $(".search-flights").hide();
        $(".search-trains").hide();
        $(".search-hotels").show();
    });
});

$(document).ready(function(){
    $(".q").hide();
    $(".w").show();
    $("#o").click(function(){
        $(".q").hide();
        $(".w").show();
    });
    $("#r").click(function(){
        $(".w").hide();
        $(".q").show();
    });
});

$(document).ready(function(){
    $(".q1").hide();
    $(".w1").show();
    $("#on").click(function(){
        $(".q1").hide();
        $(".w1").show();
    });
    $("#ro").click(function(){
        $(".w1").hide();
        $(".q1").show();
    });
});

$(document).ready(function(){
    
    $("#addRoomBtn").click(function(){
        console.log('Add room');

        var roomsIpDiv = document.getElementById("rooms-ip");

        var lastOne = roomsIpDiv.lastElementChild.lastElementChild.getAttribute('name');
        console.log(lastOne);
        var num = parseInt(lastOne.substr(-1));
        console.log(num);
        console.log(num + 1);

        var newRoom = document.createElement('div');
        newRoom.className = "input-grp-2";

        var labelNode = document.createElement('label');
        var label = document.createTextNode('Room ' + (num+1));
        labelNode.appendChild(label);
        newRoom.appendChild(labelNode);

        var inputNode = document.createElement('input');
        inputNode.className = "form-control";
        inputNode.setAttribute('type','number');
        inputNode.setAttribute('value',1);
        inputNode.setAttribute('min',1);
        inputNode.setAttribute('max',3);
        inputNode.name = "room"+(num+1);
        newRoom.appendChild(inputNode);

        roomsIpDiv.appendChild(newRoom);
        });        
});