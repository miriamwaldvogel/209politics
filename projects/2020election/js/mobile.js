window.onload = function(){
  var l = [["0: Federal", "https://datastudio.google.com/embed/reporting/31f8fa53-76a4-4280-9193-1d3a9dd2f3f5/page/J3jlB"]];
  if (window.innerWidth <= 667){
    document.getElementsByTagName("iframe")[0].src = l[document.getElementById("linknum").content][1];
  }
};
