addItem = document.getElementById('add_item');
myList = document.querySelector('ul');
//onsole.log(myList);

addItem.addEventListener('click', () => {
    listItem = document.createElement('li');
    //console.log(listItem);
    listItem.textContent = 'Item';
    myList.append(listItem);
});
