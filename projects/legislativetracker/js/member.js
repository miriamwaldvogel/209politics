var para = {'role': {'sponsor': [3, 4], 'cosponsor': [0, 1, 2]}, 'status': {'fail2': [2], 'fail1': [], 'veto': [3], 'resdif': [4], 'law': [], 'topres': [], 'senate': [], 'house': [1], 'intro': [0]}, 'area': {'Not assigned': [0, 1], 'Education': [2], 'Water Resources Development': [3, 4]}, 'date': ['12/16/2020', '12/3/2020', '11/24/2020', '8/14/2020', '8/14/2020']};
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
function filter(check, category){
  var a = document.getElementById(check);
  var b = para[category][check];
  if (a.checked){
    for (var i = 0; i < b.length; i++){
      l[b[i]].classList.remove("hide");
    }
  } else{
    for (var i = 0; i < b.length; i++){
      l[b[i]].classList.add("hide");
    }
  }
}
function datefilter(se){
  if (se === 'start'){
    var d = Date.parse(document.getElementById("startdate").value);
    for (var i = 0; i < l.length; i++){
      if (Date.parse(para['date'][i]) < d){
        l[i].classList.add("hide");
      } else{
        l[i].classList.remove("hide");
      }
    }
  } else{
    var d = Date.parse(document.getElementById("enddate").value);
    for (var i = 0; i < l.length; i++){
      if (Date.parse(para['date'][i]) > d){
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
