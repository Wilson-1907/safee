const button = document.getElementById("mic-button")
const status = document.getElementById("status")

const recognition = new(window.SpeechRecognition || window.webkitSpeechRecognition)()

recognition.lang = "en-US"

button.addEventListener("click", () => {

button.classList.add("listening")
status.innerText = "Listening..."

recognition.start()

})

recognition.onresult = async function(event){

const speech = event.results[0][0].transcript

status.innerText = "You said: " + speech

button.classList.remove("listening")

// send to backend

const response = await fetch("http://localhost:8000/api/voice", {

method:"POST",

headers:{
"Content-Type":"application/json"
},

body: JSON.stringify({
driver_input: speech
})

})

const data = await response.json()

const reply = data.response

status.innerText = reply

// speak response

const speechSynthesisUtterance = new SpeechSynthesisUtterance(reply)

speechSynthesis.speak(speechSynthesisUtterance)

}

recognition.onerror = function(){

button.classList.remove("listening")

status.innerText = "Could not hear you"

}