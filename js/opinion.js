function resizetop(){
  document.getElementById("topcontainer").style.height = Math.max(document.getElementById("leftpanel").offsetHeight, document.getElementById("rightpanel").offsetHeight)+10+'px';
}
window.onload = function(){
  resizetop();
};
