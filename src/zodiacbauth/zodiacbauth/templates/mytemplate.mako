<h1>Projecte ${project}</h1>
<h2>Benvinguts a la pàgina inicial "/" root. HOME</h2>
<h3>Signes del Zodiac</h3>
% if logged_in:
 <h4> Usuari:  ${logged_in}</h4>
<p><a href="/logout">Clic aqui per logout.</a></p>
% endif


% for imatge in imatges:
	<img src="static/${imatge}" height="100" width="100">
% endfor
</br>
<p><a href="/elmeu">Fes clic aquí per provar sort amb el teu futur.</a></p>


