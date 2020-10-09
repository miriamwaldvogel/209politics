<?php
$r = new RecursiveIteratorIterator(new RecursiveDirectoryIterator('/home/miriamwaldvogel/209politics/'));
$files = array();
foreach ($r as $file) {
    if ($file->isDir()){
        continue;
    }
    $a = $file->getPathname();
    if (substr($a, -4, -1) == "htm" and substr_count($a, "/") > 4){
      $g = fopen($a, "r");
      $files[$a] = fread($g, filesize($a));
      fclose($g);
    }
}
$key = explode(" ", $_GET["q"]);
$f = array();
foreach($files as $i => $j){
  $t = 0;
  $b = 0;
  foreach($key as $k){
    $a = substr_count(strtoupper($j), strtoupper($k));
    $t+= $a;
    if ($a > 0){
      $b += 1;
    }
  }
  if ($b > 0){
    $f[$i] = array($b, $t);
  }
}

echo "<!DOCTYPE html>
<html lang=\"en\" dir=\"ltr\">
  <head>
    <meta charset=\"utf-8\">
    <meta name=\"description\" content=\"\">
    <meta name=\"keywords\" content=\"\">
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <link rel=\"icon\" type=\"image/png\" href=\"/images/favicon.png\">
    <link rel=\"stylesheet\" href=\"/css/header.css\">
    <link rel=\"stylesheet\" href=\"/css/global.css\">
    <link rel=\"stylesheet\" href=\"/css/search.css\">
    <link href='https://fonts.googleapis.com/css?family=Rubik' rel='stylesheet'>
    <link href=\"https://fonts.googleapis.com/css?family=Libre Baskerville\" rel=\"stylesheet\">
    <script type=\"text/javascript\" src=\"/js/header.js\"></script>
    <script async src=\"https://www.googletagmanager.com/gtag/js?id=UA-174685284-1\"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'UA-174685284-1');
      </script>
    <title>Search - 209 Politics</title>
  </head>
  <body>
    <div id=\"content\">
      <div id=\"headercontainer\">
        <button type=\"button\" id=\"sidebar\" onclick=\"sidebar();\">&#9776;</button>
        <div id=\"logocontainer\">
          <a href=\"https://209politics.com/\">
            <img src=\"/images/favicon-horizontal.png\" alt=\"209 Politics\" id=\"logo\">
          </a>
        </div>
      </div>
      <div id=\"sectionscontainer\" class=\"sections\">
        <div id=\"homenavcontainer\" class=\"headernavcontainer\">
          <a href=\"https://209politics.com/\" id=\"latest\" class=\"section\">HOME</a>
        </div>
        <div id=\"latestnavcontainer\" class=\"headernavcontainer\">
          <a href=\"/latest.html\" id=\"latest\" class=\"section\">LATEST</a>
        </div>
        <div id=\"electionsnavcontainer\" class=\"headernavcontainer\">
          <a href=\"/elections.html\" id=\"elections\" class=\"section\">ELECTIONS</a>
        </div>
        <div id=\"policynavcontainer\" class=\"headernavcontainer\">
          <a href=\"/policy.html\" class=\"section\">POLICY</a>
        </div>
        <div id=\"covidnavcontainer\" class=\"headernavcontainer\">
          <a href=\"/covid-19.html\" class=\"section\">COVID-19</a>
        </div>
        <div id=\"contactnavcontainer\" class=\"headernavcontainer\">
          <a href=\"/contact.html\" class=\"section\">CONTACT US</a>
        </div>
      </div>
      <div id=\"filler\"></div>
      <div id=\"titlecontainer\">
        <h1 id=\"title\">SEARCH</h1>
      </div>
			<div id=\"content\">
";
arsort($f);
foreach($f as $i=>$k){
	if (strpos($i, "202") === false){
    echo sprintf("<div class=\"articlecontainer\">
  		<a href=\"%s\" class=\"articlelink\">
  			<p class=\"articletitle\">%s</p>
				<p class=\"articleinfo\">%s</p>
  		</a>
  	</div>", substr($i, 33, strlen($i)), str_replace(" - 209 Politics", "", explode("</title>", explode("<title>", $files[$i], 2)[1], 2)[0]), explode("</p>", explode(">", explode("<p", $files[$i], 2)[1], 2)[1], 2)[0]);
  } else{
		$p = explode("</p>", explode("class=\"paragraph\">", $files[$i])[1])[0];
		if (strlen($p) > 200){
			$c = explode(".", $p);
			$d = "";
			foreach($c as $l=>$m){
				$d.=$m.".";
				if (strlen($d) > 199){
					break;
				}
			}
			$p = $d;
		}
		echo sprintf("<div class=\"articlecontainer\">
			<a href=\"%s\" class=\"articlelink\">
				<p class=\"articletitle\">%s</p>
				<p class=\"articleinfo\">%s - %s</p>
			</a>
		</div>", substr($i, 33, strlen($i)), explode("</h1>", explode("id=\"title\">", $files[$i], 2)[1], 2)[0], $p, date("F jS Y", strtotime(substr($i, 34, 11))));
	}
}
echo "</div>
</div>
</body>
</html>";
 ?>
