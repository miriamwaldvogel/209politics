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
  if (isNaN(e)){
    e = Date.now();
  }
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
      } else if (Date.parse(markers[i].properties.date) >= s){
        markers[i].properties.appear = 1;
      }
    }
  }
  relayer();
}
function filter(t) {
  var a = document.getElementById(t.replaceAll(" ", "-"));
  var s = Date.parse(document.getElementById("startdate").value);
  var e = Date.parse(document.getElementById("enddate").value);
  if (isNaN(e)){
    e = Date.now();
  }
  if (a.checked) {
    for (var i = 0; i < markers.length; i++) {
      markerdate = Date.parse(markers[i].properties.date);
      if (types[t].includes(markers[i].properties.type) && s <= markerdate && markerdate <= e) {
        markers[i].properties.appear = 1;
      }
    }
  } else {
    for (var i = 0; i < markers.length; i++) {
      markerdate = Date.parse(markers[i].properties.date);
      if (types[t].includes(markers[i].properties.type) && s <= markerdate && markerdate <= e) {
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
function filtertoggle(){
  var f = document.getElementById("filtercontainer");
  var fi = document.getElementById("filterimgcontainer");
  if (f.style.width === "250px"){
    f.style.width = "0px";
    fi.innerHTML = '<img src="images/leaflet-control.png" alt="Filters" id="filterimg">';
    fi.classList.remove("filterx");
    fi.classList.add("filterimgcontainer");
  } else{
    f.style.width = "250px";
    fi.innerHTML = "&times";
    fi.classList.add("filterx");
    fi.classList.remove("filterimgcontainer");
  }
}
