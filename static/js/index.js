const splash = document.querySelector('.splash');

document.addEventListener('DOMContenLoaded', (e)=>{
    setTimeout( ()=>{
        splash.classList.add('display-none');
    }, 2000);
})


$("#menu-toggle").click(function(e) {
    e.preventDefault();
    
    $("#wrapper").toggleClass("toggled");
  });