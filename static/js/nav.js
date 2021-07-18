
window.addEventListener("resize",dropUser)
document.getElementById("btnUsr").style.display = "none";

function dropUser(event) {

  console.log(document.body.clientWidth + ' wide by ' + document.body.clientHeight+' high');
  //625
  if( document.body.clientWidth >= 625){

    document.getElementById("dropUser").style.display = "block";
    document.getElementById("btnUsr").style.display = "none";

  }else if(document.body.clientWidth < 625){

    document.getElementById("dropUser").style.display = "none";
    document.getElementById("btnUsr").style.display = "block";
      
  }
  

}

dropUser()

//document.getElementById("ddu").addEventListener(onclick, dropDownUser)
  function dropDownUser() {
    var x = document.getElementById("listAction");
    console.log(x.className.indexOf("w3-show") == -1)
    if (x.className.indexOf("w3-show") == -1) { 
        
        x.className += " w3-show";

    } else {
      x.className = x.className.replace(" w3-show", "");
    }
  }
