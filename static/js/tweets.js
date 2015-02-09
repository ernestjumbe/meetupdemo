var dragon = new VanillaDragon({onopen: onOpen, onchannelmessage: onChannelMessage});


function onChannelMessage(channels, message) {
	$('#tweets').append('<li class="list-group-item">'+ message.data.text + '</li>');
}

function onOpen(){
    dragon.subscribe('tweets', 'tweet', null, function(response) {
        console.log(response);
    }, function(response) {
        console.log("Failed to subscribe");
    })
}