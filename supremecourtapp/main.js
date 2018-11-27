


$('#filter').click(function() {
	//Reload the page to display the new data.
	//You could optionally work with Ajax

	window.location.href="/?title=" + $("#title").val() + "&topic=" + $("#topic").val() +
	"&name=" + $("#name").val()  +
	"&month=" + $("#month").val() + "&day=" + $("#day").val() + "&year=" + $("#year").val()
});

// $('#download-btn').click(function() {
// 	window.location.href="/speakers?format=csv&name=" + $("#speaker").val()
// });
