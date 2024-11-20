const preBtn = document.querySelector('.pre-btn');
const nxtBtn = document.querySelector('.nxt-btn');
const posts = document.querySelector('.posts');
const cardWidth = document.querySelector('.post--card').offsetWidth;

let currentScroll = 0;
preBtn.addEventListener('click', () => {
    currentScroll -= cardWidth * 3; //Evandro, caso você queira mudar a quantidade de cards que ele vai movimentar só mudar aqui
    if (currentScroll < 0) currentScroll = 0;
    posts.style.transform = `translateX(-${currentScroll}px)`;
});

nxtBtn.addEventListener('click', () => {
    const maxScroll = posts.scrollWidth - posts.offsetWidth;
    currentScroll += cardWidth * 3; //E aqui também
    if (currentScroll > maxScroll) currentScroll = maxScroll;
    posts.style.transform = `translateX(-${currentScroll}px)`;
});