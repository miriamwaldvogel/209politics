function language(){
  var lang = document.getElementById('button').innerHTML;
  if(lang=='english'){
    document.getElementById('purpose').innerHTML = 'But: permettre à des femmes défavorisées d\'Indonésie de devenir indépendantes par l’enseignement de la couture.';
    document.getElementById('desc').innerHTML = 'Les cours sont proposés dans diverse villes d’Indonésie. Ils durent en général trois moiset forment vingt femmes. Celles-ci ont chacune une machine à coudre qu’elle pourront acquérir en fin du cours réussi avec un contrat de microcrédit sans intérêt. Nous essayons systématiquement d’avoir des élèves de diverses religions et culture et sans considération de caste!';
    document.getElementById('button').innerHTML='francais';
  }
  else{
    document.getElementById('purpose').innerHTML = 'We seek to empower Indonesian women by offering them sewing courses.';
    document.getElementById('desc').innerHTML = 'The purpose of the foundation is to help underprivileged women through sewing. Numerous courses have been offered throughout Indonesia. They usually last three months and involve twenty students at the most. The students are p</span>rovided with modern sewing machines which they buy, through micro-credit contract, after successful completion of the course. Local teachers are selected by the foundation. They follow a predetermined set of topics that range from basic sewing skills (dresses, pants) to marketing. Our vision is to empower women of various religious and ethnic backgrounds by giving them lasting professional skills, in Indonesia and elsewhere.';
    document.getElementById('button').innerHTML='english';
  }
}
