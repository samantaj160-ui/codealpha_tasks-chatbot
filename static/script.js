loadQuestions();

async function loadQuestions(){

    const response =
    await fetch('/questions');

    const questions =
    await response.json();

    let list =
    document.getElementById("faq-list");

    list.innerHTML = "";

    questions.forEach(q => {

        list.innerHTML += `
        <li>${q}</li>
        `;
    });
}

async function sendMessage(){

    const input =
    document.getElementById("user-input");

    const message =
    input.value.trim();

    if(message === "")
        return;

    const chatBox =
    document.getElementById("chat-box");

    chatBox.innerHTML += `
    <div class="user">
        <span>${message}</span>
    </div>
    `;

    input.value = "";

    chatBox.innerHTML += `
    <div class="bot" id="typing">
        <span>Typing...</span>
    </div>
    `;

    const response =
    await fetch("/chat",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            message:message
        })
    });

    const data =
    await response.json();

    document
    .getElementById("typing")
    .remove();

    chatBox.innerHTML += `
    <div class="bot">
        <span>${data.reply}</span>
    </div>
    `;

    chatBox.scrollTop =
    chatBox.scrollHeight;
}

async function addFAQ(){

    const question =
    document.getElementById("new-question").value;

    const answer =
    document.getElementById("new-answer").value;

    if(question === "" || answer === "")
        return;

    await fetch("/add_faq",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            question:question,
            answer:answer
        })
    });

    alert("FAQ Added Successfully");

    document.getElementById(
        "new-question"
    ).value = "";

    document.getElementById(
        "new-answer"
    ).value = "";

    loadQuestions();
}

document
.getElementById("user-input")
.addEventListener(
"keypress",
function(e){

    if(e.key === "Enter"){
        sendMessage();
    }
});