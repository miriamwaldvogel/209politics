var schools = function(){
  b = document.getElementById("schooldropdown");
  if (b.style.display === "block"){
    b.style.display = "none";
  }else{
    b.style.display = "block";
  }
};
window.onload = function(){
  window.setInterval("reload();", 60000);
  var c = 60;
  window.setInterval(function(){
    document.getElementById("refreshing").innerHTML = "Refreshing in "+c+" seconds";
    c-=1;
    if (c < 0){
      c = 60;
    }
  }, 1000)
};
var reload = function(){
    var d = document.getElementsByClassName("results");
    for (var i = 0; i < d.length; i++){
      d[i].src = d[i].src;
    }
};
