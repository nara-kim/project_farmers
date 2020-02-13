<template>

<div class = "price">
<link href="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">

	<!-- <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous"> -->
    <!-- <div v-for="price of pricelist" v-bind:key="price.id">
      {{price.test.split('/')[1].split(',')[1].split("'")[1]}}
      {{price.test.split('/')[1].split(',')[2].split("'")[1]}}
      {{price.test.split('/')[1].split(',')[3].split("'")[1]}}
      가격
  </div> -->

<div class="spe-cor">
    <div class="container">
        <h2>Responsive Slider <small>[Just Use Normal Slider Code and Get Full Responsive Slider]</small></h2>
        <div class="row">
            <div id="slider-1" class="carousel carousel-by-item slide" data-ride="carousel">
                <div class="carousel-inner">
                    <div class="carousel-item active">
                        <div class="col-lg-2 col-md-3 col-sm-4 col-4">
                            <img class="d-block img-fluid" src="https://images.unsplash.com/photo-1564359916269-08ddfdf543ee?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60" alt="First slide">
                        </div>
                    </div>
                    <div class="carousel-item">
                        <div class="col-lg-2 col-md-3 col-sm-4 col-4">
                            <img class="d-block img-fluid" src="https://images.unsplash.com/photo-1558979158-65a1eaa08691?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60" alt="First slide">
                        </div>
                    </div>
                    <div class="carousel-item">
                        <div class="col-lg-2 col-md-3 col-sm-4 col-4">
                            <img class="d-block img-fluid" src="https://images.unsplash.com/photo-1562101806-ecd80e69bbb7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60" alt="First slide">
                        </div>
                    </div>
                    <div class="carousel-item">
                        <div class="col-lg-2 col-md-3 col-sm-4 col-4">
                            <img class="d-block img-fluid" src="https://images.unsplash.com/photo-1564423531399-89ed4c4e3ddb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60" alt="Second slide">
                        </div>
                    </div>
                    <div class="carousel-item">
                        <div class="col-lg-2 col-md-3 col-sm-4 col-4">
                            <img class="d-block img-fluid" src="https://images.unsplash.com/flagged/photo-1564373020761-b9e8ab5c03b0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60" alt="Third slide">
                        </div>
                    </div>
                    <div class="carousel-item">
                        <div class="col-lg-2 col-md-3 col-sm-4 col-4">
                            <img class="d-block img-fluid" src="https://images.unsplash.com/photo-1564410267845-ae5acf1ce8d9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60" alt="Third slide">
                        </div>
                    </div>
                </div>
                <a class="carousel-control-prev" href="#slider-1" role="button" data-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="sr-only">Previous</span>
                </a>
                <a class="carousel-control-next" href="#slider-1" role="button" data-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="sr-only">Next</span>
                </a>
            </div>
        </div>
    </div>
</div>
</div>
</template>

<script src="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
<script src="//code.jquery.com/jquery-1.11.1.min.js"></script>

<script>
import axios from 'axios';

export default {
  data() {
    return {	
      weatherlist: []
    }
  },
  created() {
    this.all();
  },
  methods: {
    all: function () {
      axios.get('http://127.0.0.1:8000/api/weatherinfo/')
        .then( response => {
                    this.weatherlist = response.data
        })
        .catch( err => {
                    console.log(err)
      });
    }


    
  },

}
</script>

<script>
var mainFunction = function(options) {
    var vars = {
        id: '',
        bootsGrid: ["col-md-1", "col-md-2", "col-md-3", "col-md-4", "col-md-6", "col-md-12", "col-sm-1", "col-sm-2", "col-sm-3", "col-sm-4", "col-sm-6", "col-sm-12", "col-lg-1", "col-lg-2", "col-lg-3", "col-lg-4", "col-lg-6", "col-lg-12", "col-xs-1", "col-xs-2", "col-xs-3", "col-xs-4", "col-xs-6", "col-xs-12", "col-xl-1", "col-xl-2", "col-xl-3", "col-xl-4", "col-xl-6", "col-xl-12"],
        breakPoint : [1200, 992, 768, 567, 0]
    }
    var root = this;

    construct = function(v, options) {
        $.extend(v, options);
    }
    this.GetUnique = function(e) {
        var l = [],
            s = temp_c = [],
            t = vars.bootsGrid;
        $(e).find('.carousel-item').each(function() {
            for (var l = $(this).find('div').first().attr("class").split(/\s+/), t = 0; t < l.length; t++) s.push(l[t])
        });
        for (var c = 0; c < s.length; c++) temp_c = s[c].split("-"), 2 == temp_c.length && (temp_c.push(""), temp_c[2] = temp_c[1], temp_c[1] = "xs", s[c] = temp_c.join("-")), -1 == $.inArray(s[c], l) && $.inArray(s[c], t) && l.push(s[c]);
        setcss(l, '#' + vars.id + ' .carousel-item', '#' + vars.id + ' .carousel-inner')
        return l
    }
    setcss = function(e, l, s) {
		var t = [];
        $.each(vars.breakPoint,function(i,e){
			t.push("");
        })
        for (var c = d = f = g = 0, o = [], a = 0; a < e.length; a++) {
            var i = e[a].split("-");
            if (3 == i.length) {
                switch (i[1]) {
                    case "xl":
                        d = 0;
                        break;
                    case "lg":
                        d = 1;
                        break;
                    case "md":
                        d = 2;
                        break;
                    case "sm":
                        d = 3;
                        break;
                    case "xs":
                        d = 4
                }
                t[d] = i[2]
            }
        }
        var slider = document.getElementById(vars.id); 
        var style = document.createElement("STYLE");
        slider.insertBefore(style, slider.childNodes[0]).id=vars.id+'-style';
        var style = $("#"+vars.id+'-style');
        for (var n = 0; n < t.length; n++)
            if ("" !== t[n]) {
                if (0 === c && (c = 12 / t[n]),
                    f = 12 / t[n],
                    g = 100 / f,
                    a = s + " > .carousel-item.active.carousel-item-right," + s + " > .carousel-item.carousel-item-next {-ms-transform: translate3d(" + g + "%, 0, 0);-o-transform: translate3d(" + g + "%, 0, 0);-moz-transform: translate3d(" + g + "%, 0, 0);-webkit-transform: translate3d(" + g + "%, 0, 0);transform: translate3d(" + g + ", 0, 0);left: 0;}" + s + " > .carousel-item.active.carousel-item-left," + s + " > .carousel-item.carousel-item-prev {-webkit-transform: translate3d(-" + g + "%, 0, 0);transform: translate3d(-" + g + "%, 0, 0);left: 0;}" + s + " > .carousel-item.carousel-item-left, " + s + " > .carousel-item.carousel-item-prev.carousel-item-right, " + s + " > .carousel-item.active {-webkit-transform: translate3d(0, 0, 0);transform: translate3d(0, 0, 0);left: 0;}", f > 1) {
                        
                    for (k = 0; k < f - 1; k++) {
                        o.push(l + " .cloneditem-" + k);
                    }
                    o.length && (a = a + o.join(",") + "{display: block;}"), o = []
                }
                0 !== vars.breakPoint[n] && (a = "@media all and (min-width: " + vars.breakPoint[n] + "px){" + a + "}"),
                    style.prepend(a)
            }
        $(l).each(function() {
            for (var e = $(this), l = 0; l < c - 1; l++) {
                (e = e.next()).length || (e = $(this).siblings(":first")), e.children(":first-child").clone().addClass("cloneditem-" + l).appendTo($(this))
            }
        })
    }
    construct(vars, options);
}
$.fn.responsiveCarousel = function(option) {
    $(this).each(function() {
        var _root = this;
        option = { id: $(this).attr('id') }
        var main = new mainFunction(option);
        main.GetUnique(_root);
    })
};
//Use Different Slider IDs for multiple slider
$(document).ready(function() {
    $('#slider-1').responsiveCarousel();
    $('#slider-2').responsiveCarousel();
});
</script>

<style scoped>
@import url('https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css');
/*================================================*/
@import url('https://fonts.googleapis.com/css?family=Roboto');
.carousel{
    width: 100%;
}
.carousel-item > div {
  float: left;
}
.carousel-by-item [class*="cloneditem-"] {
  display: none;
}
.price{
	margin-bottom: 5%;
}
.spe-cor{
    height: 180px;
    background-color: rgb(235, 232, 232);
}
</style>
