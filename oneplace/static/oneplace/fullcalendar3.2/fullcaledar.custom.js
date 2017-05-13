$(document).ready(function() {
		$('#calendar').fullCalendar({
			
			header: {
				left: 'prev,next today',
				center: 'title',
				right: 'month,basicWeek,basicDay,listMonth'
			},

			defaultDate: '{{ now }}',
			navLinks: true, // can click day/week names to navigate views
			editable: true,
			eventLimit: true, // allow "more" link when too many events
			events: [
			{% for calvalue in calendarInfo %}
				{
					title: '{{ calvalue.title }}',
					start: '{{ calvalue.start }}',
					end:   '{{ calvalue.end }}'
				},
			{% endfor %}
			]
		});
		
	});
