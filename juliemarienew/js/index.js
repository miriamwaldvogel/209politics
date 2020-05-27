function en(){
  var e = document.getElementsByClassName("english");
  var f = document.getElementsByClassName("francais");
  for(var i = 0; i < e.length; i++){
    e[i].style.display="block";
  }
  for(var j = 0; j < f.length; j++){
    f[j].style.display="none";
  }
  document.getElementById("languagenav").innerHTML = "Version français";
  document.getElementById("homenav").href = "indexen.html";
  document.getElementById("locationsnav").href = "locationsen.html";
  document.getElementById("historynav").href = "historyen.html";
  document.getElementById("guidelinesnav").href = "guidelinesen.html";
  document.getElementById("contactnav").href = "contacten.html";
  document.getElementById("languagenav").href = "indexfr.html";
}
function fr(){
  var e = document.getElementsByClassName("english");
  var f = document.getElementsByClassName("francais");
  for(var k = 0; k < e.length; k++){
    e[k].style.display="none";
  }
  for(var l = 0; l < f.length; l++){
    f[l].style.display="block";
  }
  document.getElementById("languagenav").innerHTML = "English version";
  document.getElementById("homenav").href = "indexfr.html";
  document.getElementById("locationsnav").href = "locationsfr.html";
  document.getElementById("historynav").href = "historyfr.html";
  document.getElementById("guidelinesnav").href = "guidelinesfr.html";
  document.getElementById("contactnav").href = "contactfr.html";
  document.getElementById("languagenav").href = "indexen.html";
}
window.onload = function(){
  var lang = navigator.language || navigator.userLanguage;
  if(lang.substring(0, 2) == "fr"){
    fr();
  }
  else{
    en();

  }
};
function language(){
  var lang = document.getElementById("languagenav").innerHTML;
  if(lang=="English version"){
    en();
  }
  else{
    fr();
  }
}
