// static/js/scripts.js
document.addEventListener('DOMContentLoaded', function () {
    // Плавное появление контента
    const content = document.querySelector('.content');
    if (content) {
        content.classList.add('fade-in');
    }

    // Подсветка активного пункта меню в сайдбаре
    const currentUrl = window.location.pathname;
    const navLinks = document.querySelectorAll('.sidebar .nav-link');

    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentUrl) {
            link.classList.add('active');
        }
    });

    // Плавная прокрутка для всех ссылок с хэшем
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Анимация при наведении на кнопки
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', () => {
            button.style.transform = 'scale(1.05)';
        });
        button.addEventListener('mouseleave', () => {
            button.style.transform = 'scale(1)';
        });
    });
});
