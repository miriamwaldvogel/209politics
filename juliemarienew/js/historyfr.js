function collapse(){
  var c = document.getElementsByClassName("collapsible");
  var toggle = document.getElementById("collapseall");
  if(toggle.innerHTML === "Ouvrir"){
    for(var i = 0; i < c.length; i++){
      c[i].classList.toggle("active");
      var d = c[i].nextElementSibling;
      d.style.maxHeight = d.scrollHeight + "px";
      toggle.innerHTML = "Fermer";
    }
  }else{
    for(var j = 0; j < c.length; j++){
      c[j].classList.toggle("active");
      var e = c[j].nextElementSibling;
      e.style.maxHeight = null;
      toggle.innerHTML = "Ouvrir";
    }
  }
}
