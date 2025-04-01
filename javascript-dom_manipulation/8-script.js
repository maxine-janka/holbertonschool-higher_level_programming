document.addEventListener('DOMContentLoaded', sayHello) //Wait for HTML to parse then call function

async function sayHello() {
    const url = "https://hellosalut.stefanbohacek.dev/?lang=fr";
    hello = document.getElementById('hello');

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        const jsonData = await response.json();
        //console.log(jsonData.hello);
        hello.textContent = jsonData.hello;
    } catch(error) {
        console.error(error.message);
    }
}