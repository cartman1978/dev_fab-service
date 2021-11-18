//  update quantity of item in bag
let updateLink = document.querySelectorAll(".update-quantity-link");
updateLink.forEach((link) => {
    link.addEventListener("click", () => {
        let form = link.previousElementSibling;
        form.submit();
    });
});
//  items from the cart
let removeLink = document.querySelectorAll(".remove-bag-item");
removeLink.forEach((link) => {
    link.addEventListener("click", () => {
        let itemId = link.getAttribute("id").split("remove_")[1];
        let url = `/bag/remove/${itemId}/`;

        fetch(url, {
            method: "POST",
            headers: {
                "X-CSRFToken": csrfToken
            },
        }).then(() => {
            location.reload();
        }).catch((error) => {
            alert("Try again, something has gone wrong.");
        });
    });
});