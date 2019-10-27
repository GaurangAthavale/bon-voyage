$(document).ready(function() {
    $(".trip").hide();
    $("input[name$='check']").click(function() {
        var test = $(this).val();
        $(".trip").hide();
        $("#" + test).show();
    });
});


// $(function() {
//     $("[name=check]").click(function(){
//             $('.rt').hide();
//             $('.ow').hide();
//             $("#r").show('slow');
//     });
//  });

// $(function() {
//     $("[name=checker]").click(function(){
//             $('.rt').hide();
//             $('.ow').hide();
//             $("#o").show('slow');
//     });
//  });

// $(document).ready(function(){
//     $('.rt').hide();
//     $('.ow').hide();
//     $('input[type="radio"]').click(function(){
//         var inputValue = $(this).attr("value");
//         var targetBox = $("." + inputValue);
//         $(".").not(targetBox).hide();
//         $(targetBox).show();
//     });
// });

// function func(x)
// {       
//     $(document).ready(function(){
//     $('.rt').hide();
//     $('.ow').hide();
//     });

//     if(x==0)
//         document.getElementById('r').style.display='block';
//         document.getElementById('o').style.display='none';
//     else if(x==1)
//         document.getElementById('o').style.display='block';
//     return;
// }