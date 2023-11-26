const hamburger = document.querySelector('.header .navbar .wrapper .content');
const mobile_menu = document.querySelector('.header .navbar .wrapper ul');
const menu_item = document.querySelectorAll('.header .navbar .wrapper ul li a');
const header = document.querySelector('.header.brand');

hamburger.addEventListener('click', () => {
	hamburger.classList.toggle('active');
	mobile_menu.classList.toggle('active');
});

document.addEventListener('scroll', () => {
	var scroll_position = window.scrollY;
	if (scroll_position > 250) {
		header.style.backgroundColor = '#29323c';
	} else {
		header.style.backgroundColor = 'transparent';
	}
});

menu_item.forEach((item) => {
	item.addEventListener('click', () => {
		hamburger.classList.toggle('active');
		mobile_menu.classList.toggle('active');
	});
});