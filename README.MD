1. Результатом виконання даного модуля є генерування карти, на якій знаходяться позначки, в місцях де були зняті фільми. Примітка: таких міток є десять 
і відображаються лише ті фільми, відстань від яких до певної точки є мінімальною. Також країни на карті зафарбовуються у певні кольори
(колір залежить від кількості населення держави).
Примітка: для нормальної роботи модуля потрібно в робочу директорію помістити два файли:world.json,locations.list.
2. На карті відображається 10 позначок(місця зйомки фільмів), які знаходяться найближче до початкової позиції(задає користувач). 
Таким чином користувач може дізнатися,які було знято фільми в певній місцевості, області. Також на карті додатково зафарбовоються у певні кольори країни, які мають якусь конкретну
кількість населення, а саме: кількості населення  меншій за 10000000 осіб відповідає оранжевий колір, більшій рівній за 10000000 осіб і водночас меншій за 20000000 осіб належить 
синій, а країнам,в яких проживає більше людей аніж 20000000 осіб відповідає зелений колір. Ці кольори(індикатори) слугують додатковим джерелом інформації для юзера
(дають додаткову інформацію про фільми)і можуть бути використані в подальших дослідженнях.
Примітка: кожна кордината рахується з пенвою незначною похибкою(0 <= mistake <= 1). Це було зроблено, аби уникнути співпадіння координат.

3.2014,(56.0, 24.02324).Рік і кординати мають бути числами.
![Знімок екрана (749)](https://user-images.githubusercontent.com/73779019/108106267-66fa0a00-7096-11eb-84ce-62b1b94075ab.png)
4. У згенерованому html файлі є досить багато тегів, а саме: `<style> </style>`(без посередньо відповідає за зовнішній вигляд карти), `<script> </script>`(описує скріпти файлу, 
містить url-посилання на програму/частину програми, записаної певною мовою), `<link>`(можна не закривати)`</link>`(відповідає за зв'язок з зовнішним файлом, який 
відповідає за дизайн(css file)),`<div> </div>`(виділяє певну частину тексу від загальної, щоб в майбутньому можна було легшо його змінити),
`<meta>`(можна не закривати)`</meta>`(відділяє частину інформації, яка повинна адресуватися браузеру.
Загальна структура:
 `<!DOCTYPE html>`
  `<head>` 
    `<meta/>`
      `<script> </scripts>`
    `<style> </style>`
    `<script> </scripts>`
    `<link/>`
      `<meta/>`
      `<style> </style>`
`</head>`
`<body>`
  `<div> </div>`
`</body>`
`<script>`
....
`</script>`
