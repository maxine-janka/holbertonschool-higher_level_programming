character = document.getElementById('character');

async function getCharacterName() {
    const url = "https://swapi-api.hbtn.io/api/people/5/?format=json";
    try {
        const response = await fetch(url); //send GET request to url
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        const jsonData = await response.json(); // wait for repsonse and store response object
        // console.log(jsonData);
        // console.log(jsonData.name);
        
        character.textContent = jsonData.name; //Set inner text to character

    }   catch (error) {
        console.error(error.message); //catch any errors, like fail to fetch if incorrect url
    }
}
getCharacterName();