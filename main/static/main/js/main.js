ymaps.ready(function () {
    var myMap = new ymaps.Map('map', {
            center: [47.233815, 39.758482],
            zoom: 16
        }),

        myPlacemark = new ymaps.Placemark(myMap.getCenter(), {
            hintContent: 'СТРОЙИНДУСТРИЯ',
            balloonContent: 'СТРОЙИНДУСТРИЯ'
        }, {
            iconLayout: 'default#image',
            iconImageHref: 'img/logo.png',
            iconImageSize: [60, 48],
            iconImageOffset: [-15, -15]
        })

    myMap.geoObjects.add(myPlacemark);
});