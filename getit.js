function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

document.addEventListener("DOMContentLoaded", function () {
  // Faz textarea aumentar a altura automaticamente
  // Fonte: https://www.geeksforgeeks.org/how-to-create-auto-resize-textarea-using-javascript-jquery/#:~:text=It%20can%20be%20achieved%20by,height%20of%20an%20element%20automatically.
  let textareas = document.getElementsByClassName("autoresize");
  for (let i = 0; i < textareas.length; i++) {
    let textarea = textareas[i];
    function autoResize() {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    }

    textarea.addEventListener("input", autoResize, false);
  }

  // Sorteia classes de cores aleatoriamente para os cards
  let cards = document.getElementsByClassName("card");
  for (let i = 0; i < cards.length; i++) {
    let card = cards[i];
    card.className += ` card-color-${getRandomInt(
      1,
      5
    )} card-rotation-${getRandomInt(1, 11)}`;
  }
    let overlay = document.getElementById("popup-overlay");
    let popupTitle = document.getElementById("popup-title");
    let popupDetails = document.getElementById("popup-details");
    let popupConfirm = document.getElementById("popup-confirm");
    let popupCancel = document.getElementById("popup-cancel");

    let deleteLinks = document.getElementsByClassName("card-delete");
    for (let i = 0; i < deleteLinks.length; i++) {
    deleteLinks[i].addEventListener("click", function (event) {
        event.preventDefault();

        let id = this.dataset.id;
        let title = this.dataset.title;
        let details = this.dataset.details;

        popupTitle.textContent = title;
        popupDetails.textContent = details;
        popupConfirm.href = `/delete/${id}/confirmar`;

        overlay.classList.add("popup-visible");
    });
    }

    popupCancel.addEventListener("click", function () {
    overlay.classList.remove("popup-visible");
    });

    overlay.addEventListener("click", function (event) {
    if (event.target === overlay) {
        overlay.classList.remove("popup-visible");
    }
    });
});
