var dragon = new VanillaDragon({onopen: onOpen, onchannelmessage: onChannelMessage});


function onChannelMessage(channels, message) {
	$('#polls').append('<a href="'+message.data.id+'" class="list-group-item">'+ message.data.question_text + '</a>');
}


function onOpen(){
    dragon.subscribe('questions-list', 'question', null, function(response) {
        //console.log(response);
    }, function(response) {
        console.log("Failed to subscribe");
    });

    dragon.getList('questions-list', {}, function(context, data){
    	console.log(data)
    	for (i in data){
    		$('#polls').append('<a href="/polls/'+data[i].id+'" class="list-group-item">'+ data[i].question_text + '</a>');
    	}
    }, function(respone){
    	console.log("Could not get");
    });
}