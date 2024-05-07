const rooms = [
    {
        image: "../images/1.jpg",
        alt: "Family Room",
        description: "Lorem ipsum . Id, eum earum possimus Lorem ipsum dolor sit amet consectetur adipisicing elit. Recusandae consequuntur ab in tempore neque eligendi dolorum iure velit temporibus incidunt maxime dicta obcaecati esse deleniti placeat, tenetur quaerat cumque quam? consequatur numquam quidem molestiae inventore dolorum ectus, officiis.",
        price: "100$-Night",
        rooms: "2 rooms",
        beds: "3 beds"
    },
    {
        image: "../images/2.jpg",
        alt: "Family Room",
        description: "Lorem ipsum . Id, eum earum possimus Lorem ipsum dolor sit amet consectetur adipisicing elit.",
        price: "120$-Night",
        rooms: "2 rooms",
        beds: "3 beds"
    },
    {
        image: "../images/3.jpg",
        alt: "Family Room",
        description: "Lorem ipsum . Id, eum earum possimus Lorem ipsum dolor sit amet consectetur adipisicing elit.",
        price: "180$ / Night",
        rooms: "2 rooms",
        beds: "3 beds"
    }
];

// Function to create room cards dynamically
function createRoomCards() {
    const roomsContainer = document.querySelector('.roomsBox');

    let currentRow;

    rooms.forEach((room, index) => {
        // Create a new row for every third card or at the start
        if (index % 3 === 0) {
            currentRow = document.createElement('div');
            currentRow.className = 'row';
            roomsContainer.appendChild(currentRow);
        }

        const col = document.createElement("div");
        col.className = "col-lg-4 col-md-6 column p-0 position-relative image bg-white";

        const image = document.createElement("img");
        image.className = "rounded";
        image.src = room.image;
        image.alt = room.alt;

        const descriptionBar = document.createElement("div");
        descriptionBar.className = "descriptionBar d-flex justify-content-around align-items-center flex-column p-2 position-absolute text-white";

        const description = document.createElement("h5");
        description.className = "p-2";
        description.textContent = room.description;

        const roomsInfo = document.createElement("div");
        roomsInfo.className = "d-flex justify-content-around w-100";

        const price = document.createElement("h4");
        price.textContent = room.price;
        roomsInfo.appendChild(price);

        const roomsElement = document.createElement("h4");
        roomsElement.textContent = room.rooms;
        roomsInfo.appendChild(roomsElement);

        const bedsElement = document.createElement("h4");
        bedsElement.textContent = room.beds;
        roomsInfo.appendChild(bedsElement);

        descriptionBar.appendChild(description);
        descriptionBar.appendChild(roomsInfo);

        col.appendChild(image);
        col.appendChild(descriptionBar);

        currentRow.appendChild(col);
    });

    // Add the icon toggle functionality
    addIconToggle();
}

// Function to add icon toggle functionality
function addIconToggle() {
    const descriptionBars = document.querySelectorAll('.descriptionBar');
    descriptionBars.forEach(descriptionBar => {
        // Create and append the icon
        const icon = document.createElement('i');
        icon.className = 'fas fa-info-circle icon-toggle my-1';
        descriptionBar.appendChild(icon);

        // Add click event listener to the icon
        icon.addEventListener('click', () => {
            // Toggle the display of the h5 element
            const h5 = descriptionBar.querySelector('h5');
            h5.style.display = (h5.style.display === 'block') ? 'none' : 'block';
            descriptionBar.style.height = (descriptionBar.style.height === '16%') ? 'auto' : '16%';
        });
    });
}

// Call the function to create room cards
createRoomCards();
