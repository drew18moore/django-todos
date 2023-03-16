$(document).ready(() => {
  $(".checkbox").click((e) => {
    let id = $(e.target).attr("id");

    $.ajax({
      url: `todo/${id}/check`,
    });
  });

  $("body").on("click", ".todo-body", (e) => {
    const id = e.target.id;
    let input = $(`<input class='todo-body-input' id="${id}"/>`).attr(
      "value",
      e.target.textContent.trim()
    );
    $(e.target).replaceWith(input);
    input.focus();
    let inputLength = input.val().length;
    input[0].selectionStart = inputLength;
    input[0].selectionEnd = inputLength;

    input.on("blur", () => {
      let inputValue = input[0].value;
      console.log(id);
      $.ajax({
        type: "POST",
        url: `todo/${id}/edit/`,
        data: { value: inputValue },
        beforeSend: function (xhr, settings) {
          if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type)) {
            xhr.setRequestHeader(
              "X-CSRFToken",
              $("input[name='csrfmiddlewaretoken']").val()
            );
          }
        },
      });
      let todoBody = $(
        `<h2 class='todo-body' id=${id}>${inputValue || "&nbsp;"}</h2>`
      );
      input.replaceWith(todoBody);
    });
  });
});
