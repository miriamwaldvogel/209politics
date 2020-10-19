function sidebar(){
  b = document.getElementById("sectionscontainer");
  if (b.style.display === "block"){
    b.style.display = "none";
  }else{
    b.style.display = "block";
  }
}
function searchtoggle(){
  if (window.innerWidth <= 870){
    f = document.getElementById("formcontainer2");
    if (f.style.display === "block"){
      f.style.display = "none";
    } else{
      f.style.display = "block";
    }
    document.getElementById("formcontainer1").style.display = "none";
  } else{
    f = document.getElementById("formcontainer1");
    if (f.style.display === "inline-block"){
      f.style.display = "none";
    } else{
      f.style.display = "inline-block";
      document.getElementById("formcontainer2").style.display = "none";
    }
  }
}
