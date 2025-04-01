toggle = document.getElementById('toggle_header');
header = document.querySelector('header');

toggle.addEventListener('click', () => {
  header.classList.toggle('red');
  header.classList.toggle('green');
  console.log(header);
});
