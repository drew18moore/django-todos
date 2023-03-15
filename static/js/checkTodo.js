$(document).ready(() => {
  $(".checkbox").click((e) => {
    let id = $(e.target).attr("id");

    $.ajax({
      url: `todo/${id}/check`,
    });
  });
});
