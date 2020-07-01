window.onscroll = function() {
  if(document.documentElement.scrollTop > 20 || document.body.scrollTop > 20){
    document.getElementById("backtotop").style.display = "block";
  }else{
    document.getElementById("backtotop").style.display = "none";
  }
};

function totop(){
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}
