<h1>Benvinguts, el projecte s'anomena: ${project}</h1>
% if logged_in:
<h2>Hola usuari: ${logged_in}. T'has registrat correctament.</h2>
% endif
<p>Entra les dades que et demanen i et mostraré el teu signe del zodíac, haviam que t'espera.</p>
<p>Data de naixement:</p>
<form method="post">
	Dia:<input type="text" name="dia" size="2" maxlength="2"/><br>
	Mes:<select name="mes">
        <option value="0">Gener</option>
        <option value="1">Febrer</option>
        <option value="2">Març</option>
        <option value="3">Abril</option>
        <option value="4">Maig</option>
        <option value="5">Juny</option>
        <option value="6">Juliol</option>
        <option value="7">Agost</option>
        <option value="8">Setembre</option>
        <option value="9">Octubre</option>
        <option value="10">Novembre</option>
        <option value="11">Desembre</option>
        </select><br>
    Any:<input type="text" name="any" size="4" maxlength="4"/><br>
    <br>
    Entra el teu nom:<br>
    <br>
    Nom:<input type="text" name="nom" size="15" maxlength="15"/><br>
    <br>
	<input type="submit" value="Enviar">
</form>

% if frase:
    <p> Hola ${nom}, vas nèixer el ${dia} de ${lletres_mes} del ${ano} </p>
    <p>${dia} - ${num_mes} - ${ano}</p>
    <p>signe:   ${signe} </p>
    <img src="static/${imatge_signe}" height="100" width="100">
    <p>Frase de la sort: ${frase}</p>
    
% endif

<a href="/">Anar a la Home Page</a>
