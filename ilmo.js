var lineLimit = 28;
var focus;
//form values
var name;
var background;
var allergies;
var email;


    var ctrlDown = false;
    var ctrlKey = 17, cKey = 67;

    $(document).keydown(function(e)
    {
        if (e.keyCode == ctrlKey) ctrlDown = true;
    }).keyup(function(e){
        if (e.keyCode == ctrlKey) ctrlDown = false;
    });

    $(document).keydown(function(e)
    {
        if (ctrlDown && e.keyCode == cKey){
        	addLine("> "+$('#input').find('input').val());
        	$('#input').cssConsole('reset');	
			execCommand = mainMenu.main;
        } 
    });

$('#input').cssConsole({
	inputName:'console',
	charLimit: 500,
	onEnter: function(){
		addLine("> "+$('#input').find('input').val());
		if ( !$('#input').find('input').val()) {
		return;
		}
		execCommand($('#input').find('input').val());
		$('#input').cssConsole('reset');	
	}
});

focus = window.setInterval(function() {
	if(!$('#input').find('input').is(":focus")){
		$('#input').find('input').focus();
	}
}, 100);

function addLine(input, style, color) {
		if($('.console div').length==lineLimit) {
			$('.console div').eq(0).remove();
		}
		var escapedInput = $('<div/>').text(input).html();
		style = typeof style !== 'undefined' ? style : 'line';
		color = typeof color !== 'undefined' ? color : 'white';

		$('.console').append('<div class="'+style+' '+color+'">'+escapedInput+'</div>');
}


var readBackground = {
    ask: function () {
       addLine("Kerro lyhyesti taustoista, esim opiskelu/työhistoria, harrasteprojektit jne.");
       execCommand = readBackground.check;
    },
    check: function (backgroundInput) {
        background = backgroundInput;
        readEmail.ask();
    }
};

var readEmail = {
    ask: function () {
        addLine("Anna sähköpostiosoitteesi, huom. käytämme tätä osoitetta vain tämän tapahtuman tarpeisiin!");
        execCommand = readEmail.check;
    },
    check: function (emailInput) {
        if (emailInput.indexOf("@") != -1) {
        email = emailInput;
        readAllergies.ask();
 	   } else {
    	addLine("Antamasi osoite ei ollut validi!");
  	   }
    }
};

var readAllergies = {
    ask: function () {
        addLine("Mikäli sinulla on allergioita/muita erityisruokavalioita niin kerro ne tässä");
        execCommand = readAllergies.check;
    },
    check: function (allergiesInput) {
        allergies = allergiesInput;
        confirmation.ask();
    }
};

var confirmation = {
    ask: function () {
        addLine("Annoit seuraavat tiedot:")
		addLine("Nimi: '" + name + "'", 'margin');
		addLine("Tausta: '" + background + "'", 'margin');
		addLine("Email '" + email + "'", 'margin');
		addLine("Allergiat: '" + allergies + "'", 'margin');
		addLine("Haluatko lähettää tiedot ? K[ylla]/E[i]");
        execCommand = confirmation.check;
    },
    check: function (confirmationInput) {
         if (confirmationInput.indexOf("K") != -1  || confirmationInput.indexOf("k") != -1)
		    {
		    	addLine("Tiedot lähetetty!");
		    	//send spam
		    } else {
		    	addLine("Tietoja ei lähetetty");
		    } 
		  execCommand = mainMenu.main;
    }
};



var mainMenu = {
   main: function(mainMenuInput){
  
	var command = mainMenuInput.split(" ")[ 0 ];
	if (mainMenuInput.split(" ").length > 2 ) {
	var parameter = mainMenuInput.substr(mainMenuInput.indexOf(" ") + 1);
	}
	else {
		var parameter =  mainMenuInput.split(" ")[ 1 ];
	}
    if ( commands[command] ) {
      return commands[command](parameter);
    } else {
      addLine("Command '" + command + "' was not found.");
    }  
    } 
};

var execCommand = mainMenu.main;

var commands = {
	help: function (){
		addLine("Järjestelmä tunnistaa seuraavat komennot:");
		addLine("adduser &ltetunimi&gt &ltsukunimi&gt ", 'margin');
		addLine("man adduser", 'margin');
		addLine("man solita", 'margin');
		addLine("help", 'margin');
	},
	man: function (parameter){

	if ( !parameter) {
		addLine("What manual page do you want?");
	}	else {
    if (parameter.indexOf("adduser") != -1) { 
		addLine("Komento adduser ottaa parametrit <etunimi> <sukunimi>");
	} else if (parameter.indexOf("solita") != -1) {
		//TODO: lisää kontentti
		addLine("Lisää juttua Solitasta");
	} else {
		addLine("No manual entry for '" + command + "'");
	}
	}
	},
	adduser: function(parameter){
		if ( parameter) {
		addLine("Adding user '" + parameter + "'");
		name = parameter;
		readBackground.ask();
		//label.style.display ="hidden";
		} else {
			addLine("Komento adduser ottaa parametrit <etunimi> <sukunimi>");
		}
	}
}