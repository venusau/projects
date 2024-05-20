document.addEventListener("DOMContentLoaded", function() {
    const contactListContainer = document.getElementById("contactList");
    const createContactButton = document.getElementById("createContactButton");
    const contactFormContainer = document.getElementById("contactFormContainer");
    const contactModal = document.getElementById("contactModal");
    const closeModalButton = document.getElementById("closeModal");

    // Function to render contact list
    const renderContactList = async () => {
        const response = await fetch("http://127.0.0.1:5000/contacts");
        const data = await response.json();
        const contacts = data.contacts;

        contactListContainer.innerHTML = ""; // Clear previous content

        contacts.forEach(contact => {
            const contactElement = document.createElement("div");
            contactElement.innerHTML = `
                <div>
                    <span>${contact.firstName} ${contact.lastName}</span>
                    <span>${contact.email}</span>
                    <button onclick="openEditModal(${contact.id})">Edit</button>
                </div>
            `;
            contactListContainer.appendChild(contactElement);
        });
    };

    // Function to open modal for creating/editing contact
    const openModal = (contact = {}) => {
        // Render contact form
        contactFormContainer.innerHTML = `
            <form id="contactForm">
                <label for="firstName">First Name:</label>
                <input type="text" id="firstName" value="${contact.firstName || ''}">
                <label for="lastName">Last Name:</label>
                <input type="text" id="lastName" value="${contact.lastName || ''}">
                <label for="email">Email:</label>
                <input type="text" id="email" value="${contact.email || ''}">
                <button type="submit">${contact.id ? 'Update' : 'Create'}</button>
            </form>
        `;

        // Show modal
        contactModal.style.display = "block";
    };

    // Function to close modal
    const closeModal = () => {
        contactModal.style.display = "none";
    };

    // Function to handle form submission
    const handleSubmit = async (e) => {
        e.preventDefault();
        const form = e.target;
        const data = {
            firstName: form.querySelector("#firstName").value,
            lastName: form.querySelector("#lastName").value,
            email: form.querySelector("#email").value
        };

        let url = "http://127.0.0.1:5000/create_contact";
        let method = "POST";

        if (form.dataset.contactId) {
            url = `http://127.0.0.1:"5000/update_contact/${form.dataset.contactId}`;
            method = "PATCH";
        }

        try {
            const response = await fetch(url, {
                method: method,
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            });

            if (!response.ok) {
                const responseData = await response.json();
                alert(responseData.message);
            } else {
                closeModal();
                renderContactList();
            }
        } catch (error) {
            console.error("Error:", error);
            alert("An error occurred while submitting the form.");
        }
    };

    // Event listener for create contact button
    createContactButton.addEventListener("click", () => {
        openModal();
    });

    // Event listener for form submission
    contactFormContainer.addEventListener("submit", handleSubmit);

    // Event listener for closing modal
    closeModalButton.addEventListener("click", () => {
        closeModal();
    });

    // Initial rendering of contact list
    renderContactList();
});
