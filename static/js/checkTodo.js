$(document).ready(() => {
  $(".checkbox").click((e) => {
    let id = $(e.target).attr("id");
    let isChecked = $(e.target).is(":checked")
    
    $.ajax({
      // data: id,
      url: `todo/${id}/check`,
      success: (res) => {
        console.log(res);
      }
    })
  })
})