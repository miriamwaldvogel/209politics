function votes(){
  var y = document.getElementById("yes");
  var n = document.getElementById("no");
  var yv = parseInt(y.innerHTML);
  var nv = parseInt(n.innerHTML);
  var t = yv+nv;
  var w = document.getElementById("main").offsetWidth - Math.max(y.offsetWidth, n.offsetWidth);
  document.getElementById("yescontainer").style.width = w*(yv/t)+'px';
  document.getElementById("nocontainer").style.width = w*(nv/t)+'px';
}
window.onload = function(){
  var y = document.getElementById("yes");
  var n = document.getElementById("no");
  var yv = parseInt(y.innerHTML);
  var nv = parseInt(n.innerHTML);
  var t = yv+nv;
  if(t>0){
    y.innerHTML += " votes - "+ ((yv/t)*100).toFixed(2) + '%';
    n.innerHTML += " votes - "+ ((nv/t)*100).toFixed(2) + '%';
    var w = document.getElementById("main").offsetWidth - Math.max(y.offsetWidth, n.offsetWidth);
    document.getElementById("yescontainer").style.width = w*(yv/t)+'px';
    document.getElementById("nocontainer").style.width = w*(nv/t)+'px';
    document.getElementById("total").innerHTML += t+" votes";
  }
};
