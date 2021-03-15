if (document.getElementById("sponsors").offsetHeight > 31){
  document.getElementById("togglesponsors").innerHTML = "Show all";
  document.getElementById("sponsors").style.height = "1.4em";
}
function sponsortoggle(){
  var a = document.getElementById("sponsors");
  var b = document.getElementById("togglesponsors");
  if (a.style.height === "1.4em"){
    a.style.height = null;
    b.innerHTML = "Hide all";
  } else{
    a.style.height = "1.4em";
    b.innerHTML = "Show all";
  }
}
