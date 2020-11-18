function resizetop(){
  if (window.innerWidth > 620){
    document.getElementById("topcontainer").style.height = Math.max(document.getElementById("leftpanel").offsetHeight,document.getElementById("rightpanel").offsetHeight)+10+'px';
  }
  else{
    document.getElementById("topcontainer").style.height = document.getElementById("leftpanel").offsetHeight + document.getElementById("rightpanel").offsetHeight+10+'px';
  }
}
window.onload = function(){
  resizetop();
};
