function onClick() {
	var i = document.getElementById('likes_id').value
	$.ajax({
		url: "/blog/ajax/likes",
		data:{'i':i},
		dataType: 'json',
		success: function(data) {
			document.getElementById('like').innerHTML = data.i
		}
	})
}
