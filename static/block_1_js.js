'use strict' // Установка JS на строгий режим написания кода;

let count_customers = 0; // количество мест;

// fetch-"GET" запрос списка постоялцев;
function get_costomers_f() {
    let xhr = new XMLHttpRequest(); // XMLHttp метод для ajax "GET" запроса;
    xhr.open('GET', '/get_costomers', true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let data = JSON.parse(xhr.responseText); // Cписок имен в JSON формате;
            // Здесь может быть функция;
            console.log(data);
            count_customers = data.length;
            for (let i=1; i<count_customers + 1; i++) {
                document.getElementById(`date_${i}_id`).value = data[i-1][1];
                document.getElementById(`time_${i}_id`).value = data[i-1][2];
                document.getElementById(`text_${i}_id`).value = data[i-1][3];
            }
        }
    }
    xhr.send();
};
get_costomers_f();

// Сохранение пользователя;
document.addEventListener('click', (e)=>{
    for (let i=1; i<count_customers + 1; i++) {
        if (e.target.id == `save_${i}_id` || e.target.id == `save_text_${i}_id`) {
            let data = [i];
            data.push(document.getElementById(`date_${i}_id`).value);
            data.push(document.getElementById(`time_${i}_id`).value);
            data.push(document.getElementById(`text_${i}_id`).value);
            console.log(data);
            post_save_f(data)
        }
    }
});

// Функция удаления данных;
document.addEventListener('click', (e)=>{
    for (let i=1; i<count_customers + 1; i++) {
        if (e.target.id == `delete_${i}_id` || e.target.id == `delete_text_${i}_id`) {
            let data = [i];
            data.push('');
            data.push('');
            data.push('');
            console.log(data);
            post_save_f(data)
        }
    }
});

// Функция сохранения в базе данных;
function post_save_f(data) {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', `post_save`, true); 
    xhr.setRequestHeader('Content-type', "application/x-www-form-urlencoded");
    xhr.send(JSON.stringify({ "save_obj": data }));
    setTimeout(()=>{get_costomers_f()}, 500);
};