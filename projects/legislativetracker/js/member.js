var para = {'role': {'sponsor': [3, 4], 'cosponsor': [0, 1, 2]}, 'status': {'intro': [0, 1, 2, 3], 'house': [4], 'senate': [], 'topres': [], 'law': [], 'resdif': [], 'veto': []}};
window.onscroll = function(){
  if (window.innerWidth < 900){
    if (window.pageYOffset > 10){
      document.getElementById("filterimgcontainer").style.height = "50px";
      document.getElementById("filterimg").style.height = "50px";
    } else{
      document.getElementById("filterimgcontainer").style.height = "0px";
      document.getElementById("filterimg").style.height = "0px";
    }
  }
};
function filterclose(){
  document.getElementById("filteroverlay").style.height = "0px";
}
function filtershow(){
  var h = "380px";
  f = document.getElementById("filteroverlay");
  if (f.style.height === h){
    f.style.height = "0px";
  } else{
    f.style.height = h;
  }
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
