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