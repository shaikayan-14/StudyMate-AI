let time = 25 * 60;

let timer = null;



function setTime(){

    let minutes = document.getElementById("minutes").value;


    if(minutes > 0){

        time = minutes * 60;

        updateTimer();

    }

}




function updateTimer(){

    let minutes = Math.floor(time / 60);

    let seconds = time % 60;


    document.getElementById("timer").innerHTML =

    `${minutes}:${seconds < 10 ? "0" : ""}${seconds}`;

}




function startTimer(){

    if(timer !== null)

        return;



    timer = setInterval(()=>{


        if(time > 0){

            time--;

            updateTimer();

        }


        else{


            clearInterval(timer);

            timer = null;


            alert("🎉 Focus session completed!");

        }



    },1000);


}




function pauseTimer(){

    clearInterval(timer);

    timer = null;

}




function resetTimer(){

    clearInterval(timer);

    timer = null;


    setTime();

}




setTime();