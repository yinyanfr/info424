/**
 * Created by Ian on 2015/3/28.
 */
//Global
var waterLevel = 0.3;

var oneStep = 0.1;

var stepOn = oneStep *  $("#can").height();

function adjust(destination,up,step){
    if(up){
        $(destination).height($(destination).height() - step);
        waterLevel += step/$("#can").height();
    }
    else{
        $(destination).height($(destination).height() + step);
        waterLevel -= step/$("#can").height();
    }

   displayWaterLevel("#level");

}

function displayWaterLevel(destination){
    $(destination).html("Process : "+100*waterLevel+"%");
    exam();
}

function exam(){
    $("#ajouter").show();
    $("#deminuer").show();
    if(waterLevel >= 1) {
        waterLevel = 1;
        $("#ajouter").hide();
    }
    if(waterLevel <= 0){
        waterLevel = 0;
        $("#deminuer").hide();
    }
}

function percent(destination){
    var gage = "";
    for(var i = 10; i>-1; i--){
        gage += "<div id=i class=percent>" + i*10 + "%</div>";
    }
    $(destination).html(gage);
    $(".percent").css("line-height",2.3)
}

//Main

$(document).ready(function(){
    percent("#percentage");
    $("#cover").height($("#can").height() * (1 -waterLevel));
    displayWaterLevel("#level");
    $("#ajouter").click(function(){
        adjust("#cover",true,20);
    });

    $("#deminuer").click(function(){
        adjust("#cover",false,20);
    });

    $("#vider").click(function(){
        $("#cover").height($("#can").height());
        waterLevel = 0;
        displayWaterLevel("#level");
    });
});