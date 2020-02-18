<template>
<div class="container my-4" style=" font-family: 'Jua', sans-serif; ">

    <!-- <h1>효진이</h1>
    <h1 class="d-none d-sm-block">바보</h1>
    <hr class="my-4"> -->

    <!--Carousel Wrapper-->
    <div id="multi-item-example" class="carousel slide carousel-multi-item" data-ride="carousel">


      <!--Indicators-->
      <ol class="carousel-indicators">
        <li data-target="#multi-item-example" data-slide-to="0" class="active"></li>
        <li data-target="#multi-item-example" data-slide-to="1"></li>
        <li data-target="#multi-item-example" data-slide-to="2"></li>
      </ol>
      <!--/.Indicators-->

      <!--Slides-->
      <div class="carousel-inner" role="listbox">

        <!--First slide-->
        <div class="carousel-item active">

          <div class="row">

            <div class="col-md-2">
              <div class="card mb-2">
                <img class="card-img-top" src="img/환절기.png" alt="Card image cap">
                <div class="card-body">
                  <!-- <h4 class="card-title" style="text-align:center">난방비</h4> -->
                  <p class="card-text">환절기 뿌리채소로 건강을 챙깁시다.</p>
                  <!-- <a class="btn btn-primary" href = "https://www.nongsaro.go.kr/portal/ps/psv/psvr/psvre/curationDtl.ps?menuId=PS03352&srchCurationNo=1375&pageUnit=6&pageIndex=1&sEraInfo=&sSrchAll=&sKidofcomdtySeCode=&srchStr=&srchAll=Y" >자세히보기</a> -->
                  <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalCenter1"  style="max-width:100%; height:auto;">
                    자세히보기
                  </button>
                  <!-- 모달 -->
                </div>
              </div>
            </div>
         <!-- -------------------------------------------------------- -->

            <div class="col-md-2 clearfix d-none d-md-block">
              <div class="card mb-2">
                <img class="card-img-top" src="img/과수화상병.png"
                  alt="Card image cap">
                <div class="card-body">
                  <p class="card-text">과수화상병 예방은 겨울철 과수원 관리부터</p>
                  <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalCenter2">
                    자세히보기
                  </button> 
                </div>
              </div>
            </div>
         <!-- -------------------------------------------------------- -->


            <div class="col-md-2 clearfix d-none d-md-block">
              <div class="card mb-2">
                <img class="card-img-top" src="img/배.png"
                  alt="Card image cap">
                <div class="card-body">
                  <p class="card-text">빅데이터로 알아본 겨울철 건강 기능성 과일 - 배
                    </p>
                  <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalCenter3">
                    자세히보기
                  </button>
                </div>
              </div>
            </div>
         <!-- -------------------------------------------------------- -->

         <div class="col-md-2 clearfix d-none d-md-block">
              <div class="card mb-2">
                <img class="card-img-top" src="img/국내산.png"
                  alt="Card image cap">
                <div class="card-body">
                  <p class="card-text">국내산으로 둔갑한 중국산 농산물 구별법</p>
                  <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalCenter4">
                    자세히보기
                  </button>
                </div>
              </div>
            </div>
         <!-- -------------------------------------------------------- -->

         <div class="col-md-2 clearfix d-none d-md-block">
              <div class="card mb-2">
                <img class="card-img-top" src="img/농진청검은보리.png"
                  alt="Card image cap">
                <div class="card-body">
                  <p class="card-text">맛은 더하고 카페인은 빼고-농진청 검은보리로 커피 개발</p>
                  <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalCenter5">
                    자세히보기
                  </button>                
                  </div>
              </div>
            </div>
         <!-- -------------------------------------------------------- -->

         <div class="col-md-2 clearfix d-none d-md-block">
              <div class="card mb-2">
                <img class="card-img-top" src="img/생강.png"
                  alt="Card image cap">
                <div class="card-body">
                  <p class="card-text">빅데이터 분석을 통한 겨울철 식탁의 보약 - 생강</p>
                  <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalCenter6">
                    자세히보기
                  </button>
                  </div>
              </div>
            </div>
         <!-- -------------------------------------------------------- -->



          </div>

        </div>
        <!--/.First slide-->

        <!--Second slide-->
        <div class="carousel-item">

          <div class="row">
   
            <div class="col-md-2">
              <div class="card mb-2">
                <img class="card-img-top" src="img/소화장애.png">
                <div class="card-body">
                  <p class="card-text">소화 장애에 특효인 약용작물 삽주(백출)</p>
                  <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalCenter7">
                    자세히보기
                  </button>                
                  </div>
              </div>
            </div>
         <!-- -------------------------------------------------------- -->


            <div class="col-md-2 clearfix d-none d-md-block">
              <div class="card mb-2">
                <img class="card-img-top" src="img/토양검정.png">
                <div class="card-body">
                  <p class="card-text">토양검정은 과학영농의 시작입니다.</p>
                  <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalCenter8">
                    자세히보기
                  </button>                
                  </div>
              </div>
            </div>
      <!-- -------------------------------------------------------- -->


            <div class="col-md-2 clearfix d-none d-md-block">
              <div class="card mb-2">
                <img class="card-img-top" src="img/잎채소.png"
                  alt="Card image cap">
                <div class="card-body">
                  <p class="card-text">추위 잘 견디는‘잎채소’로 겨울 식단 풍성하게</p>
                  <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalCenter9">
                    자세히보기
                  </button>                
                  </div>
              </div>
            </div>
      <!-- -------------------------------------------------------- -->

      <div class="col-md-2 clearfix d-none d-md-block">
              <div class="card mb-2">
                <img class="card-img-top" src="img/난방비.png"
                  alt="Card image cap">
                <div class="card-body">
                  <p class="card-text">(꿀팁) 겨울철 시설하우스 난방비를 줄여 봐요</p>
                  <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalCenter10">
                    자세히보기
                  </button>                
                  </div>
              </div>
            </div>
      <!-- -------------------------------------------------------- -->

      <div class="col-md-2 clearfix d-none d-md-block">
              <div class="card mb-2">
                <img class="card-img-top" src="img/농기계.png"
                  alt="Card image cap">
                <div class="card-body">
                  <p class="card-text">농기계 수명 겨울철 관리가 좌우</p>
                  <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalCenter11">
                    자세히보기
                  </button>                
                  </div>
              </div>
            </div>
      <!-- -------------------------------------------------------- -->

      <div class="col-md-2 clearfix d-none d-md-block">
              <div class="card mb-2">
                <img class="card-img-top" src="img/농업인.png"
                  alt="Card image cap">
                <div class="card-body">
                  <p class="card-text">올 농사의 첫걸음 새해 농업인 실용교육</p>
                  <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalCenter12">
                    자세히보기
                  </button>                
                  </div>
              </div>
            </div>
      <!-- -------------------------------------------------------- -->

          </div>

        </div>
        <!--/.Second slide-->

        <!--Third slide-->
        <div class="carousel-item">

          <div class="row">
      
            <div class="col-md-2">
              <div class="card mb-2">
                <img class="card-img-top" src="img/소.png"
                  alt="Card image cap">
                <div class="card-body">
                  <p class="card-text">소·돼지·닭의 건강한 겨울나기</p>
                  <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalCenter13">
                    자세히보기
                  </button>                
                  </div>
              </div>
            </div>
      <!-- -------------------------------------------------------- -->


            <div class="col-md-2 clearfix d-none d-md-block">
              <div class="card mb-2">
                <img class="card-img-top" src="img/소득조사.png"
                  alt="Card image cap">
                <div class="card-body">
                  <p class="card-text">농산물 소득조사 결과 가장 소득이 높은 작물은?</p>
                  <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalCenter14">
                    자세히보기
                  </button>                
                  </div>
              </div>
            </div>
      <!-- -------------------------------------------------------- -->


            <div class="col-md-2 clearfix d-none d-md-block">
              <div class="card mb-2">
                <img class="card-img-top" src="img/시래기.png"
                  alt="Card image cap">
                <div class="card-body">
                  <p class="card-text">겨울철 식탁 위의 건강지킴이 “시래기”</p>
                  <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalCenter15">
                    자세히보기
                  </button>                
                  </div>
              </div>
            </div>
      <!-- -------------------------------------------------------- -->

      <div class="col-md-2 clearfix d-none d-md-block">
              <div class="card mb-2">
                <img class="card-img-top" src="img/시설재배지.png"
                  alt="Card image cap">
                <div class="card-body">
                  <p class="card-text">시설재배지 염류장해 고민 킬레이트제로 해결전체목록</p>
                  <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalCenter16">
                    자세히보기
                  </button>                
                  </div>
              </div>
            </div>
      <!-- -------------------------------------------------------- -->

      <div class="col-md-2 clearfix d-none d-md-block">
              <div class="card mb-2">
                <img class="card-img-top" src="img/초보농업인.png"
                  alt="Card image cap">
                <div class="card-body">
                  <p class="card-text">(꿀팁) 초보 창업 농업인이 스마트팜 사장님이 되는 비결</p>
                  <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalCenter17">
                    자세히보기
                  </button>                
                  </div>
              </div>
            </div>
      <!-- -------------------------------------------------------- -->

      <div class="col-md-2 clearfix d-none d-md-block">
              <div class="card mb-2">
                <img class="card-img-top" src="img/토마토.png"
                  alt="Card image cap">
                <div class="card-body">
                  <p class="card-text">겨울철 시설토마토를 말려 죽이는 잎마름역병</p>
                  <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalCenter18">
                    자세히보기
                  </button>                
                  </div>
              </div>
            </div>
      <!-- -------------------------------------------------------- -->   

          </div>

        </div>
        <!--/.Third slide-->

      </div>
      <!--/.Slides-->

    </div>
    <!--/.Carousel Wrapper-->
<!--Controls-->
      <div class="controls-top" style="text-align:center">
        <a class="btn-floating" href="#multi-item-example" data-slide="prev"><img src="img/left-arrow.png" class="fa fa-chevron-left" style="width:5%;"></a>
        <a class="btn-floating" href="#multi-item-example" data-slide="next"><img  src="img/right-arrow.png" class="fa fa-chevron-right" style="width:5%;"></a>
      </div>
      <!--/.Controls-->
      
      <!-- 모달 -->
      <div class="modal fade bd-example-modal-xl"  id="exampleModalCenter1" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabe" aria-hidden="true">
        <div class="modal-dialog modal-xl" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalCenterTitle">Modal title</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body" style="text-align: center;">
              <img src="img/number1-cont.png" style="max-width:100%; height:auto;">
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div> 
      <!-- 모달end -->
      <!-- 모달 -->
      <div class="modal fade bd-example-modal-xl"  id="exampleModalCenter2" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabe" aria-hidden="true">
        <div class="modal-dialog modal-xl" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalCenterTitle">Modal title</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body" style="text-align: center;">
              <img src="img/number2-cont.png" style="max-width:100%; height:auto;">
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div> 
      <!-- 모달end -->
      <!-- 모달 -->
      <div class="modal fade bd-example-modal-xl"  id="exampleModalCenter3" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabe" aria-hidden="true">
        <div class="modal-dialog modal-xl" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalCenterTitle">Modal title</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body" style="text-align: center;">
              <img src="img/number3-cont.png" style="max-width:100%; height:auto;">
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div> 
      <!-- 모달end -->
      <!-- 모달 -->
      <div class="modal fade bd-example-modal-xl"  id="exampleModalCenter4" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabe" aria-hidden="true">
        <div class="modal-dialog modal-xl" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalCenterTitle">Modal title</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body" style="text-align: center;">
              <img src="img/number4-cont.png" style="max-width:100%; height:auto;">
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div> 
      <!-- 모달end -->
      <!-- 모달 -->
      <div class="modal fade bd-example-modal-xl"  id="exampleModalCenter5" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabe" aria-hidden="true">
        <div class="modal-dialog modal-xl" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalCenterTitle">Modal title</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body" style="text-align: center;">
              <img src="img/number5-cont.png" style="max-width:100%; height:auto;">
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div> 
      <!-- 모달end -->
      <!-- 모달 -->
      <div class="modal fade bd-example-modal-xl"  id="exampleModalCenter6" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabe" aria-hidden="true">
        <div class="modal-dialog modal-xl" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalCenterTitle">Modal title</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body" style="text-align: center;">
              <img src="img/number6-cont.png" style="max-width:100%; height:auto;">
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div> 
      <!-- 모달end -->
      <!-- 모달 -->
      <div class="modal fade bd-example-modal-xl"  id="exampleModalCenter7" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabe" aria-hidden="true">
        <div class="modal-dialog modal-xl" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalCenterTitle">Modal title</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body" style="text-align: center;">
              <img src="img/number7-cont.png" style="max-width:100%; height:auto;">
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div> 
      <!-- 모달end -->
      <!-- 모달 -->
      <div class="modal fade bd-example-modal-xl"  id="exampleModalCenter8" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabe" aria-hidden="true">
        <div class="modal-dialog modal-xl" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalCenterTitle">Modal title</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body" style="text-align: center;">
              <img src="img/number8-cont.png" style="max-width:100%; height:auto;">
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div> 
      <!-- 모달end -->
      <!-- 모달 -->
      <div class="modal fade bd-example-modal-xl"  id="exampleModalCenter9" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabe" aria-hidden="true">
        <div class="modal-dialog modal-xl" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalCenterTitle">Modal title</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body" style="text-align: center;">
              <img src="img/number9-cont.png" style="max-width:100%; height:auto;">
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div> 
      <!-- 모달end -->
      <!-- 모달 -->
      <div class="modal fade bd-example-modal-xl"  id="exampleModalCenter10" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabe" aria-hidden="true">
        <div class="modal-dialog modal-xl" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalCenterTitle">Modal title</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body" style="text-align: center;">
              <img src="img/number10-cont.png" style="max-width:100%; height:auto;">
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div> 
      <!-- 모달end -->
      <!-- 모달 -->
      <div class="modal fade bd-example-modal-xl"  id="exampleModalCenter11" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabe" aria-hidden="true">
        <div class="modal-dialog modal-xl" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalCenterTitle">Modal title</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body" style="text-align: center;">
              <img src="img/number11-cont.png" style="max-width:100%; height:auto;">
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div> 
      <!-- 모달end -->
      <!-- 모달 -->
      <div class="modal fade bd-example-modal-xl"  id="exampleModalCenter12" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabe" aria-hidden="true">
        <div class="modal-dialog modal-xl" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalCenterTitle">Modal title</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body" style="text-align: center;">
              <img src="img/number12-cont.png" style="max-width:100%; height:auto;">
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div> 
      <!-- 모달end -->
      <!-- 모달 -->
      <div class="modal fade bd-example-modal-xl"  id="exampleModalCenter13" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabe" aria-hidden="true">
        <div class="modal-dialog modal-xl" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalCenterTitle">Modal title</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body" style="text-align: center;">
              <img src="img/number13-cont.png" style="max-width:100%; height:auto;">
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div> 
      <!-- 모달end -->
      <!-- 모달 -->
      <div class="modal fade bd-example-modal-xl"  id="exampleModalCenter14" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabe" aria-hidden="true">
        <div class="modal-dialog modal-xl" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalCenterTitle">Modal title</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body" style="text-align: center;">
              <img src="img/number14-cont.png" style="max-width:100%; height:auto;">
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div> 
      <!-- 모달end -->
      <!-- 모달 -->
      <div class="modal fade bd-example-modal-xl"  id="exampleModalCenter15" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabe" aria-hidden="true">
        <div class="modal-dialog modal-xl" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalCenterTitle">Modal title</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body" style="text-align: center;">
              <img src="img/number15-cont.png" style="max-width:100%; height:auto;">
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div> 
      <!-- 모달end -->
      <!-- 모달 -->
      <div class="modal fade bd-example-modal-xl"  id="exampleModalCenter16" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabe" aria-hidden="true">
        <div class="modal-dialog modal-xl" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalCenterTitle">Modal title</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body" style="text-align: center;">
              <img src="img/number16-cont.png" style="max-width:100%; height:auto;">
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div> 
      <!-- 모달end -->
      <!-- 모달 -->
      <div class="modal fade bd-example-modal-xl"  id="exampleModalCenter17" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabe" aria-hidden="true">
        <div class="modal-dialog modal-xl" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalCenterTitle">Modal title</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body" style="text-align: center;">
              <img src="img/number17-cont.png" style="max-width:100%; height:auto;">
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div> 
      <!-- 모달end -->
      <!-- 모달 -->
      <div class="modal fade bd-example-modal-xl"  id="exampleModalCenter18" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabe" aria-hidden="true">
        <div class="modal-dialog modal-xl" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalCenterTitle">Modal title</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body" style="text-align: center;">
              <img src="img/number18-cont.png" style="max-width:100%; height:auto;">
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div> 
      <!-- 모달end -->
  </div>
</template>

<style scoped>
.btn.btn-primary{
   text-align:center;
   background-color: rgb(218, 216, 216);
   border: none;
   color:black;
   font-family: 'Jua', sans-serif;
}
.card-text{
   overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 2; 
    -webkit-box-orient: vertical;
}

</style>