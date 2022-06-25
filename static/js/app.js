
const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.nav-menu');

menu.addEventListener('click', function(){
  menu.classList.toggle('is-active')
  menuLinks.classList.toggle('active')
    }

)


const app_clocks = document.getElementsByClassName("clock");

function updateClocks() {
  for (let clock of app_clocks) {
    let timezone = clock.dataset.timezone;
    let time = new Date().toLocaleTimeString("en-US", {
      hour: '2-digit',
      minute:'2-digit',
      second:'2-digit',
      timeZone: timezone
    });
    clock.textContent = time;
  }
}

