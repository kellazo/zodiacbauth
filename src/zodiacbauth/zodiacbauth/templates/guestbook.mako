<h1>Benvinguts, al llibre de visites (guestbook) el projecte s'anomena: ${project}</h1>
<table width="100" border="5" align="center">

<tr>
  <td><strong>Data</strong></td>
  <td><strong>Signe</strong></td>
  <td><strong>Frase</strong></td>
</tr>
<tr>
  <td> <ul>
    % for dates in fortuna:
		<li>${dates.data_consulta}</li>
	% endfor
    </ul> </td>
    
  <td> <ul>
	% for signe in fortuna:
		<li>${signe.signe}</li>
	% endfor
</ul> </td>
  <td> <ul>
	% for frase in fortuna:
		<li>${frase.frase}</li>
	% endfor
</ul> </td>
</tr>
</table>
