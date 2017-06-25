function f()
	{
		var t1 = document.getElementById('t1').value;
		var t2 = document.getElementById('t2').value;

        var s = "../summa2?t1=" + t1 + "@" + t2;
		console.log(s);



		var r = new XMLHttpRequest();
		r.open("GET",s);
		r.setRequestHeader("Content-Type","text/plain;charset=UTF-8");
		r.send(null);

		r.onreadystatechange = function()
		{
			if(r.readyState === 4 && r.status === 200)
			{
				var answer = r.responseText;

				var myJSON = JSON.parse(answer);
                var summaAns = (myJSON.summa);
                var statusAns = (myJSON.status);


				document.getElementById('result').innerHTML = summaAns + " ___ " + statusAns;
			}
		}

	}

function f_like(element) {

		var t2 = "p";//type = plus

		let myId = element.id;
		let mass = [];
		mass = myId.split("_");
		let number = parseInt(mass[1]);
		let resultId = "rating_" + number;

		var t1 = mass[1]; // id вопроса


		var s = "../qlike?t=" + t1 + "@" + t2;
		console.log(s);

		var r = new XMLHttpRequest();
		r.open("GET", s);
		r.setRequestHeader("Content-Type", "text/plain;charset=UTF-8");
		r.send(null);

		r.onreadystatechange = function () {
			if (r.readyState === 4 && r.status === 200) {
				var answer = r.responseText;

				var myJSON = JSON.parse(answer);
				var result = (myJSON.result);
				var status = (myJSON.status);

				if (status == "ok") document.getElementById(resultId).innerHTML = result;
				else alert("yoy have alredy liked or dont auth")
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


    var s = "../qlike?t=" + t1 + "@" + t2;
    console.log(s);

    var r = new XMLHttpRequest();
    r.open("GET", s);
    r.setRequestHeader("Content-Type", "text/plain;charset=UTF-8");
    r.send(null);

    r.onreadystatechange = function () {
        if (r.readyState === 4 && r.status === 200) {
            var answer = r.responseText;

            var myJSON = JSON.parse(answer);
            var result = (myJSON.result);
            var status = (myJSON.status);

            if (status == "ok") document.getElementById(resultId).innerHTML = result;
            else alert("yoy have alredy liked or dont auth")
        }
    }
}

