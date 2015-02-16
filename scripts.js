function point_it(event){
	pos_x = event.offsetX?(event.offsetX):event.pageX-document.getElementById("pointer_div").offsetLeft;
	pos_y = event.offsetY?(event.offsetY):event.pageY-document.getElementById("pointer_div").offsetTop;
	document.getElementById("cross").style.left = (pos_x-1) ;
	document.getElementById("cross").style.top = (pos_y-15) ;
	document.getElementById("cross").style.visibility = "visible" ;
	//document.pointform.form_x.value = pos_x;
	//document.pointform.form_y.value = pos_y;
	var milliseconds = (new Date).getTime();
	window.location.href = "http://[IP]:[PORT]/index.html?mouse_x="+pos_x+"&mouse_y="+pos_y+ "&epoch="+milliseconds;
}

function myKeyPress(e){
			var writeroot = document.getElementById('writeroot');
            var keynum;

            if(window.event){ // IE
            	keynum = e.keyCode;
            }else
                if(e.which){ // Netscape/Firefox/Opera
            		keynum = e.which;
                 }
            //alert(String.fromCharCode(keynum));
			//writeroot.innerHTML += String.fromCharCode(keynum);
			var data = 'key='+ String.fromCharCode(keynum) + "&epoch="+milliseconds ; // this where i add multiple data using  ' & '
            var milliseconds = (new Date).getTime();
		  $.ajax({
		    type:"GET",
		    cache:false,
		    url:"http://[IP]:[PORT]/",
		    data:data,    // multiple data sent using ajax
		    success: function (html) {

		      //$('#add').val('data sent sent');
		      //$('#msg').html(html);
              //alert(String.fromCharCode(keynum));
		    }
		  });
		  return false;
        }