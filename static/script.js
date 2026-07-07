new Chart(document.getElementById("solarChart"),{

type:"line",

data:{

labels:["6","8","10","12","2","4","6"],

datasets:[{

label:"kW",

data:[1,3,5,8,7,5,2],

borderColor:"#22c55e",

backgroundColor:"rgba(34,197,94,.2)",

fill:true,

tension:.4

}]

}

});



new Chart(document.getElementById("batteryChart"),{

type:"doughnut",

data:{

labels:["Used","Remaining"],

datasets:[{

data:[25,75]

}]

}

});



new Chart(document.getElementById("revenueChart"),{

type:"bar",

data:{

labels:["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],

datasets:[{

label:"₹",

data:[250,310,280,350,420,380,450]

}]

}

});



new Chart(document.getElementById("energyChart"),{

type:"line",

data:{

labels:["Jan","Feb","Mar","Apr","May","Jun"],

datasets:[{

label:"kWh",

data:[620,710,790,850,920,980],

borderColor:"#3b82f6",

fill:false,

tension:.4

}]

}

});
