
top_offset = $("a[name='top']").offset().top
proj_offset = $("a[name='projects']").offset().top
contact_offset = $("a[name='bottom']").offset().top

navbar_free = true

$(function () {
    $(window).scroll(function() {
        //Control navbar at top of page vs free
        navbar = $(".navbar")
        nav_offset = navbar.offset().top
        if (nav_offset>30) {
            if(!navbar_free){
                $(".jf-navbar").addClass("jf-navbar-free");
                $(".jf-navbar").animate({
                   "padding-top":"5px",
                   "padding-bottom": "5px"
                }, "fast");
            }
            navbar_free = true
        }
        else {
            if(navbar_free){
                $(".jf-navbar").removeClass("jf-navbar-free");
                $(".jf-navbar").animate({
                   "padding-top":"15px",
                   "padding-bottom": "15px"
                }, "fast");
            }
            navbar_free = false
        }

        //Auto-highlight items on navbar 
        window_height = $(window).height()
        contact_offset = $("a[name='bottom']").offset().top-window_height
        proj_offset = $("a[name='projects']").offset().top-window_height
        if( nav_offset >= contact_offset){
            $(".jf-navbar-item").removeClass("jf-active");
            $("#navbar_contact").addClass("jf-active");
        }else if (nav_offset >= proj_offset){
            $(".jf-navbar-item").removeClass("jf-active");
            $("#navbar_projects").addClass("jf-active");
        }else{
            $(".jf-navbar-item").removeClass("jf-active");
            $("#navbar_home").addClass("jf-active");
        }

        $("#navbar_offset").text(nav_offset)
        $("#navbar_projects_offset").text(proj_offset)
        $("#navbar_contact_offset").text(contact_offset)
    });
});

