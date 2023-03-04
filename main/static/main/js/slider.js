var mySwiper = new Swiper ('.swiper-container', {
    slidesPerView:1,
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
    },
    effect:'fade',
    loop:true,
  })

  var mySwiper = new Swiper ('.swiper-container1', {
    slidesPerView:1,
    autoplay: {
      delay: 5000,
    },
    speed: 2000,
    effect:'fade',
    loop:true,
  })