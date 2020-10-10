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
    document.getElementById("covidcontainer").style.height = +document.getElementById("leftpanel").offsetHeight-20+'px';
    document.getElementById("coviddatacontainer").style.height = document.getElementById("leftpanel").offsetHeight-150+'px';
    document.getElementById("rightpanel").style.height =document.getElementById("leftpanel").offsetHeight+'px';
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

function searchtoggle(){
  if (window.innerWidth <= 870){
    f = document.getElementById("formcontainer2");
  } else{
    f = document.getElementById("formcontainer1");
  }
  if (f.style.display === "inline-block"){
    f.style.display = "none";
    document.getElementById("searchimgcontainer").style.top = 7+'px';
  } else{
    f.style.display = "inline-block";
    document.getElementById("searchimgcontainer").style.top = -5+'px';
  }
}
