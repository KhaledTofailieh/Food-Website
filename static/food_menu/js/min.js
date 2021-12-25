var men = document.querySelector("#menu");
var navber = document.querySelector(".navber");
var scrollTop = document.querySelector("#scroll-top");

men.onclick = () => {
  men.classList.toggle("fa-times");
  navber.classList.toggle("active");
};

window.onscroll = () => {
  men.classList.remove("fa-times");
  navber.classList.remove("active");

  if (window.scrollY > 60) {
    scrollTop.classList.add("active");
  } else {
    scrollTop.classList.remove("active");
  }
};

function loader() {
  document.querySelector(".loader-container").classList.add("fade-out");
}
function fadeOut() {
  setInterval(loader, 3000);
}
window.onload = fadeOut();

function predicte(date) {
  var data = JSON.stringify({
    time: date
  });

  var xhr = new XMLHttpRequest();
  xhr.withCredentials = true;

  xhr.addEventListener("readystatechange", function() {
    if (this.readyState === 4) {
      console.log(this.responseText);
    }
  });

  xhr.open("GET", "http://127.0.0.1:8000/rank_time_restaurants");
  xhr.setRequestHeader("Content-Type", "application/json");
  /* xhr.setRequestHeader(
    "Cookie",
    "csrftoken=bJ2cvcsM15GQJmYJ0NTFPlhGULPnraXsEx0NEcaz3CuC6J26nKB39F9tYEmzCfBr"
  );
*/
  xhr.send(data);
}
