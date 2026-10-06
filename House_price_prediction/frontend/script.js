const form=document.getElementById("predictionForm");
const result=document.getElementById("result");
const loading=document.getElementById("loading");
const price=document.getElementById("price");
const summary=document.getElementById("summary");

form.addEventListener("submit",async function(event){

event.preventDefault();

loading.style.display="block";
result.style.display="none";

const data={
area:parseFloat(document.getElementById("area").value),
bedrooms:parseInt(document.getElementById("bedrooms").value),
bathrooms:parseInt(document.getElementById("bathrooms").value),
stories:parseInt(document.getElementById("stories").value),
parking:parseInt(document.getElementById("parking").value),
age:parseInt(document.getElementById("age").value),
location:document.getElementById("location").value
};

try{

const response=await fetch("http://127.0.0.1:8000/predict",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify(data)
});

if(!response.ok){
throw new Error("Prediction failed");
}

const resultData=await response.json();

const predictedPrice=resultData.predicted_price;

price.innerHTML="₹ "+predictedPrice.toLocaleString("en-IN");

summary.innerHTML=`
<strong>Area:</strong> ${data.area} sq ft<br>
<strong>Bedrooms:</strong> ${data.bedrooms}<br>
<strong>Bathrooms:</strong> ${data.bathrooms}<br>
<strong>Floors:</strong> ${data.stories}<br>
<strong>Parking:</strong> ${data.parking}<br>
<strong>Property Age:</strong> ${data.age} years<br>
<strong>Location:</strong> ${data.location}
`;

result.style.display="block";

}
catch(error){

alert("Unable to connect to backend. Please start FastAPI server.");

}

loading.style.display="none";

});