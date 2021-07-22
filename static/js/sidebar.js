
let tamanioActual;

window.addEventListener("resize",window_option)

  function window_option(event){
    w3_close();
  }

  function w3_open() {

    console.log(document.body.clientWidth + ' wide by ' + document.body.clientHeight+' high');
    let width = document.body.clientWidth
    if( document.body.clientWidth > 1069){

        tamanioActual = "23%";
    }else if(document.body.clientWidth < 1069 && document.body.clientWidth > 450 ){
        tamanioActual = "40%";
    }else if(document.body.clientWidth < 450){
      tamanioActual = "100%";
    }
    
    document.getElementById("mySidebar").style.width = tamanioActual;
    document.getElementById("mySidebar").style.display = "block";
    document.getElementById("back").style.display = "block";
    document.getElementById("back").addEventListener("click", w3_close)
    
 
  }
  
  function w3_close() {
    document.getElementById("mySidebar").style.display = "none";
    document.getElementById("back").style.display = "none";
   
  }


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