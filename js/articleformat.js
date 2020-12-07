function resize(){
  var c = document.getElementsByClassName("storycontainer");
  var t = document.getElementsByClassName("storytextcontainer");
  var i = document.getElementsByClassName("storyimgcontainer");
  if (window.innerWidth <= 667){
    for(var k = 0; k < i.length; k++){
      c[k].style.height = (t[k].offsetHeight+i[k].offsetHeight+10)+'px';
    }
  }else{
    for(var j = 0; j < i.length; j++){
      c[j].style.height = (Math.max(t[j].offsetHeight, i[j].offsetHeight)+20)+'px';
    }
  }
}
window.onload = function(){
  resize();
  var a = document.getElementById("paragraphcontainer").getElementsByTagName("P");
  for (var i = 0; i < a.length; i++){
    var b = a[i].getElementsByTagName("A");
    for (var j = 0; j < b.length; j++){
      b[j].target = "_blank";
    }
  }
};
