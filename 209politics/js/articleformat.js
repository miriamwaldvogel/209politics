function resize(){
  var c = document.getElementsByClassName("storycontainer");
  var t = document.getElementsByClassName("storytextcontainer");
  var i = document.getElementsByClassName("storyimgcontainer");
  for(var j = 0; j < c.length; j++){
    c[j].style.height = (Math.max(t[j].offsetHeight, i[j].offsetHeight)+20)+'px';
  }
}
window.onload = function(){
  resize();
};
