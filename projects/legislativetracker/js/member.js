var para = {'flora': {'status': {'Introduced': [0]}, 'committees': {'Not assigned': [0]}, 'area': {'COVID-19': [0]}, 'role': {'sponsor': [], 'cosponsor': [0]}, 'date': ['12/10/20'], 'type': {'Bill': [0]}}};
window.onscroll = function(){
  if (window.innerWidth <= 700){
    if (window.pageYOffset > 10){
      document.getElementById("filterimgcontainer").style.height = "50px";
      document.getElementById("filterimgcontainer").style.display = "block";
      document.getElementById("filterimg").style.height = "50px";
      document.getElementById("filterimg").style.display = "block";
    } else{
      document.getElementById("filterimgcontainer").style.height = "0px";
      document.getElementById("filterimg").style.height = "0px";
    }
  }
};
function filterclose(){
  document.getElementById("filteroverlay").style.height = "0px";
}
function filterresize(){
  var a = document.getElementById("filteroverlay");
  if (window.innerWidth <= 701){
    a.style.left = (window.innerWidth - a.offsetWidth)/2+'px';
  } else{
    document.getElementById("filterimgcontainer").style.display = "none";
  }
}
function filtershow(){
  var h = "550px";
  f = document.getElementById("filteroverlay");
  if (f.style.height === h){
    f.style.height = "0px";
  } else{
    f.style.height = h;
  }
  filterresize();
}
var l = document.getElementsByClassName("leg");
function filter(pol, check, category){
  var a = document.getElementById(check.replaceAll(" ", "-"));
  var b = para[pol][category][check];
  var s = Date.parse(document.getElementById("startdate").value);
  var e = Date.parse(document.getElementById("enddate").value);
  if (isNaN(s)){
    s = Date.parse('12/01/2020');
  }
  if (isNaN(e)){
    e = Date.now();
  }
  if (a.checked){
    for (var i = 0; i < b.length; i++){
      if (s <= Date.parse(para[pol]['date'][i]) && Date.parse(para[pol]['date'][i]) <= e){
        l[b[i]].classList.remove("hide");
      }
    }
  } else{
    for (var i = 0; i < b.length; i++){
      if (s <= Date.parse(para[pol]['date'][i]) && Date.parse(para[pol]['date'][i]) <= e){
        l[b[i]].classList.add("hide");
      }
    }
  }
}
function datefilter(p, se){
  if (se === 'start'){
    var d = Date.parse(document.getElementById("startdate").value);
    for (var i = 0; i < l.length; i++){
      if (Date.parse(para[p]['date'][i]) < d){
        l[i].classList.add("hide");
      } else{
        l[i].classList.remove("hide");
      }
    }
  } else{
    var d = Date.parse(document.getElementById("enddate").value);
    for (var i = 0; i < l.length; i++){
      if (Date.parse(para[p]['date'][i]) > d){
        l[i].classList.add("hide");
      } else{
        l[i].classList.remove("hide");
      }
    }
  }
}
function showall(){
  for (var i = 0; i < l.length; i++){
    l[i].classList.remove("hide");
  }
}
