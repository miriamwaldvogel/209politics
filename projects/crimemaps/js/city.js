function show(e) {
  var a = e.target.nextElementSibling;
  a.style.display = "block";
  a.nextElementSibling.style.display = "block";
  e.target.style.display = "none";
};
function hide(e) {
  var a = e.target.previousElementSibling;
  a.style.display = "none";
};
function relayer(){
  var filterlayer = [];
  for (var i = 0; i < markers.length; i++) {
    if (markers[i].properties.appear === 1) {
      filterlayer.push(markers[i])
    }
  }
  map.removeLayer(mainlayer);
  mainlayer = L.geoJSON(filterlayer, {
    onEachFeature: onEachFeature
  }).addTo(map);
}
function datefilter(se) {
  var s = Date.parse(document.getElementById("startdate").value);
  var e = Date.parse(document.getElementById("enddate").value);
  if (se === 'start') {
    for (var i = 0; i < markers.length; i++) {
      if (Date.parse(markers[i].properties.date) < s) {
        markers[i].properties.appear = 0;
      } else if (Date.parse(markers[i].properties.date) <= e){
        markers[i].properties.appear = 1;
      }
    }
  } else {
    for (var i = 0; i < markers.length; i++) {
      if (Date.parse(markers[i].properties.date) > e) {
        markers[i].properties.appear = 0;
      } else if ((Date.parse(markers[i].properties.date) >= s)) {
        markers[i].properties.appear = 1;
      }
    }
  }
  relayer();
}
function filter(t) {
  var a = document.getElementById(t.replaceAll(" ", "-"));
  if (a.checked) {
    for (var i = 0; i < markers.length; i++) {
      if (types[t].includes(markers[i].properties.type)) {
        markers[i].properties.appear = 1;
      }
    }
  } else {
    for (var i = 0; i < markers.length; i++) {
      if (types[t].includes(markers[i].properties.type)) {
        markers[i].properties.appear = 0;
      }
    }
  }
  relayer();
}
function showall(){
  for (var i = 0; i < markers.length; i++){
    markers[i].properties.appear = 1;
  }
  relayer();
}
