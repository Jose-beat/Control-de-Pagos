
let tamanioActual;

window.addEventListener("resize",w3_open)


  function w3_open(event) {

    console.log(document.body.clientWidth + ' wide by ' + document.body.clientHeight+' high');
    
    if( document.body.clientWidth > 1069){

        tamanioActual = "23%";
    }else if(document.body.clientWidth < 1069){
        tamanioActual = "50%";
    }
    document.getElementById("mySidebar").style.width = tamanioActual;
    document.getElementById("mySidebar").style.display = "block";
 
  }
  
  function w3_close() {
    document.getElementById("mySidebar").style.display = "none";
  }

  /*
    function w3_open() {
        
        let menu = document.getElementById("openNav");
        document.getElementById("main").style.marginLeft = "23%";
        document.getElementById("mySidebar").style.width = "23%";
        document.getElementById("mySidebar").style.display = "block";
        document.getElementById("openNav").style.display = 'inline-block';
        
        menu.innerHTML="&#10510;"
        menu.onclick=w3_close;
        
    }

    
    function w3_close() {
        var menu = document.getElementById("openNav");
        document.getElementById("main").style.marginLeft = "0%";
        document.getElementById("mySidebar").style.display = "none";
        document.getElementById("openNav").style.display = "inline-block";

        menu.innerHTML="&#9776;"
        menu.onclick=w3_open;
        console.log(menu)
    }
*/
    function myAccFunc() {
        var x = document.getElementById("demoAcc");
        if (x.className.indexOf("w3-show") == -1) {
          x.className += " w3-show";
          x.previousElementSibling.className += " w3-green";
        } else { 
          x.className = x.className.replace(" w3-show", "");
          x.previousElementSibling.className = 
          x.previousElementSibling.className.replace(" w3-green", "");
        }
      }
      function myAccFunc1() {
        var x = document.getElementById("demoAcc1");
        if (x.className.indexOf("w3-show") == -1) {
          x.className += " w3-show";
          x.previousElementSibling.className += " w3-green";
        } else { 
          x.className = x.className.replace(" w3-show", "");
          x.previousElementSibling.className = 
          x.previousElementSibling.className.replace(" w3-green", "");
        }
      }
      function myAccFunc2() {
        var x = document.getElementById("demoAcc2");
        if (x.className.indexOf("w3-show") == -1) {
          x.className += " w3-show";
          x.previousElementSibling.className += " w3-green";
        } else { 
          x.className = x.className.replace(" w3-show", "");
          x.previousElementSibling.className = 
          x.previousElementSibling.className.replace(" w3-green", "");
        }
      }

      function myAccFunc3() {
        var x = document.getElementById("demoAcc3");
        if (x.className.indexOf("w3-show") == -1) {
          x.className += " w3-show";
          x.previousElementSibling.className += " w3-green";
        } else { 
          x.className = x.className.replace(" w3-show", "");
          x.previousElementSibling.className = 
          x.previousElementSibling.className.replace(" w3-green", "");
        }
      }
      function myAccFunc4() {
        var x = document.getElementById("demoAcc4");
        if (x.className.indexOf("w3-show") == -1) {
          x.className += " w3-show";
          x.previousElementSibling.className += " w3-green";
        } else { 
          x.className = x.className.replace(" w3-show", "");
          x.previousElementSibling.className = 
          x.previousElementSibling.className.replace(" w3-green", "");
        }
      }
      function myAccFunc5() {
        var x = document.getElementById("demoAcc5");
        if (x.className.indexOf("w3-show") == -1) {
          x.className += " w3-show";
          x.previousElementSibling.className += " w3-green";
        } else { 
          x.className = x.className.replace(" w3-show", "");
          x.previousElementSibling.className = 
          x.previousElementSibling.className.replace(" w3-green", "");
        }
      }