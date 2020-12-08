function format(){
  document.getElementById(document.getElementById("formatid").content).style.height = Math.max(document.getElementById("leftpanel").offsetHeight, document.getElementById("rightpanel").offsetHeight)+10+'px';
}
window.onload = function(){
  format();
};
