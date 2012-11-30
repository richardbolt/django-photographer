/*
 * jQuery custom navigation.
 */
;(function($) {
    function do_nav(item){
        $(item).each(function(index) {
            if ($(this).siblings('ul').length) {
                $(this).click(function(){
                    if ($(this).siblings('ul').is(':hidden')){
                        $(this).siblings('ul').show();
                        $(this).addClass('hover');
                        // Prepare and sub-items for show/hide
                        $(item).siblings('ul').find('>li>a').each(function(index) {
                            $(this).unbind('click');
                            $(this).click(function(){
                                if (!$(this).siblings('ul').length) {
                                    return;
                                }
                                if ($(this).siblings('ul').is(':hidden')) {
                                    $(this).siblings('ul').show();
                                    $(this).addClass('hover');
                                    return false;
                                } else {
                                    $(this).siblings('ul').hide();
                                    $(this).removeClass('hover');
                                    return false;
                                }
                            });
                        });
                    } else {
                        $(this).siblings('ul').hide();
                        $(this).removeClass('hover');
                    }
                    return false;
                });
            }
        });
    };
    
    $(document).ready(function(){            
        do_nav('nav>ul>li>a');
    });
})(jQuery);