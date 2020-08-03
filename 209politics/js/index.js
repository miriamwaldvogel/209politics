function resize(){
  var c = document.getElementsByClassName("storycontainer");
  var t = document.getElementsByClassName("storytextcontainer");
  var i = document.getElementsByClassName("storyimgcontainer");
  for(var j = 0; j < c.length; j++){
    c[j].style.height = (Math.max(t[j].offsetHeight, i[j].offsetHeight)+20)+'px';
  }
}

window.onload = function(){
  var days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
  var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  var d = new Date();
  document.getElementById("date").innerHTML = days[d.getDay()]+", "+months[d.getMonth()]+" "+d.getDate().toString()+", "+d.getFullYear().toString();
  resize();
};
