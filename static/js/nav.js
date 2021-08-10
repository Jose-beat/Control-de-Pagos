
window.addEventListener("resize",dropUser)
document.getElementById("btnUsr").style.display = "none";

function dropUser(event) {

  console.log(document.body.clientWidth + ' wide by ' + document.body.clientHeight+' high');
  //625
  if( document.body.clientWidth >= 625){

    let dropWI = document.getElementById("imgUser")
    let sidWI = document.getElementById("imgSidebarUser")
    document.getElementById("dropUser").style.display = "block";
    document.getElementById("btnUsr").style.display = "none";
    
    if( dropWI !== null &&  sidWI !==null){
      document.getElementById("imgUser").style.display = "inline-block";
      document.getElementById("imgSidebarUser").style.display = "none";
    }else{

    }
    
    

  }else if(document.body.clientWidth < 625){

    let dropWI = document.getElementById("imgUser")
    let sidWI = document.getElementById("imgSidebarUser")
    if(dropWI !== null && sidWI !== null){
      document.getElementById("imgUser").style.display = "none";
      document.getElementById("imgSidebarUser").style.display = "block";
    }
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
