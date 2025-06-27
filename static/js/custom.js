(function ($, window, document, undefined) {
    'use strict';
    var $winW = function () {
        return $(window).width();
    };
    var $winH = function () {
        return $(window).height();
    };
    var $screensize = function (element) {
        $(element).width($winW()).height($winH());
    };
    var screencheck = function (mediasize) {
        if (typeof window.matchMedia !== "undefined") {
            var screensize = window.matchMedia("(max-width:" + mediasize + "px)");
            if (screensize.matches) {
                return true;
            } else {
                return false;
            }
        } else {
            if ($winW() <= mediasize) {
                return true;
            } else {
                return false;
            }
        }
    };
    $(document).ready(function () {
        $(window).on('load', function () {
            $('.preloader').fadeOut();
            $('.animated-row').each(function () {
                var $this = $(this);
                $this.find('.animate').each(function (i) {
                    var $item = $(this);
                    var animation = $item.data('animate');
                    $item.on('inview', function (event, isInView) {
                        if (isInView) {
                            setTimeout(function () {
                                $item.addClass('animated ' + animation).removeClass('animate');
                            }, i * 50);
                        } else if (!screencheck(767)) {
                            $item.removeClass('animated ' + animation).addClass('animate');
                        }
                    });
                });
            });
        });
        if ($('.facts-list').length) {
            $('.facts-list').owlCarousel({
                loop: true,
                nav: false,
                dots: true,
                items: 3,
                margin: 30,
                autoplay: false,
                smartSpeed: 700,
                autoplayTimeout: 6000,
                responsive: {
                    0: {
                        items: 1,
                        margin: 0
                    },
                    460: {
                        items: 1,
                        margin: 0
                    },
                    576: {
                        items: 2,
                        margin: 20
                    },
                    992: {
                        items: 3,
                        margin: 30
                    }
                }
            });
        }
        if ($('.services-list').length) {
            $('.services-list').owlCarousel({
                loop: true,
                nav: false,
                dots: true,
                items: 3,
                margin: 30,
                autoplay: false,
                smartSpeed: 700,
                autoplayTimeout: 6000,
                responsive: {
                    0: {
                        items: 1,
                        margin: 0
                    },
                    460: {
                        items: 1,
                        margin: 0
                    },
                    576: {
                        items: 2,
                        margin: 20
                    },
                    992: {
                        items: 3,
                        margin: 30
                    }
                }
            });
        }
        if ($('.gallery-list').length) {
            $('.gallery-list').owlCarousel({
                loop: false,
                nav: false,
                dots: true,
                items: 3,
                autoplay: true,
                smartSpeed: 700,
                autoplayTimeout: 4000,
                responsive: {
                    0: {
                        items: 1,
                        margin: 0
                    },
                    576: {
                        items: 2,
                        margin: 20
                    },
                    992: {
                        items: 3,
                        margin: 30
                    }
                }
            });
        }
        if ($('.testimonials-slider').length) {
            $('.testimonials-slider').owlCarousel({
                loop: true,
                nav: false,
                dots: true,
                items: 1,
                margin: 30,
                autoplay: true,
                smartSpeed: 700,
                autoplayTimeout: 6000,
                responsive: {
                    0: {
                        items: 1,
                        margin: 0
                    },
                    768: {
                        items: 1
                    }
                }
            });
        }

        const sectionsCount = document.querySelectorAll('.fullpage-default .section').length;


        const anchorsArray = [];
        for (let i = 1; i <= sectionsCount; i++) {
            anchorsArray.push('slide' + (i < 10 ? '0' + i : i));
        }


        window.scrollingEnabled = false;


        if ($('.fullpage-default').length) {
            var myFullpage = new fullpage('.fullpage-default', {
                licenseKey: ' C7F41B00-5E824594-9A5EFB99-B556A3D5',
                anchors: anchorsArray,
                menu: '#nav',
                lazyLoad: true,
                navigation: true,
                navigationPosition: 'right',
                scrollOverflow: true,
                responsiveWidth: 768,
                responsiveHeight: 600,
                responsiveSlides: true,

                onLeave: function (origin, destination, direction) {
                    if (!window.scrollingEnabled && origin.index === 0) {
                        console.log('Scroll blocked - button not clicked yet');
                        return false;
                    }
                    return true;
                },

                afterLoad: function (origin, destination, direction) {
                    const section = destination.item;
                    const video = section.querySelector("video");


                    document.querySelectorAll("video").forEach(v => {
                        v.pause();
                        v.currentTime = 0;
                    });

                    // מריץ רק אם זה לא slide01
                    if (video && destination.anchor !== "slide01") {
                        video.play();
                        console.log("Playing video in section:", destination.anchor);
                    }
                },
            });


            window.myFullpage = myFullpage;


            setTimeout(() => {
                const currentHash = window.location.hash;
                if (currentHash && currentHash !== '#slide01' && !window.scrollingEnabled) {
                    console.log('Enabling scrolling due to hash:', currentHash);
                    window.scrollingEnabled = true;


                    const btn = document.querySelector('.view-videos-btn');
                    if (btn) {
                        btn.style.display = 'none';
                    }
                }
            }, 300);
        }

        function enableScrolling() {
            scrollingEnabled = true;


            const btn = document.querySelector('.view-videos-btn');
            if (btn) {
                btn.style.display = 'none';
            }

            setTimeout(() => {
                if (myFullpage) {
                    myFullpage.moveSectionDown();
                }
            }, 100);
        }


        $(document).on('click', '.navbar-toggle', function () {
            $('.navbar-collapse').slideToggle(300);
            return false;
        }).on('click', '.navigation-menu > li > a', function () {
            $('.navbar-collapse').slideUp(300);
        }).on('click', '.next-section', function () {
            fullpage_api.moveSectionDown();
        });
        $('.facts-row').on('inview', function (event, isInView) {
            $('.count-number').each(function () {
                $(this).prop('Counter', 0).animate({
                    Counter: $(this).text()
                }, {
                    duration: 1000,
                    easing: 'swing',
                    step: function (now) {
                        $(this).text(Math.ceil(now));
                    }
                });
                setTimeout(function () {
                    $('.count-number').removeClass('count-number').addClass('counted');
                }, 1000);
            });
        });
        $('.skills-row').on('inview', function (event, isInView) {
            $(this).addClass('view');
        });
        $(document).on('click', '.menu-trigger', function () {
            $('body').toggleClass('sidemenu-open');
        }).on('click', '.side-menu .navbar-nav li a', function () {
            $('body').removeClass('sidemenu-open');
        });
    });
})(jQuery, window, document);