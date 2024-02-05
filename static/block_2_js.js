'use strict' // Установка JS на строгий режим написания кода;

// fetch-"GET" запрос рекламы;
function get_costomers_bot_f() {
    let xhr = new XMLHttpRequest(); // XMLHttp метод для ajax "GET" запроса;
    xhr.open('GET', '/get_costomers_bot', true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let data = JSON.parse(xhr.responseText); // Cписок имен в JSON формате;
            // Здесь может быть функция;
            console.log(data);
            document.getElementById('textarea_id').value = data;
        }
    }
    xhr.send();
};
get_costomers_bot_f();

// Функция сохранения в базе данных рекламы;
document.getElementById('button_save_advert_id').addEventListener('click', ()=>{
    let data = document.getElementById('textarea_id').value;
    console.log(data);
    post_save_bot_f(data);
})
function post_save_bot_f(data) {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', `/post_save_bot`, true); 
    xhr.setRequestHeader('Content-type', "application/x-www-form-urlencoded");
    xhr.send(JSON.stringify({ "save_obj": data }));
    setTimeout(()=>{get_costomers_bot_f()}, 500);
};

// fetch-"GET" запрос для запуска бота;
document.getElementById('button_start_advert_id').onclick = () => {get_bot_start_f()};
function get_bot_start_f() {
    let xhr = new XMLHttpRequest(); // XMLHttp метод для ajax "GET" запроса;
    xhr.open('GET', '/get_bot_start', true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let data = JSON.parse(xhr.responseText); // Cписок имен в JSON формате;
            // Здесь может быть функция;
            console.log('Бот запущен');
        }
    }
    xhr.send();
};