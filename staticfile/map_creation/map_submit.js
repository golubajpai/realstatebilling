const cordinates=['#value-point-a-x','#value-point-a-y','#value-point-b-x',
	'#value-point-b-y','#value-point-c-x','#value-point-c-y','#value-point-d-x','#value-point-d-y']


$( document ).ready(function() {
	


$( "#submit" ).click(function() {
	dict={}

	for(let i=0;i<cordinates.length;i++){

		if ($('#value-point-a-x').text()==""){
			dict={}
			alert('a-x required')
		}
		else{
			dict[cordinates[i]]=$(cordinates[i]).text()
			console.log(dict)


		}


	}


	$.ajax({
		'type':'POST',
		'url':window.location.href+'add_data',
		'data':dict,
		success: function(data){
     console.log(data);
	}
})

	console.log(dict)
});


})