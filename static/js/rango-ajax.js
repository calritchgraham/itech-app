$(document).ready(function() {
    $('#like_btn').click(function() {
        var categoryIdVar;
        categoryIdVar = $(this).attr('data-categoryid');

        $.get('/rango/like_category/',
            {'category_id': categoryIdVar},
            function(data) {
                $('#like_count').html(data);
                $('#like_btn').hide();
            })
    });

    $('.like_page_btn').click(function() {
        var pageIdVar;
        pageIdVar = $(this).attr('data-pageid');

        $.get('/rango/like_page/',
            {'page_id': pageIdVar},
            function(data) {
                $('.like_page_count').html(data);
                $('#like_page_btn').hide();
            })
    });

    $('.like_video_btn').click(function() {
        var videoIdVar;
        videoIdVar = $(this).attr('data-videoid');

        $.get('/rango/like_video/',
            {'video': videoIdVar},
            function(data) {
                $('#like_video_count').html(data);
                $('#like_video_btn').hide();
            })
    });

    $('#search-input').keyup(function() {
        var query;
        query = $(this).val();

        $.get('/rango/suggest',
              {'suggestion': query},
              function(data) {
                  $('#categories-listing').html(data);
              })
    });


   
});