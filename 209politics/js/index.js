window.onload = function(){
  var days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
  var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  var d = new Date();
  document.getElementById("date").innerHTML = days[d.getDay()]+", "+months[d.getMonth()]+" "+d.getDate().toString()+", "+d.getFullYear().toString();
};
