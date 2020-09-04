window.onload = function(){
  document.getElementById("bolded").innerHTML = ' '+Math.floor((new Date("11/03/2020").getTime()- new Date().getTime())/(1000*3600*24))+' days.';
};
