var csrfcookie = function() {
    var cookieValue = null,
        name = 'csrftoken';
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};
//  POST with csrftoken  //
function f_like(element) {

    var t2 = "p";//type = plus

    let myId = element.id;
    let mass = [];
    mass = myId.split("_");
    let number = parseInt(mass[1]);
    let resultId = "rating_" + number;

    var t1 = mass[1]; // id вопроса


    // var urlString = "../qlike/"; //url запроса
    if (mass[0] === "like") {
        var urlString = "../qlike/"; //url запроса
        console.log(urlString);
    }
    else if (mass[0] === "alike")
    {
        var urlString = "../../qlike/"; //url запроса
        console.log(urlString);
    }


    var s = "t=" + t1 + "@" + t2; //данные запроса, посылаемые в теле запроса
	console.log(s);

    var r = new XMLHttpRequest();
    r.open("POST", urlString);
    // r.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
	r.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
	r.setRequestHeader('X-CSRFToken', csrfcookie());
	// r.onload = callback;
    r.send(s);

    r.onreadystatechange = function () {
        if (r.readyState === 4 && r.status === 200) {
            var answer = r.responseText;

            var myJSON = JSON.parse(answer);
            var result = (myJSON.result);
            var status = (myJSON.status);

            if (status == "ok") document.getElementById(resultId).innerHTML = result;
            else alert("yoy have alredy liked")
        }
    }
}
function f_dislike(element) {

    var t2 = "m";//type = plus

    let myId = element.id;
    let mass = [];
    mass = myId.split("_");
    let number = parseInt(mass[1]);
    let resultId = "rating_" + number;

    var t1 = mass[1]; // id вопроса


    // var urlString = "../qlike/"; //url запроса
    // console.log(urlString);

    if (mass[0] === "dislike") {
        var urlString = "../qlike/"; //url запроса
        console.log(urlString);
    }
    else if (mass[0] === "adislike")
    {
        var urlString = "../../qlike/"; //url запроса
        console.log(urlString);
    }

    var s = "t=" + t1 + "@" + t2; //данные запроса, посылаемые в теле запроса
	console.log(s);

    var r = new XMLHttpRequest();
    r.open("POST", urlString);
    // r.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
	r.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
	r.setRequestHeader('X-CSRFToken', csrfcookie());
	// r.onload = callback;
    r.send(s);

    // var request = new XMLHttpRequest();
	// request.open('POST', url, true);
	// request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
	// request.setRequestHeader('X-CSRFToken', csrfcookie());
	// request.onload = callback;
	// request.send(data);

    r.onreadystatechange = function () {
        if (r.readyState === 4 && r.status === 200) {
            var answer = r.responseText;

            var myJSON = JSON.parse(answer);
            var result = (myJSON.result);
            var status = (myJSON.status);

            if (status == "ok") document.getElementById(resultId).innerHTML = result;
            else alert("yoy have alredy liked")
        }
    }
}

//  POST with csrftoken  //
function a_like(element) {

    var t2 = "p";//type = plus

    let myId = element.id;
    let mass = [];
    mass = myId.split("_");
    let number = parseInt(mass[1]);
    let resultId = "rating_" + number;

    var t1 = mass[1]; // id вопроса


    var urlString = "../../alike/"; //url запроса
    console.log(urlString);


    var s = "t=" + t1 + "@" + t2; //данные запроса, посылаемые в теле запроса
	console.log(s);

    var r = new XMLHttpRequest();
    r.open("POST", urlString);
	r.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
	r.setRequestHeader('X-CSRFToken', csrfcookie());
	// r.onload = callback;
    r.send(s);

    r.onreadystatechange = function () {
        if (r.readyState === 4 && r.status === 200) {
            var answer = r.responseText;

            var myJSON = JSON.parse(answer);
            var result = (myJSON.result);
            var status = (myJSON.status);

            if (status == "ok") document.getElementById(resultId).innerHTML = result;
            else alert("yoy have alredy liked")
        }
    }
}
function a_dislike(element) {

    var t2 = "m";//type = plus

    let myId = element.id;
    let mass = [];
    mass = myId.split("_");
    let number = parseInt(mass[1]);
    let resultId = "rating_" + number;

    var t1 = mass[1]; // id вопроса


    var urlString = "../../alike/"; //url запроса
    console.log(urlString);


    var s = "t=" + t1 + "@" + t2; //данные запроса, посылаемые в теле запроса
	console.log(s);

    var r = new XMLHttpRequest();
    r.open("POST", urlString);
	r.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
	r.setRequestHeader('X-CSRFToken', csrfcookie());
	// r.onload = callback;
    r.send(s);

    r.onreadystatechange = function () {
        if (r.readyState === 4 && r.status === 200) {
            var answer = r.responseText;

            var myJSON = JSON.parse(answer);
            var result = (myJSON.result);
            var status = (myJSON.status);

            if (status == "ok") document.getElementById(resultId).innerHTML = result;
            else alert("yoy have alredy liked")
        }
    }
}

function a_correct(element) {

    let myId = element.id;
    let mass = [];
    mass = myId.split("_");
    let number = parseInt(mass[1]);

    var ansId = mass[1]; // id вопроса


    var urlString = "../../acorrect/"; //url запроса
    console.log(urlString);


    var s = "id=" + ansId; //данные запроса, посылаемые в теле запроса
	console.log(s);

    var r = new XMLHttpRequest();
    r.open("POST", urlString);
	r.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
	r.setRequestHeader('X-CSRFToken', csrfcookie());
	// r.onload = callback;
    r.send(s);

    r.onreadystatechange = function () {
        if (r.readyState === 4 && r.status === 200) {
            var answer = r.responseText;

            var myJSON = JSON.parse(answer);
            var result = (myJSON.result);
            var status = (myJSON.status);

            if (status == "ok") document.getElementById(myId).checked = result;
        }
    }
}



// GET
// function f()
// 	{
// 		var t1 = document.getElementById('t1').value;
// 		var t2 = document.getElementById('t2').value;
//
//         var s = "../summa2?t1=" + t1 + "@" + t2;
// 		console.log(s);
//
//
//
// 		var r = new XMLHttpRequest();
// 		r.open("GET",s);
// 		r.setRequestHeader("Content-Type","text/plain;charset=UTF-8");
// 		r.send(null);
//
// 		r.onreadystatechange = function()
// 		{
// 			if(r.readyState === 4 && r.status === 200)
// 			{
// 				var answer = r.responseText;
//
// 				var myJSON = JSON.parse(answer);
//                 var summaAns = (myJSON.summa);
//                 var statusAns = (myJSON.status);
//
//
// 				document.getElementById('result').innerHTML = summaAns + " ___ " + statusAns;
// 			}
// 		}
//
// 	}
// function f_like(element) {
//
// 		var t2 = "p";//type = plus
//
// 		let myId = element.id;
// 		let mass = [];
// 		mass = myId.split("_");
// 		let number = parseInt(mass[1]);
// 		let resultId = "rating_" + number;
//
// 		var t1 = mass[1]; // id вопроса
//
//
// 		var s = "../qlike?t=" + t1 + "@" + t2;
// 		console.log(s);
//
// 		var r = new XMLHttpRequest();
// 		r.open("GET", s);
// 		r.setRequestHeader("Content-Type", "text/plain;charset=UTF-8");
// 		r.send(null);
//
// 		r.onreadystatechange = function () {
// 			if (r.readyState === 4 && r.status === 200) {
// 				var answer = r.responseText;
//
// 				var myJSON = JSON.parse(answer);
// 				var result = (myJSON.result);
// 				var status = (myJSON.status);
//
// 				if (status == "ok") document.getElementById(resultId).innerHTML = result;
// 				else alert("yoy have alredy liked or dont auth")
// 			}
// 		}
// 	}
//
// function f_dislike(element) {
//
//     var t2 = "m";//type = plus
//
//     let myId = element.id;
//     let mass = [];
//     mass = myId.split("_");
//     let number = parseInt(mass[1]);
//     let resultId = "rating_" + number;
//
//     var t1 = mass[1]; // id вопроса
//
//
//     var s = "../qlike?t=" + t1 + "@" + t2;
//     console.log(s);
//
//     var r = new XMLHttpRequest();
//     r.open("GET", s);
//     r.setRequestHeader("Content-Type", "text/plain;charset=UTF-8");
//     r.send(null);
//
//     r.onreadystatechange = function () {
//         if (r.readyState === 4 && r.status === 200) {
//             var answer = r.responseText;
//
//             var myJSON = JSON.parse(answer);
//             var result = (myJSON.result);
//             var status = (myJSON.status);
//
//             if (status == "ok") document.getElementById(resultId).innerHTML = result;
//             else alert("yoy have alredy liked or dont auth")
//         }
//     }
// }