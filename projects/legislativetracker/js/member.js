if (window.innerWidth > 899){
  var a = (document.getElementById("textinfo").offsetHeight - document.getElementById("introinfo").offsetHeight - 50);
  if (a > 250){
    document.getElementById("map").style.height = a+'px';
  }
}
var para = {'flora': {'status': {'Introduced': [0]}, 'role': {'sponsor': [], 'cosponsor': [0]}, 'type': {'Bill': [0]}, 'date': ['12/10/2020'], 'area': {'COVID-19': [0]}}, 'cooper': {'status': {'Introduced': [0, 1, 2, 3, 4]}, 'role': {'sponsor': [0, 1, 2, 3], 'cosponsor': [4]}, 'type': {'Bill': [0, 1, 2, 3, 4]}, 'date': ['12/16/2020', '12/7/2020', '12/7/2020', '12/7/2020', '12/7/2020'], 'area': {'Cannabis': [0], 'Housing': [4], 'Peace officers': [2], 'Bail': [3], 'State bodies': [1]}}, 'harder': {'status': {'House Veto Override': [4], 'Failed Senate Committee': [2], 'Introduced': [0], 'Resolving Differences': [3], 'Failed House Committee': [1]}, 'role': {'sponsor': [3, 4], 'cosponsor': [0, 1, 2]}, 'type': {'Bill': [0, 1, 2, 3, 4]}, 'date': ['12/16/2020', '12/3/2020', '11/24/2020', '8/14/2020', '8/14/2020'], 'area': {'Education': [2], 'Not assigned': [0, 1], 'Water Resources Development': [3, 4]}}, 'villapudua': {'status': {}, 'role': {'sponsor': [], 'cosponsor': []}, 'type': {}, 'date': [], 'area': {}}, 'mcnerney': {'status': {'Introduced': [0, 1, 2]}, 'role': {'sponsor': [], 'cosponsor': [0, 1, 2]}, 'type': {'Bill': [0, 1], 'Resolution': [2]}, 'date': ['1/4/2021', '1/4/2021', '1/4/2021'], 'area': {'Not assigned': [0, 1, 2]}}, 'eggman': {'status': {'Introduced': [0, 1, 2]}, 'role': {'sponsor': [], 'cosponsor': [0, 1, 2]}, 'type': {'Bill': [0, 1, 2]}, 'date': ['12/16/2020', '12/7/2020', '12/7/2020'], 'area': {'Communications': [0], 'Housing': [2], 'Drugs/alcohol': [1]}}};
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
