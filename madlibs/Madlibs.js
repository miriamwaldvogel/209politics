function next(){
  var n1 = document.getElementById('noun1').value;
  var a1 = document.getElementById('adj1').value;
  var l = document.getElementById('length').value;
  var t = document.getElementById('time').value;
  var n2 = document.getElementById('noun2').value;
  var ing = document.getElementById('ingverb').value;
  var s = document.getElementById('sound').value;
  var a2 = document.getElementById('adj2').value;
  var n3 = document.getElementById('noun3').value;
  var w = document.getElementById('word').value;
  var usermessage = "The FitnessGram™ Pacer Test is a multistage aerobic capacity "+n1 + " that progressively gets more "+a1+" as it continues. The 20 "+l+" pacer test will begin in 30 "+t+". Line up at the "+n2+". The "+ing+" speed starts slowly, but gets faster each minute after you hear this signal. ["+s+"]. A single lap should be completed each time you hear this sound. [ding] Remember to run in a "+a2+" line, and run as long as possible. The second time you fail to complete a "+n3 + " before the sound, your test is over. The test will begin on the word "+w+". On your mark, get ready, "+w+"!";
  document.getElementById('text').innerHTML = usermessage;
  document.getElementById('page1').style.display = 'none';
  document.getElementById('page2').style.display = 'block';
}
function back(){
  document.getElementById('page2').style.display = 'none';
  document.getElementById('noun1').value = '';
  document.getElementById('adj1').value = '';
  document.getElementById('length').value = '';
  document.getElementById('time').value = '';
  document.getElementById('noun2').value = '';
  document.getElementById('ingverb').value = '';
  document.getElementById('sound').value = '';
  document.getElementById('adj2').value = '';
  document.getElementById('noun3').value = '';
  document.getElementById('word').value = '';
  document.getElementById('page1').style.display = 'block';
}
