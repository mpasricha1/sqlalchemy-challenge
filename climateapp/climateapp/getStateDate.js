window.onload = function() {
	var a = document.getElementById("starDate");

	a.onclick = function() { 
		(function() {
    		$('#hiddenDate').datepicker({
        		changeYear: 'true',
        		changeMonth: 'true',
        		startDate: '07/16/1989',
        		firstDay: 1
    });
    $('#pickDate').click(function (e) {
        $('#hiddenDate').datepicker("show");
        e.preventDefault();
    });
});
	}
}