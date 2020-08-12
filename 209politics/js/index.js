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
  var s = document.getElementsByClassName("smallstory");
  var u = document.getElementsByClassName("smalltext");
  for(var l = 0; l < s.length; l++){
    s[l].style.height = (u[l].offsetHeight+20)+'px';
  }
}
window.onload = function(){
  resize();
  var days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
  var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  var d = new Date();
  document.getElementById("date").innerHTML = days[d.getDay()]+", "+months[d.getMonth()]+" "+d.getDate().toString()+", "+d.getFullYear().toString();
};
