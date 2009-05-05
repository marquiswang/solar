// Solar Power Installation Planner Javascript file for making all the cool things work

$(document).ready(function(){
    
    // enable modal box on all elements with attr rel="facebox"
    $('a[rel*=facebox]').facebox(); 
    
	// LiveValidation code for client side error checking
	var id_peak_power_output = new LiveValidation('id_peak_power_output',{ validMessage: "✓", wait: 500 });
	id_peak_power_output.add( Validate.Numericality);
	id_peak_power_output.add( Validate.Presence, { failureMessage: "x" } );

	var id_installation_price = new LiveValidation('id_installation_price',{ validMessage: "✓", wait: 500 });
	id_installation_price.add( Validate.Numericality);
	id_installation_price.add( Validate.Presence, { failureMessage: "x" } );

    var id_city = new LiveValidation('id_city',{validMessage: "✓", wait: 500 });
    id_city.add( Validate.Presence, { failureMessage: "x" } );
	
    var id_state = new LiveValidation('id_state',{validMessage: "✓", wait: 500 });
	
	var id_zip_code = new LiveValidation('id_zip_code',{ validMessage: "✓", wait: 500 });
	id_zip_code.add( Validate.Numericality, { minimum: 0, maximum: 99999, failureMessage: "x"});
	id_zip_code.add( Validate.Length, { is: 5, failureMessage: "x"} );
	id_zip_code.add( Validate.Presence, { failureMessage: "x" } );
	
	var id_latitude = new LiveValidation('id_latitude',{ validMessage: "✓", wait: 500 });
	id_latitude.add( Validate.Numericality, { minimum: -90, maximum: 89, failureMessage: "x"});
	id_latitude.add( Validate.Presence, { failureMessage: "x" } );
	
	var id_longitude = new LiveValidation('id_longitude',{ validMessage: "✓", wait: 500 });
	id_longitude.add( Validate.Numericality, { minimum: -180, maximum: 180, failureMessage: "x"});
	id_longitude.add( Validate.Presence, { failureMessage: "x" } );

    // form tweaks
    function disable_unused_locations() {
        validation_lookup = {
            "#loc_choice_cs"  : [id_city, id_state], 
            "#loc_choice_zip" : [id_zip_code],
            "#loc_choice_ll"  : [id_latitude, id_longitude]
            }

    	for (var radio_button in validation_lookup) {
            for(j in validation_lookup[radio_button]) {
                if ($(radio_button).is(":checked") == true) 
                    validation_lookup[radio_button][j].enable();
                else 
                    validation_lookup[radio_button][j].disable();
            }
    	}
    }

	// Disable unused location configuration options
	disable_unused_locations()
	
	// Update when one is selected
	$('#loc_config').find(':radio').change(function(event){
		disable_unused_locations()
	});
		
	// Hide power bill input table if its not being used
	if ($("#costs_choice_spec").is(":checked") == false)
		$("#power_bill").hide()
	
	// Toggle on the input table if necessary
	$("#costs_choice_avg").change(function(event){
		$("#power_bill").slideUp("slow")
	});
	$("#costs_choice_spec").change(function(event){
		$("#power_bill").slideDown("slow")
	});	

	// on pageload, set these how we want them
	if ($("#advanced_control").is(":checked") == false)
	    $("#advanced").hide();

	// show/hide the advanced pane	
	$('#advanced_control').click(function() {
	    $('#advanced').toggle(50);
	    $("#advanced_control").toggleCheckboxes();
	    return false;
	});

	$('.help_button').tooltip({
		track: true,
		delay: 0, 
		showURL: false, 
		top: 0, 
		extraClass: "fixed_width" 
	});
	
});    
