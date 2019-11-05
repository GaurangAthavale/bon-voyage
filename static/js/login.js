$(document).ready(function(){
    $(".signup").hide();
    $(".login").show();

    $("#login1").click(function(){
        $(".signup").hide();
        $(".login").show();
    });

    $("#signup1").click(function(){
        $(".login").hide();
        $(".signup").show();
    });
});  