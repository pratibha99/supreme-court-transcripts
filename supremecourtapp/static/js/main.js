/*
 * This is the Javascript file that makes requests to our controller.
 * We have prepared one API that makes requests in two unique ways
 * The filter option requests for data to be displayed and the download option
 * requests for data to be in a downloadable form
 */


$('#filter').click(function() {
	//Reload the page to display the new data.
	//You could optionally work with Ajax
	alert("HELLOOOOO")
	window.location.href="/?title=" + $("#title").val() + "&topic=" + $("#topic").val() +
	"&name=" + $("#name").val()  +
	"&month=" + $("#month").val() + "&day=" + $("#day").val() + "&year=" + $("#year").val()
});

// $('#download-btn').click(function() {
// 	window.location.href="/speakers?format=csv&name=" + $("#speaker").val()
// });
