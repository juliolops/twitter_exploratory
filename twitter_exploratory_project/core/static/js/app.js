contexto3 = document.getElementById("grafico3")
contexto4 = document.getElementById("grafico4")
contexto5 = document.getElementById("grafico5")
contexto6 = document.getElementById("grafico6")
contexto7 = document.getElementById("grafico7")
contexto8 = document.getElementById("grafico8")






var grafico3 = new Chart(contexto3,
    
    {

        type:"bar",
        data: {

            labels:{{ mean_count_words }},
            datasets: [{
                //label:"# de votos",
                data:[700,522,510,401,369,350,300,293,256,124],
                backgroundColor : "#45b6fe",

                borderColor:  [

                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)"
                ],

                borderWidth: 1

            }]
        }

    ,
    
    options: {
    
    
        title: {
    
            display:true,
            fontSize:20,
            text: "Top 10 Count Words",
            fontColor: 'white'
        },
    
        labels: {
    
            fontStyle: 'bold',
            fontColor: '#ff1493'
    
           
            
        },
    
    
        legend :{
    
            display:false
        },
    
        scales: {
        yAxes: [{
            display: true,
            
            gridLines: {
                display : true
               
            },
            ticks: {
                display: true,
                fontColor: 'white',
                beginAtZero:true,
                fontSize: 20
            }
        }],
        xAxes: [{
            gridLines: {
                display : true
            },
            ticks: {
                beginAtZero:true,
                fontColor: 'white',
                fontSize: 20
            }
        }]
    },
    
    
    
    
    
    }
}
    
    )














    var grafico4 = new Chart(contexto4,
    
        {
    
            type:"bar",
            data: {
    
                labels:["palavra 1","palavra 2","palavra 3","palavra 4","palavra 5","palavra 6","palavra 7","palavra 8","palavra 9","palavra 10"],
                datasets: [{
                    //label:"# de votos",
                    data:[643,520,410,401,341,325,295,293,246,124],
                    backgroundColor : "#45b6fe",
    
                    borderColor:  [
    
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)"
                    ],
    
                    borderWidth: 1
    
                }]
            }
    
        ,
        
        options: {
        
        
            title: {
        
                display:true,
                fontSize:20,
                text: "Top 10 TF-IDF Words",
                fontColor: 'white'
            },
        
            labels: {
        
                fontStyle: 'bold',
        
               
                
            },
        
        
            legend :{
        
                display:false
            },
        
            scales: {
            yAxes: [{
                display: true,
                
                gridLines: {
                    display : true
                   
                },
                ticks: {
                    display: true,
                    fontColor: 'white',
                    beginAtZero:true,
                    fontSize: 20
                }
            }],
            xAxes: [{
                gridLines: {
                    display : true
                },
                ticks: {
                    beginAtZero:true,
                    fontColor: 'white',
                    fontSize: 20
                }
            }]
        },
        
        
        
        
        
        }
    }
        
        )

        












var grafico5 = new Chart(contexto5,
    
    {

        type:"bar",
        data: {

            labels:["palavra 1","palavra 2","palavra 3","palavra 4","palavra 5","palavra 6","palavra 7","palavra 8","palavra 9","palavra 10"],
            datasets: [{
                //label:"# de votos",
                data:[743,420,415,411,331,325,285,283,236,124],
                backgroundColor : "#45b6fe",

                borderColor:  [

                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)"
                ],

                borderWidth: 1

            }]
        }

    ,
    
    options: {
    
    
        title: {
    
            display:true,
            fontSize:20,
            text: "Top 10 Count Documents",
            fontColor: 'white'
        },
    
        labels: {
    
            fontStyle: 'bold',
    
           
            
        },
    
    
        legend :{
    
            display:false
        },
    
        scales: {
        yAxes: [{
            display: true,
            
            gridLines: {
                display : true
               
            },
            ticks: {
                display: true,
                fontColor: 'white',
                beginAtZero:true,
                fontSize: 20
            }
        }],
        xAxes: [{
            gridLines: {
                display : true
            },
            ticks: {
                beginAtZero:true,
                fontColor: 'white',
                fontSize: 20
            }
        }]
    },
    
    
    
    
    
    }
}
    
    )








    var grafico6 = new Chart(contexto6,
    
        {
    
            type:"bar",
            data: {
    
                labels:["palavra 1","palavra 2","palavra 3","palavra 4","palavra 5","palavra 6","palavra 7","palavra 8","palavra 9","palavra 10"],
                datasets: [{
                    //label:"# de votos",
                    data:[743,420,415,411,331,325,285,283,236,124],
                    backgroundColor : "#45b6fe",
    
                    borderColor:  [
    
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)"
                    ],
    
                    borderWidth: 1
    
                }]
            }
    
        ,
        
        options: {
        
        
            title: {
        
                display:true,
                fontSize:20,
                text: "Top 10 Count Documents (%)",
                fontColor: 'white'
            },
        
            labels: {
        
                fontStyle: 'bold',
        
               
                
            },
        
        
            legend :{
        
                display:false
            },
        
            scales: {
            yAxes: [{
                display: true,
                
                gridLines: {
                    display : true
                   
                },
                ticks: {
                    display: true,
                    fontColor: 'white',
                    beginAtZero:true,
                    fontSize: 20
                }
            }],
            xAxes: [{
                gridLines: {
                    display : true
                },
                ticks: {
                    beginAtZero:true,
                    fontColor: 'white',
                    fontSize: 20
                }
            }]
        },
        
        
        
        
        
        }
    }
        
        )
    
    












var grafico7 = new Chart(contexto7,
    
    {

        type:"bar",
        data: {

            labels:[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200],
            datasets: [{
                //label:"# de votos",
                data:[9,9,2,8,7,13,19,21,40,47,42,19,20,19,17,15,13,10,10,7],
                backgroundColor : "#45b6fe",

                borderColor:  [

                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)",
                    "rgba(53,98,68,1)"
                ],

                borderWidth: 1

            }]
        }

    ,
    
    options: {
    
    
        title: {
    
            display:true,
            fontSize:20,
            text: "Histogram quantity words",
            fontColor: 'white'
        },
    
        labels: {
    
            fontStyle: 'bold',
    
           
            
        },
    
    
        legend :{
    
            display:false
        },
    
        scales: {
        yAxes: [{
            display: true,
            
            gridLines: {
                display : true
               
            },
            ticks: {
                display: true,
                fontColor: 'white',
                beginAtZero:true,
                fontSize: 20
            }
        }],
        xAxes: [{
            gridLines: {
                display : true
            },
            ticks: {
                beginAtZero:true,
                fontColor: 'white',
                fontSize: 20
            }
        }]
    },
    
    
    
    
    
    }
}
    
    )








    
    
    
    
    
    
    
    
    
    
    var grafico8 = new Chart(contexto8,
        
        {
    
            type:"bar",
            data: {
    
                labels:[10,20,30,40,50,60,70,80,90,100,210,320,230,190,150,160,170,180,190,200],
                datasets: [{
                    //label:"# de votos",
                    data:[9,9,2,8,7,13,19,21,40,47,42,19,20,19,17,15,13,10,10,7],
                    backgroundColor : "#45b6fe",
    
                    borderColor:  [
    
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)",
                        "rgba(53,98,68,1)"
                    ],
    
                    borderWidth: 1
    
                }]
            }
    
        ,
        
        options: {
        
        
            title: {
        
                display:true,
                fontSize:20,
                text: "Histogram quantity different words",
                fontColor: 'white'
            },
        
            labels: {
        
                fontStyle: 'bold',
        
               
                
            },
        
        
            legend :{
        
                display:false
            },
        
            scales: {
            yAxes: [{
                display: true,
                
                gridLines: {
                    display : true
                   
                },
                ticks: {
                    display: true,
                    fontColor: 'white',
                    beginAtZero:true,
                    fontSize: 20
                }
            }],
            xAxes: [{
                gridLines: {
                    display : true
                },
                ticks: {
                    beginAtZero:true,
                    fontColor: 'white',
                    fontSize: 20
                }
            }]
        },
        
        
        
        
        
        }
    }
        
        )
    
    
    
    