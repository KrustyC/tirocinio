function showAlert (text) {
	var alert=$("<div class=\'alert\' role=\'alert\'' style=\'display: none;\'>"+text+"</div>");
	$('body').append(alert);
	alert.fadeIn();
	setTimeout(function(){
	alert.fadeOut(400, function() { alert.remove(); });
	}, 2500);
}


function showAlertBad (text) {
	var alert=$("<div class=\'alertBad\' role=\'alert\'' style=\'display: none;\'>"+text+"</div>");
	$('body').append(alert);
	alert.fadeIn();
	setTimeout(function(){
	alert.fadeOut(400, function() { alert.remove(); });
	}, 2500);
}
