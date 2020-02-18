<template>
<div class="container">
    <div class="card">
        <div class="row">
            <!-- <aside class="col-sm-5 border-right">
                <article class="gallery-wrap">  -->
                <!-- <div class="img-big-wrap">
                <div><img src="img/vvvvv.jpg"></div>
                </div> -->
                <!-- <div class="img-small-wrap">
                    <div class="item-gallery"> <img src="https://s9.postimg.org/tupxkvfj3/image.jpg"> </div>
                    <div class="item-gallery"> <img src="https://s9.postimg.org/tupxkvfj3/image.jpg"> </div>
                    <div class="item-gallery"> <img src="https://s9.postimg.org/tupxkvfj3/image.jpg"> </div>
                    <div class="item-gallery"> <img src="https://s9.postimg.org/tupxkvfj3/image.jpg"> </div>
                </div> -->
                <!-- </article>
            </aside> -->
            
            <aside class="col-sm-10">
                <article class="card-body p-5">
                    <h3 class="title mb-3">일손을 구합니다 도와주세요ㅠㅠ</h3>

                <p class="price-detail-wrap"> 
                    <span class="price h3 text-warning"> 
                        <span class="currency">일당!!</span><span class="num">시급 10,000</span>
                    </span> 
                    <span>원</span> 
                </p> <!-- price-detail-wrap .// -->
                <dl class="item-property">
                <dt>내용</dt>
                <dd><p>저희 승규네 집은 소도 키우고요 음메~ 유자나무는 아쉽게도 없어요ㅜㅜ 유자나무 사주실래요?ㅎㅎ
                    승규가 일하기 싫다고 도망가서 일할 사람이 필요하답니다 흑흑</p></dd>
                </dl>
                <dl class="param param-feature">
                <dt>지역</dt>
                <dd>전라남도 고흥군</dd>
                </dl>  <!-- item-property-hor .// -->
                <dl class="param param-feature">
                <dt>날짜</dt>
                <dd>언제부터 언제</dd>
                </dl>  <!-- item-property-hor .// -->
                <dl class="param param-feature">
                <dt>인원</dt>
                <dd>2</dd>
                </dl>  <!-- item-property-hor .// -->

                <hr>

                <a href="#" class="btn btn-lg btn-primary text-uppercase"> 수정 </a>
                <a href="#" class="btn btn-lg btn-outline-primary text-uppercase"> 삭제 </a>
                </article> <!-- card-body.// -->
            </aside> <!-- col.// -->
           
        </div> <!-- row.// -->
    </div> <!-- card.// -->


</div>
<!--container.//-->
</template>

<style scoped>
.gallery-wrap .img-big-wrap img {
    height: 450px;
    width: auto;
    display: inline-block;
    cursor: zoom-in;
}


.gallery-wrap .img-small-wrap .item-gallery {
    width: 60px;
    height: 60px;
    border: 1px solid #ddd;
    margin: 7px 2px;
    display: inline-block;
    overflow: hidden;
}

.gallery-wrap .img-small-wrap {
    text-align: center;
}
.gallery-wrap .img-small-wrap img {
    max-width: 100%;
    max-height: 100%;
    object-fit: cover;
    border-radius: 4px;
    cursor: zoom-in;
}
</style>