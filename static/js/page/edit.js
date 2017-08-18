/*保存*/
var saving = false;
$("#save").click(function() {
    if (saving) return false;
    var page_id = $("#page_id").val();
    var item_id = $("#item_id").val();
    var page_title = $("#page_title").val();
    var page_comments = $("#page_comments").val();
    var new_page = $("#new_page").val();
    var page_content = $("#page_content").val();
    var item_id = $("#item_id").val();
    var s_number = $("#s_number").val();
    var cat_id = $("#cat_id").val();
    var parent_cat_id = $("#parent_cat_id").val();
    if (parent_cat_id > 0 ) {
      cat_id = parent_cat_id ;
    };
    saving = true;
    $.post("/page/save",{
            "page_id": page_id,
            "cat_id": cat_id,
            "order_id": s_number,
            "page_content": page_content,
            "page_title": page_title,
            "page_comments": page_comments,
            "item_id": item_id,
            "new_page": new_page
      },
      function(data) {
            console.log(data)
            history.go(-1)
      },
      'json'
    )
});