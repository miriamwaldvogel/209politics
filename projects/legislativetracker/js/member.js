var para = {'flora': {'status': {'Passed Assembly': [2, 3, 4], 'Introduced': [0, 1, 5, 6, 7]}, 'committees': {'Rules': [2, 3], 'Not assigned': [0, 1, 4, 5, 6, 7]}, 'area': {'Firefighting': [1], 'Hazardous waste': [7], 'COVID-19': [0], 'Holidays': [2, 3, 6], 'Other': [4], 'Healthcare': [5]}, 'role': {'sponsor': [5, 6], 'cosponsor': [0, 1, 2, 3, 4, 7]}, 'date': ['12/10/20', '1/11/21', '1/8/21', '12/7/20', '12/7/20', '1/19/21', '1/21/21', '1/21/21'], 'type': {'Assembly concurrent resolution': [2, 3, 6], 'Bill': [0, 1, 5, 7], 'Assembly resolution': [4]}}, 'cooper': {'status': {'Passed Assembly': [5, 6, 8, 9], 'Introduced': [0, 1, 2, 3, 4, 7, 10]}, 'committees': {'Rules': [5, 8], 'Public Safety': [2, 3], 'Governmental Organization': [1], 'Not assigned': [0, 4, 6, 7, 9, 10]}, 'area': {'State bodies': [1], 'Housing': [4], 'Holidays': [5, 8], 'Cannabis': [0], 'Other': [6, 9], 'Healthcare': [10], 'Peace officers': [2], 'Crime': [7], 'Bail': [3]}, 'role': {'sponsor': [0, 1, 2, 3, 7], 'cosponsor': [4, 5, 6, 8, 9, 10]}, 'date': ['12/16/20', '12/7/20', '12/7/20', '12/7/20', '12/7/20', '1/8/21', '1/11/21', '1/15/21', '12/7/20', '12/7/20', '1/15/21'], 'type': {'Assembly concurrent resolution': [5, 8], 'Bill': [0, 1, 2, 3, 4, 7, 10], 'Assembly resolution': [6, 9]}}, 'harder': {'status': {'Passed House': [0], 'Introduced': [1, 2, 3]}, 'committees': {'Natural Resources': [2, 3], 'Judiciary': [0, 2], 'Energy and Commerce': [2], 'Foreign Affairs': [2], 'Financial Services': [1, 2], 'Ways and Means': [2]}, 'area': {'Not assigned': [1, 2, 3], 'Congress': [0]}, 'role': {'sponsor': [], 'cosponsor': [0, 1, 2, 3]}, 'date': ['1/11/21', '1/13/21', '1/4/21', '1/21/21'], 'type': {'Bill': [1, 2, 3], 'Resolution': [0]}}, 'villapudua': {'status': {'Passed Assembly': [2, 3, 6, 7], 'Introduced': [0, 1, 4, 5]}, 'committees': {'Rules': [3, 6], 'Not assigned': [0, 1, 2, 4, 5, 7]}, 'area': {'Alcohol': [4], 'Taxation': [0], 'Holidays': [3, 6], 'Other': [2, 7], 'Homelessness': [5], 'Emergency food assistance': [1]}, 'role': {'sponsor': [0, 4, 5], 'cosponsor': [1, 2, 3, 6, 7]}, 'date': ['1/11/21', '1/11/21', '1/11/21', '1/8/21', '1/13/21', '1/15/21', '12/7/20', '12/7/20'], 'type': {'Assembly resolution': [2, 7], 'Bill': [0, 1, 4, 5], 'Assembly concurrent resolution': [3, 6]}}, 'mcnerney': {'status': {'Passed House': [3], 'Introduced': [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]}, 'committees': {'Natural Resources': [4, 7, 18], 'Transportation and Infrastructure': [8], 'Rules': [1, 5, 6], 'House Administration': [2, 11], 'Oversight and Reform': [1], 'Judiciary': [0, 1, 2, 3, 5, 7, 11, 14, 15], 'Energy and Commerce': [1, 7, 17], 'Foreign Affairs': [7], 'Financial Services': [7, 10, 12], 'Ways and Means': [7], 'Science, Space, and Technology': [17], 'Ethics': [6, 9, 13, 16], 'Armed Services': [1]}, 'area': {'Crime and Law Enforcement': [11], 'Government operations and politics': [1, 2], 'Civil rights and liberties': [0], 'Not assigned': [4, 6, 7, 8, 9, 10, 12, 14, 15, 17, 18], 'Congress': [3, 5, 13, 16]}, 'role': {'sponsor': [], 'cosponsor': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]}, 'date': ['1/4/21', '1/4/21', '1/4/21', '1/11/21', '1/11/21', '1/11/21', '1/12/21', '1/4/21', '1/13/21', '1/13/21', '1/4/21', '1/12/21', '1/13/21', '1/5/21', '1/19/21', '1/21/21', '1/11/21', '1/25/21', '1/25/21'], 'type': {'Bill': [0, 1, 4, 7, 8, 10, 12, 15, 17, 18], 'Resolution': [2, 3, 5, 6, 9, 11, 13, 14, 16]}}, 'eggman': {'status': {'Introduced': [0, 1, 2, 3, 4]}, 'committees': {'Communications and conveyance': [0], 'Not assigned': [1, 2, 3, 4], 'Local government': [0]}, 'area': {'Foreign policy': [3], 'Communications': [0], 'Housing': [2], 'Taxation': [4], 'Drugs/alcohol': [1]}, 'role': {'sponsor': [4], 'cosponsor': [0, 1, 2, 3]}, 'date': ['12/16/20', '12/7/20', '12/7/20', '1/12/20', '1/21/21'], 'type': {'Bill': [0, 1, 2, 4], 'Assembly joint resolution': [3]}}};
window.onscroll = function(){
  if (window.innerWidth <= 700){
    if (window.pageYOffset > 10){
      document.getElementById("filterimgcontainer").style.height = "50px";
      document.getElementById("filterimgcontainer").style.display = "block";
      document.getElementById("filterimg").style.height = "50px";
      document.getElementById("filterimg").style.display = "block";
    } else{
      document.getElementById("filterimgcontainer").style.height = "0px";
      document.getElementById("filterimg").style.height = "0px";
    }
  }
};
function filterclose(){
  document.getElementById("filteroverlay").style.height = "0px";
}
function filterresize(){
  var a = document.getElementById("filteroverlay");
  if (window.innerWidth <= 701){
    a.style.left = (window.innerWidth - a.offsetWidth)/2+'px';
  } else{
    document.getElementById("filterimgcontainer").style.display = "none";
  }
}
function filtershow(){
  var h = "550px";
  f = document.getElementById("filteroverlay");
  if (f.style.height === h){
    f.style.height = "0px";
  } else{
    f.style.height = h;
  }
  filterresize();
}
var l = document.getElementsByClassName("leg");
function filter(pol, check, category){
  var a = document.getElementById(check.replaceAll(" ", "-"));
  var b = para[pol][category][check];
  var s = Date.parse(document.getElementById("startdate").value);
  var e = Date.parse(document.getElementById("enddate").value);
  if (isNaN(s)){
    s = Date.parse('12/01/2020');
  }
  if (isNaN(e)){
    e = Date.now();
  }
  if (a.checked){
    for (var i = 0; i < b.length; i++){
      if (s <= Date.parse(para[pol]['date'][i]) && Date.parse(para[pol]['date'][i]) <= e){
        l[b[i]].classList.remove("hide");
      }
    }
  } else{
    for (var i = 0; i < b.length; i++){
      if (s <= Date.parse(para[pol]['date'][i]) && Date.parse(para[pol]['date'][i]) <= e){
        l[b[i]].classList.add("hide");
      }
    }
  }
}
function datefilter(p, se){
  if (se === 'start'){
    var d = Date.parse(document.getElementById("startdate").value);
    for (var i = 0; i < l.length; i++){
      if (Date.parse(para[p]['date'][i]) < d){
        l[i].classList.add("hide");
      } else{
        l[i].classList.remove("hide");
      }
    }
  } else{
    var d = Date.parse(document.getElementById("enddate").value);
    for (var i = 0; i < l.length; i++){
      if (Date.parse(para[p]['date'][i]) > d){
        l[i].classList.add("hide");
      } else{
        l[i].classList.remove("hide");
      }
    }
  }
}
function showall(){
  for (var i = 0; i < l.length; i++){
    l[i].classList.remove("hide");
  }
}
