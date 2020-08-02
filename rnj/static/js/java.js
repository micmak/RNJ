$(window).load(function () {

    $(".loading-page .sk-cube-grid").fadeOut(1000,
        function () {
            $(this).parent().fadeOut(2000,
                function () {
                    $("body").css("overflow", "auto");
                    $(this).remove();
                })
        });
});

// $(window).load(function () {
//     $(".loading-page, .loading-page .sk-cube-grid").fadeOut(1000);
// });