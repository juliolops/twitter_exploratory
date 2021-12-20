
buttonRun = document.querySelector(".buttonRun")

buttonStop = document.querySelector(".buttonStop")

if(document.querySelector(".status-system").innerText == "Running") {

  document.querySelector(".status-system").style.color = "#008000"

  } else {


    document.querySelector(".status-system").style.color = "#800900"

  }


if(document.querySelector(".status-system").innerText != "Not starting") {

    //document.querySelector(".status-system").style.color = "#008000"

    //document.getElementById("myBtn").disabled = true

    document.querySelector(".contentTwitter").disabled = true;

    document.querySelector(".contentTwitter").style.backgroundColor='gray';

    document.querySelector(".contentTwitter").style.color='white';




    document.querySelector(".StopWords").disabled = true;

    document.querySelector(".StopWords").style.backgroundColor='gray';

    document.querySelector(".StopWords").style.color='white';




  
    }



buttonStop.addEventListener("click", function() {


  document.querySelector(".status-system").innerText = "Stopped"

  document.querySelector(".status-system").style.color = "#800900"

  console.log("carregou!")
  
  //contentTwitter = document.querySelector(".contentTwitter").value;
  
 
  let data = new FormData();
  
  //data.append("contentTwitter", contentTwitter);

  data.append("status_sytem", "Stopped");
  
  data.append("query", contentTwitter);
  
  console.log("clicou aqui!")
    
  const Http = new XMLHttpRequest();
  
  const url='http://127.0.0.1:8000/persist_results';
  
  
  
  Http.open("POST", url,true);
  
  Http.send(data);
  
  Http.onreadystatechange = (e) => {
  console.log(Http.responseText);
  location.reload(true);
  
  }


})


buttonRun.addEventListener("click", function() {

    document.querySelector(".status-system").innerText = "Running";

    document.querySelector(".status-system").style.color = "#008000";



    document.querySelector(".contentTwitter").disabled = true;

    document.querySelector(".contentTwitter").style.backgroundColor='gray';

    document.querySelector(".contentTwitter").style.color='white';




    document.querySelector(".StopWords").disabled = true;

    document.querySelector(".StopWords").style.backgroundColor='gray';

    document.querySelector(".StopWords").style.color='white';




    console.log("carregou!")
    
    contentTwitter = document.querySelector(".contentTwitter").value;
    
    console.log(contentTwitter)
    
   
    let data = new FormData();
    
    //data.append("contentTwitter", contentTwitter);

    data.append("status_sytem", "Running");

    data.append("query", contentTwitter);
    
    
    
    console.log("clicou aqui!")
      
    const Http = new XMLHttpRequest();
    
    const url='http://127.0.0.1:8000/persist_results';
    
    
    
    Http.open("POST", url,true);
    
    Http.send(data);
    
    Http.onreadystatechange = (e) => {
    console.log(Http.responseText);
    location.reload(true);
    
    }
    
    }
    
    
    // this is inside your loop
)





interval = setInterval(function () {
  
  
  if(document.querySelector(".status-system").innerText == "Running") {
  
    
    console.log("carregou!")
    
    contentTwitter = document.querySelector(".contentTwitter").value;
    
    console.log(contentTwitter)
    
    dados = {data:contentTwitter};
    
    let data = new FormData();
    
    data.append("query", contentTwitter);

    data.append("status_sytem", "Running");
    
    
    
    console.log("clicou aqui!")
      
    const Http = new XMLHttpRequest();
    
    const url='http://127.0.0.1:8000/persist_results';
    
    
    data.append("query", contentTwitter);
    
    
    
    console.log(dados)
    
    Http.open("POST", url,true);
    
    Http.send(data);
    
    Http.onreadystatechange = (e) => {
    console.log(Http.responseText);
    location.reload(true);
    
    }
    
    }
    
    
    // this is inside your loop
  }, 10000)





/*

interval = null;

startBTN.onclick = function () {
    var i = 0;
    interval = setInterval(function () {
        console.log(i++);  // this is inside your loop
    }, 1);
};

stopBTN.onclick = function () {
    clearInterval(interval);
};

*/



