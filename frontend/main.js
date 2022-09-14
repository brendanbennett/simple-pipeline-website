async function fetchText(request_text) {
    let request_dict = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: request_text }),
    }
    let response = await fetch("http://127.0.0.1:5000/gptj", request_dict);
    return response.text();
}

async function getInput() {
    // Selecting the input element and get its value 
    let inputVal = document.getElementById("textInput").value;
    if (inputVal.length === 0) {
        inputVal = document.getElementById("textInput").placeholder;
    }
    let response = await fetchText(inputVal);
    response_text = JSON.parse(response)["result"];

    const output = document.createElement("p");
    output.textContent = response_text;
    document.body.appendChild(output);
}