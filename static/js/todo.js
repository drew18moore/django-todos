$(document).ready(() => {
  $(".checkbox").click((e) => {
    let id = $(e.target).attr("id");

    $.ajax({
      url: `todo/${id}/check`,
    });
  });

  $("body").on("click", ".todo-body", (e) => {
    let input = $("<input class='todo-body-input' />").attr("value", e.target.textContent.trim())
    $(e.target).replaceWith(input)
    input.focus()
    let inputLength = input.val().length;
    input[0].selectionStart = inputLength;
    input[0].selectionEnd = inputLength;

    input.on("blur", () => {
      let inputValue = input[0].value || "&nbsp;"
      let todoBody = $(`<h2 class='todo-body'>${inputValue}</h2>`)
      input.replaceWith(todoBody)
    })
  })
});
