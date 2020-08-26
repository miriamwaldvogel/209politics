function resize(){
  var c = document.getElementsByClassName("bigstory");
  var t = document.getElementsByClassName("storytextcontainer");
  var i = document.getElementsByClassName("storyimgcontainer");
  var h = 0;
  if (window.innerWidth <= 667){
    for(var k = 0; k < c.length; k++){
      c[k].style.height = (t[k].offsetHeight+i[k].offsetHeight+10)+'px';
    }
  }else{
    for(var j = 0; j < c.length; j++){
      c[j].style.height = (Math.max(t[j].offsetHeight, i[j].offsetHeight)+20)+'px';
      h += c[j].offsetHeight;
    }
    document.getElementById("covidcontainer").style.height = h+document.getElementById("mainstorycontainer").offsetHeight+'px';
    document.getElementById("coviddatacontainer").style.height = h+document.getElementById("mainstorycontainer").offsetHeight-100+'px';
  }
  var l = document.getElementsByClassName("leftballot");
  var r = document.getElementsByClassName("rightballot");
  for(var m = 0; m < l.length; m++){
    l[m].style.height = Math.max(l[m].offsetHeight, r[m].offsetHeight)+'px';
    r[m].style.height = Math.max(l[m].offsetHeight, r[m].offsetHeight)+'px';
  }
}
window.onload = function(){
  resize();
  var days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
  var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  var d = new Date();
  document.getElementById("date").innerHTML = days[d.getDay()]+", "+months[d.getMonth()]+" "+d.getDate().toString()+", "+d.getFullYear().toString();
};
