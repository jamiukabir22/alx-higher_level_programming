$(function() {
	var character = $('character');
	

	//Script that fetches cahracter name from url://swapi-api.hbtn.io/api/people/5/?format=json
	
	$.ajax({
		type: 'GET',
		url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
		success: function(name) {
			$(character).append(name.name);
		}
	})
})
