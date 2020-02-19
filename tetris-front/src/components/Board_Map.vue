<template>
    <div class="container">
          <div id="map" style="width:auto;height:400px;"></div>
    </div>
</template>

<script>
import axios from 'axios';
const kakao = window.kakao
const imageSrc = "http://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png"; 

export default {
    data(){
      return {
                totallist: [],
                locationinfo: [
                                {
                                    name: "서울특별시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.566609, 126.978423)
                                },
                                {
                                    name: "광주광역시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.159998, 126.851465)
                                },
                                {
                                    name: "대구광역시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.871451, 128.601672)
                                },
                                {
                                    name: "대전광역시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.350413, 127.384840)
                                },
                                {
                                    name: "부산광역시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.179719, 129.075091)
                                },
                                {
                                    name: "인천광역시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.455909, 126.705524)
                                },
                                {
                                    name: "울산광역시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.539631, 129.311489)
                                },
                                {
                                    name: "거제시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(34.880703, 128.621142)
                                },
                                {
                                    name: "김해시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.228567, 128.889274)
                                },
                                {
                                    name: "밀양시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.503868, 128.746554)
                                },
                                {
                                    name: "사천시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.003761, 128.064184)
                                },
                                {
                                    name: "양산시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.335107, 129.037055)
                                },
                                {
                                    name: "진주시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.180367, 128.108749)
                                },
                                {
                                    name: "창원시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.227957, 128.681863)
                                },
                                {
                                    name: "통영시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(34.854436, 128.433214)
                                },
                                {
                                    name: "거창군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.686626, 127.909515)
                                },
                                {
                                    name: "고성군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(34.972988, 128.322239)
                                },
                                {
                                    name: "남해군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(34.837730, 127.892526)
                                },
                                {
                                    name: "산청군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.415605, 127.873497)
                                },
                                {
                                    name: "의령군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.322155, 128.261763)
                                },
                                {
                                    name: "창녕군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.544540, 128.492285)
                                },
                                {
                                    name: "하동군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.067202, 127.751226)
                                },
                                {
                                    name: "함안군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.272520, 128.406481)
                                },
                                {
                                    name: "함양군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.520580, 127.725187)
                                },
                                {
                                    name: "합천군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.566623, 128.165871)
                                },
                                {
                                    name: "경산시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.825048, 128.741511)
                                },
                                {
                                    name: "경주시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.856215, 129.224760)
                                },
                                {
                                    name: "구미시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.119616, 128.344295)
                                },
                                {
                                    name: "김천시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.139893, 128.113704)
                                },
                                {
                                    name: "문경시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.586447, 128.186801)
                                },
                                {
                                    name: "상주시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.410923, 128.158992)
                                },
                                {
                                    name: "안동시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.568388, 128.729533)
                                },
                                {
                                    name: "영주시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.805718, 128.623992)
                                },
                                {
                                    name: "영천시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.973272, 128.938540)
                                },
                                {
                                    name: "포항시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.019203, 129.343466)
                                },
                                {
                                    name: "고령군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.726124, 128.262996)
                                },
                                {
                                    name: "군위군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.242988, 128.572926)
                                },
                                {
                                    name: "봉화군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.893145, 128.732548)
                                },
                                {
                                    name: "성주군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.919204, 128.283027)
                                },
                                {
                                    name: "영덕군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.415153, 129.366073)
                                },
                                {
                                    name: "영양군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.666664, 129.112423)
                                },
                                {
                                    name: "예천군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.646750, 128.437416)
                                },
                                {
                                    name: "울릉군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.484435, 130.905901)
                                },
                                {
                                    name: "울진군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.993067, 129.400629)
                                },
                                {
                                    name: "의성군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.352739, 128.696981)
                                },
                                {
                                    name: "청도군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.647384, 128.734394)
                                },
                                {
                                    name: "청송군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.436251, 129.057144)
                                },
                                {
                                    name: "칠곡군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.995564, 128.401685)
                                },
                                {
                                    name: "광양시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(34.940701, 127.696006)
                                },
                                {
                                    name: "나주시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.015875, 126.710911)
                                },
                                {
                                    name: "목포시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(34.811820, 126.392177)
                                },
                                {
                                    name: "순천시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(34.950647, 127.487331)
                                },
                                {
                                    name: "여수시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(34.760431, 127.662287)
                                },
                                {
                                    name: "강진군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(34.642059, 126.767267)
                                },
                                {
                                    name: "고흥군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(34.611245, 127.285057)
                                },
                                {
                                    name: "곡성군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.282072, 127.292099)
                                },
                                {
                                    name: "구례군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.202506, 127.462764)
                                },
                                {
                                    name: "담양군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.321249, 126.988283)
                                },
                                {
                                    name: "무안군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(34.990491, 126.481674)
                                },
                                {
                                    name: "보성군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(34.771446, 127.080100)
                                },
                                {
                                    name: "신안군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(34.833352, 126.351379)
                                },
                                {
                                    name: "영광군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.277172, 126.512109)
                                },
                                {
                                    name: "영암군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(34.800174, 126.696857)
                                },
                                {
                                    name: "완도군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(34.310980, 126.755069)
                                },
                                {
                                    name: "장성군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.301848, 126.784913)
                                },
                                {
                                    name: "장흥군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(34.681629, 126.907080)
                                },
                                {
                                    name: "진도군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(34.486863, 126.263508)
                                },
                                {
                                    name: "함평군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.065930, 126.516626)
                                },
                                {
                                    name: "해남군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(34.573387, 126.599218)
                                },
                                {
                                    name: "화순군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.064492, 126.986657)
                                },
                                {
                                    name: "군산시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.967704, 126.736820)
                                },
                                {
                                    name: "김제시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.803535, 126.880569)
                                },
                                {
                                    name: "남원시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.416401, 127.390373)
                                },
                                {
                                    name: "익산시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.948273, 126.957718)
                                },
                                {
                                    name: "전주시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.824175, 127.147994)
                                },
                                {
                                    name: "정읍시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.569885, 126.856057)
                                },
                                {
                                    name: "고창군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.435811, 126.702139)
                                },
                                {
                                    name: "무주군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.006845, 127.660808)
                                },
                                {
                                    name: "부안군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.731791, 126.733498)
                                },
                                {
                                    name: "순창군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.374407, 127.137619)
                                },
                                {
                                    name: "완주군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.904702, 127.162247)
                                },
                                {
                                    name: "임실군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.617821, 127.289126)
                                },
                                {
                                    name: "장수군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.647322, 127.521252)
                                },
                                {
                                    name: "진안군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(35.791756, 127.424924)
                                },
                                {
                                    name: "계룡시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.274575, 127.248601)
                                },
                                {
                                    name: "공주시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.446625, 127.118989)
                                },
                                {
                                    name: "논산시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.187082, 127.098719)
                                },
                                {
                                    name: "당진시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.889955, 126.645810)
                                },
                                {
                                    name: "보령시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.333498, 126.612829)
                                },
                                {
                                    name: "서산시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.784850, 126.450309)
                                },
                                {
                                    name: "아산시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.789852, 127.002588)
                                },
                                {
                                    name: "천안시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.815129, 127.113915)
                                },
                                {
                                    name: "금산군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.108867, 127.488116)
                                },
                                {
                                    name: "부여군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.275796, 126.909843)
                                },
                                {
                                    name: "서천군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.080404, 126.691762)
                                },
                                {
                                    name: "예산군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.682632, 126.848773)
                                },
                                {
                                    name: "청양군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.459192, 126.802238)
                                },
                                {
                                    name: "태안군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.745596, 126.298158)
                                },
                                {
                                    name: "홍성군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.601303, 126.660804)
                                },
                                {
                                    name: "제천시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.132676, 128.190959)
                                },
                                {
                                    name: "청주시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.641884, 127.488779)
                                },
                                {
                                    name: "충주시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.991025, 127.925916)
                                },
                                {
                                    name: "괴산군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.815404, 127.786705)
                                },
                                {
                                    name: "단양군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.984702, 128.365431)
                                },
                                {
                                    name: "보은군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.489430, 127.729504)
                                },
                                {
                                    name: "영동군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.175075, 127.783366)
                                },
                                {
                                    name: "옥천군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.306402, 127.571271)
                                },
                                {
                                    name: "음성군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.940235, 127.690480)
                                },
                                {
                                    name: "증평군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.785505, 127.581499)
                                },
                                {
                                    name: "진천군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.855380, 127.435639)
                                },
                                {
                                    name: "강릉시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.752149, 128.875974)
                                },
                                {
                                    name: "동해시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.524692, 129.114324)
                                },
                                {
                                    name: "삼척시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.449946, 129.165153)
                                },
                                {
                                    name: "속초시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(38.207009, 128.591884)
                                },
                                {
                                    name: "원주시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.342034, 127.919710)
                                },
                                {
                                    name: "춘천시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.881319, 127.730044)
                                },
                                {
                                    name: "태백시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.164140, 128.985749)
                                },
                                {
                                    name: "고성군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(34.973035, 128.322245)
                                },
                                {
                                    name: "양구군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(38.109955, 127.989913)
                                },
                                {
                                    name: "양양군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(38.075451, 128.619010)
                                },
                                {
                                    name: "영월군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.183752, 128.461740)
                                },
                                {
                                    name: "인제군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(38.069710, 128.170236)
                                },
                                {
                                    name: "정선군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.380587, 128.660908)
                                },
                                {
                                    name: "철원군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(38.146709, 127.313435)
                                },
                                {
                                    name: "평창군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.370767, 128.390327)
                                },
                                {
                                    name: "홍천군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.697078, 127.888854)
                                },
                                {
                                    name: "화천군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(38.106183, 127.708120)
                                },
                                {
                                    name: "횡성군",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.491703, 127.985047)
                                },
                                {
                                    name: "고양시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.658373, 126.831941)
                                },
                                {
                                    name: "과천시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.429188, 126.987630)
                                },
                                {
                                    name: "광명시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.478669, 126.864675)
                                },
                                {
                                    name: "광주시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.429493, 127.255131)
                                },
                                {
                                    name: "구리시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.594457, 127.129711)
                                },
                                {
                                    name: "군포시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.361657, 126.935207)
                                },
                                {
                                    name: "김포시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.615238, 126.715655)
                                },
                                {
                                    name: "남양주시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.636039, 127.216532)
                                },
                                {
                                    name: "동두천시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.903604, 127.060375)
                                },
                                {
                                    name: "부천시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.503573, 126.765961)
                                },
                                {
                                    name: "성남시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.420065, 127.126669)
                                },
                                {
                                    name: "수원시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.263384, 127.028560)
                                },
                                {
                                    name: "시흥시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.380127, 126.802870)
                                },
                                {
                                    name: "안산시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.321886, 126.830914)
                                },
                                {
                                    name: "안성시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.008085, 127.279860)
                                },
                                {
                                    name: "안양시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.394230, 126.956792)
                                },
                                {
                                    name: "양주시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.785321, 127.045736)
                                },
                                {
                                    name: "여주시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.298251, 127.637277)
                                },
                                {
                                    name: "오산시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.149862, 127.077471)
                                },
                                {
                                    name: "용인시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.241096, 127.177899)
                                },
                                {
                                    name: "의왕시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.344737, 126.968250)
                                },
                                {
                                    name: "의정부시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.738122, 127.033756)
                                },
                                {
                                    name: "이천시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.272288, 127.435012)
                                },
                                {
                                    name: "파주시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.759913, 126.779893)
                                },
                                {
                                    name: "평택시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(36.992323, 127.112688)
                                },
                                {
                                    name: "포천시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.894971, 127.200406)
                                },
                                {
                                    name: "하남시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.539346, 127.214943)
                                },
                                {
                                    name: "화성시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(37.199490, 126.831667)
                                },
                                {
                                    name: "서귀포시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(33.253932, 126.559618)
                                },
                                {
                                    name: "제주시",
                                    number: 0,
                                    latlng: new kakao.maps.LatLng(33.499603, 126.531255)
                                }

                            ]
               }
   },
   methods:{
       mapLoad(){
           var mapContainer = document.getElementById("map") 
                       var mapOption = {
                                           center : new kakao.maps.LatLng(35.950701, 127.870667),
                                           level : 12
                                       };
                       this.map = new kakao.maps.Map(mapContainer, mapOption)
                       this.zoomControl = new kakao.maps.ZoomControl();
                       this.map.addControl(this.zoomControl, kakao.maps.ControlPosition.RIGHT);
           
                       for (var i = 0; i < this.locationinfo.length; i ++) {
                                       this.imageSize = new kakao.maps.Size(24, 35); 
                                       this.markerImage = new kakao.maps.MarkerImage(imageSrc, this.imageSize); 
                                       // 마커를 생성합니다
                                       this.marker = new kakao.maps.Marker({
                                           map: this.map, // 마커를 표시할 지도
                                           position: this.locationinfo[i].latlng, // 마커를 표시할 위치
                                           title : this.locationinfo[i]['number'] + "팀",  // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
                                           image : this.markerImage // 마커 이미지 
                                       });
                                   }
              },
       },
    mounted(){
        axios.get('http://15.165.77.204:8000/helppage/gethelp/')
                    .then(res => {
                            this.totallist = res.data;
                            for (var i = 0; i < this.totallist.length; i ++){
                                if (this.totallist[i].location1 === "서울특별시"){
                                    this.locationinfo[0]['number'] += 1 
                                    } else if (this.totallist[i].location1 === "광주광역시"){
                                    this.locationinfo[1]['number'] += 1
                                    } else if (this.totallist[i].location1 === "대구광역시"){
                                    this.locationinfo[2]['number'] += 1
                                    } else if (this.totallist[i].location1 === "대전광역시"){
                                    this.locationinfo[3]['number'] += 1
                                    } else if (this.totallist[i].location1 === "부산광역시"){
                                    this.locationinfo[4]['number'] += 1
                                    } else if (this.totallist[i].location1 === "인천광역시"){
                                    this.locationinfo[5]['number'] += 1
                                    } else if (this.totallist[i].location1 === "울산광역시"){
                                    this.locationinfo[6]['number'] += 1
                                    } else if (this.totallist[i].location2 === "거제시"){
                                    this.locationinfo[7]['number'] += 1
                                    } else if (this.totallist[i].location2 === "김해시"){
                                    this.locationinfo[8]['number'] += 1
                                    } else if (this.totallist[i].location2 === "밀양시"){
                                    this.locationinfo[9]['number'] += 1
                                    } else if (this.totallist[i].location2 === "사천시"){
                                    this.locationinfo[10]['number'] += 1
                                    } else if (this.totallist[i].location2 === "양산시"){
                                    this.locationinfo[11]['number'] += 1
                                    } else if (this.totallist[i].location2 === "진주시"){
                                    this.locationinfo[12]['number'] += 1
                                    } else if (this.totallist[i].location2 === "창원시"){
                                    this.locationinfo[13]['number'] += 1
                                    } else if (this.totallist[i].location2 === "통영시"){
                                    this.locationinfo[14]['number'] += 1
                                    } else if (this.totallist[i].location2 === "거창군"){
                                    this.locationinfo[15]['number'] += 1
                                    } else if (this.totallist[i].location2 === "고성군"){
                                    this.locationinfo[16]['number'] += 1
                                    } else if (this.totallist[i].location2 === "남해군"){
                                    this.locationinfo[17]['number'] += 1
                                    } else if (this.totallist[i].location2 === "산청군"){
                                    this.locationinfo[18]['number'] += 1
                                    } else if (this.totallist[i].location2 === "의령군"){
                                    this.locationinfo[19]['number'] += 1
                                    } else if (this.totallist[i].location2 === "창녕군"){
                                    this.locationinfo[20]['number'] += 1
                                    } else if (this.totallist[i].location2 === "하동군"){
                                    this.locationinfo[21]['number'] += 1
                                    } else if (this.totallist[i].location2 === "함안군"){
                                    this.locationinfo[22]['number'] += 1
                                    } else if (this.totallist[i].location2 === "함양군"){
                                    this.locationinfo[23]['number'] += 1
                                    } else if (this.totallist[i].location2 === "합천군"){
                                    this.locationinfo[24]['number'] += 1
                                    } else if (this.totallist[i].location2 === "경산시"){
                                    this.locationinfo[25]['number'] += 1
                                    } else if (this.totallist[i].location2 === "경주시"){
                                    this.locationinfo[26]['number'] += 1
                                    } else if (this.totallist[i].location2 === "구미시"){
                                    this.locationinfo[27]['number'] += 1
                                    } else if (this.totallist[i].location2 === "김천시"){
                                    this.locationinfo[28]['number'] += 1
                                    } else if (this.totallist[i].location2 === "문경시"){
                                    this.locationinfo[29]['number'] += 1
                                    } else if (this.totallist[i].location2 === "상주시"){
                                    this.locationinfo[30]['number'] += 1
                                    } else if (this.totallist[i].location2 === "안동시"){
                                    this.locationinfo[31]['number'] += 1
                                    } else if (this.totallist[i].location2 === "영주시"){
                                    this.locationinfo[32]['number'] += 1
                                    } else if (this.totallist[i].location2 === "영천시"){
                                    this.locationinfo[33]['number'] += 1
                                    } else if (this.totallist[i].location2 === "포항시"){
                                    this.locationinfo[34]['number'] += 1
                                    } else if (this.totallist[i].location2 === "고령군"){
                                    this.locationinfo[35]['number'] += 1
                                    } else if (this.totallist[i].location2 === "군위군"){
                                    this.locationinfo[36]['number'] += 1
                                    } else if (this.totallist[i].location2 === "봉화군"){
                                    this.locationinfo[37]['number'] += 1
                                    } else if (this.totallist[i].location2 === "성주군"){
                                    this.locationinfo[38]['number'] += 1
                                    } else if (this.totallist[i].location2 === "영덕군"){
                                    this.locationinfo[39]['number'] += 1
                                    } else if (this.totallist[i].location2 === "영양군"){
                                    this.locationinfo[40]['number'] += 1
                                    } else if (this.totallist[i].location2 === "예천군"){
                                    this.locationinfo[41]['number'] += 1
                                    } else if (this.totallist[i].location2 === "울릉군"){
                                    this.locationinfo[42]['number'] += 1
                                    } else if (this.totallist[i].location2 === "울진군"){
                                    this.locationinfo[43]['number'] += 1
                                    } else if (this.totallist[i].location2 === "의성군"){
                                    this.locationinfo[44]['number'] += 1
                                    } else if (this.totallist[i].location2 === "청도군"){
                                    this.locationinfo[45]['number'] += 1
                                    } else if (this.totallist[i].location2 === "청송군"){
                                    this.locationinfo[46]['number'] += 1
                                    } else if (this.totallist[i].location2 === "칠곡군"){
                                    this.locationinfo[47]['number'] += 1
                                    } else if (this.totallist[i].location2 === "광양시"){
                                    this.locationinfo[48]['number'] += 1
                                    } else if (this.totallist[i].location2 === "나주시"){
                                    this.locationinfo[49]['number'] += 1
                                    } else if (this.totallist[i].location2 === "나주시"){
                                    this.locationinfo[50]['number'] += 1
                                    } else if (this.totallist[i].location2 === "순천시"){
                                    this.locationinfo[51]['number'] += 1
                                    } else if (this.totallist[i].location2 === "여수시"){
                                    this.locationinfo[52]['number'] += 1
                                    } else if (this.totallist[i].location2 === "강진군"){
                                    this.locationinfo[53]['number'] += 1
                                    } else if (this.totallist[i].location2 === "고흥군"){
                                    this.locationinfo[54]['number'] += 1
                                    } else if (this.totallist[i].location2 === "곡성군"){
                                    this.locationinfo[55]['number'] += 1
                                    } else if (this.totallist[i].location2 === "구례군"){
                                    this.locationinfo[56]['number'] += 1
                                    } else if (this.totallist[i].location2 === "담양군"){
                                    this.locationinfo[57]['number'] += 1
                                    } else if (this.totallist[i].location2 === "무안군"){
                                    this.locationinfo[58]['number'] += 1
                                    } else if (this.totallist[i].location2 === "보성군"){
                                    this.locationinfo[59]['number'] += 1
                                    } else if (this.totallist[i].location2 === "신안군"){
                                    this.locationinfo[60]['number'] += 1
                                    } else if (this.totallist[i].location2 === "영광군"){
                                    this.locationinfo[61]['number'] += 1
                                    } else if (this.totallist[i].location2 === "영암군"){
                                    this.locationinfo[62]['number'] += 1
                                    } else if (this.totallist[i].location2 === "완도군"){
                                    this.locationinfo[63]['number'] += 1
                                    } else if (this.totallist[i].location2 === "장성군"){
                                    this.locationinfo[64]['number'] += 1
                                    } else if (this.totallist[i].location2 === "장흥군"){
                                    this.locationinfo[65]['number'] += 1
                                    } else if (this.totallist[i].location2 === "진도군"){
                                    this.locationinfo[66]['number'] += 1
                                    } else if (this.totallist[i].location2 === "함평군"){
                                    this.locationinfo[67]['number'] += 1
                                    } else if (this.totallist[i].location2 === "해남군"){
                                    this.locationinfo[68]['number'] += 1
                                    } else if (this.totallist[i].location2 === "화순군"){
                                    this.locationinfo[69]['number'] += 1
                                    } else if (this.totallist[i].location2 === "군산시"){
                                    this.locationinfo[70]['number'] += 1
                                    } else if (this.totallist[i].location2 === "김제시"){
                                    this.locationinfo[71]['number'] += 1
                                    } else if (this.totallist[i].location2 === "남원시"){
                                    this.locationinfo[72]['number'] += 1
                                    } else if (this.totallist[i].location2 === "익산시"){
                                    this.locationinfo[73]['number'] += 1
                                    } else if (this.totallist[i].location2 === "전주시"){
                                    this.locationinfo[74]['number'] += 1
                                    } else if (this.totallist[i].location2 === "정읍시"){
                                    this.locationinfo[75]['number'] += 1
                                    } else if (this.totallist[i].location2 === "고창군"){
                                    this.locationinfo[76]['number'] += 1
                                    } else if (this.totallist[i].location2 === "무주군"){
                                    this.locationinfo[77]['number'] += 1
                                    } else if (this.totallist[i].location2 === "부안군"){
                                    this.locationinfo[78]['number'] += 1
                                    } else if (this.totallist[i].location2 === "순창군"){
                                    this.locationinfo[79]['number'] += 1
                                    } else if (this.totallist[i].location2 === "완주군"){
                                    this.locationinfo[80]['number'] += 1
                                    } else if (this.totallist[i].location2 === "임실군"){
                                    this.locationinfo[81]['number'] += 1
                                    } else if (this.totallist[i].location2 === "장수군"){
                                    this.locationinfo[82]['number'] += 1
                                    } else if (this.totallist[i].location2 === "진안군"){
                                    this.locationinfo[83]['number'] += 1
                                    } else if (this.totallist[i].location2 === "계룡시"){
                                    this.locationinfo[84]['number'] += 1
                                    } else if (this.totallist[i].location2 === "공주시"){
                                    this.locationinfo[85]['number'] += 1
                                    } else if (this.totallist[i].location2 === "논산시"){
                                    this.locationinfo[86]['number'] += 1
                                    } else if (this.totallist[i].location2 === "당진시"){
                                    this.locationinfo[87]['number'] += 1
                                    } else if (this.totallist[i].location2 === "보령시"){
                                    this.locationinfo[88]['number'] += 1
                                    } else if (this.totallist[i].location2 === "서산시"){
                                    this.locationinfo[89]['number'] += 1
                                    } else if (this.totallist[i].location2 === "아산시"){
                                    this.locationinfo[90]['number'] += 1
                                    } else if (this.totallist[i].location2 === "천안시"){
                                    this.locationinfo[91]['number'] += 1
                                    } else if (this.totallist[i].location2 === "금산군"){
                                    this.locationinfo[92]['number'] += 1
                                    } else if (this.totallist[i].location2 === "부여군"){
                                    this.locationinfo[93]['number'] += 1
                                    } else if (this.totallist[i].location2 === "서천군"){
                                    this.locationinfo[94]['number'] += 1
                                    } else if (this.totallist[i].location2 === "예산군"){
                                    this.locationinfo[95]['number'] += 1
                                    } else if (this.totallist[i].location2 === "청양군"){
                                    this.locationinfo[96]['number'] += 1
                                    } else if (this.totallist[i].location2 === "태안군"){
                                    this.locationinfo[97]['number'] += 1
                                    } else if (this.totallist[i].location2 === "홍성군"){
                                    this.locationinfo[98]['number'] += 1
                                    } else if (this.totallist[i].location2 === "제천시"){
                                    this.locationinfo[99]['number'] += 1
                                    } else if (this.totallist[i].location2 === "청주시"){
                                    this.locationinfo[100]['number'] += 1
                                    } else if (this.totallist[i].location2 === "충주시"){
                                    this.locationinfo[101]['number'] += 1
                                    } else if (this.totallist[i].location2 === "괴산군"){
                                    this.locationinfo[102]['number'] += 1
                                    } else if (this.totallist[i].location2 === "단양군"){
                                    this.locationinfo[103]['number'] += 1
                                    } else if (this.totallist[i].location2 === "보은군"){
                                    this.locationinfo[104]['number'] += 1
                                    } else if (this.totallist[i].location2 === "영동군"){
                                    this.locationinfo[105]['number'] += 1
                                    } else if (this.totallist[i].location2 === "옥천군"){
                                    this.locationinfo[106]['number'] += 1
                                    } else if (this.totallist[i].location2 === "음성군"){
                                    this.locationinfo[107]['number'] += 1
                                    } else if (this.totallist[i].location2 === "증평군"){
                                    this.locationinfo[108]['number'] += 1
                                    } else if (this.totallist[i].location2 === "진천군"){
                                    this.locationinfo[109]['number'] += 1
                                    } else if (this.totallist[i].location2 === "강릉시"){
                                    this.locationinfo[110]['number'] += 1
                                    } else if (this.totallist[i].location2 === "동해시"){
                                    this.locationinfo[111]['number'] += 1
                                    } else if (this.totallist[i].location2 === "삼척시"){
                                    this.locationinfo[112]['number'] += 1
                                    } else if (this.totallist[i].location2 === "속초시"){
                                    this.locationinfo[113]['number'] += 1
                                    } else if (this.totallist[i].location2 === "원주시"){
                                    this.locationinfo[114]['number'] += 1
                                    } else if (this.totallist[i].location2 === "춘천시"){
                                    this.locationinfo[115]['number'] += 1
                                    } else if (this.totallist[i].location2 === "태백시"){
                                    this.locationinfo[116]['number'] += 1
                                    } else if (this.totallist[i].location2 === "고성군"){
                                    this.locationinfo[117]['number'] += 1
                                    } else if (this.totallist[i].location2 === "양구군"){
                                    this.locationinfo[118]['number'] += 1
                                    } else if (this.totallist[i].location2 === "양양군"){
                                    this.locationinfo[119]['number'] += 1
                                    } else if (this.totallist[i].location2 === "영월군"){
                                    this.locationinfo[120]['number'] += 1
                                    } else if (this.totallist[i].location2 === "인제군"){
                                    this.locationinfo[121]['number'] += 1
                                    } else if (this.totallist[i].location2 === "정선군"){
                                    this.locationinfo[122]['number'] += 1
                                    } else if (this.totallist[i].location2 === "철원군"){
                                    this.locationinfo[123]['number'] += 1
                                    } else if (this.totallist[i].location2 === "평창군"){
                                    this.locationinfo[124]['number'] += 1
                                    } else if (this.totallist[i].location2 === "홍천군"){
                                    this.locationinfo[125]['number'] += 1
                                    } else if (this.totallist[i].location2 === "화천군"){
                                    this.locationinfo[126]['number'] += 1
                                    } else if (this.totallist[i].location2 === "횡성군"){
                                    this.locationinfo[127]['number'] += 1
                                    } else if (this.totallist[i].location2 === "고양시"){
                                    this.locationinfo[128]['number'] += 1
                                    } else if (this.totallist[i].location2 === "과천시"){
                                    this.locationinfo[129]['number'] += 1
                                    } else if (this.totallist[i].location2 === "광명시"){
                                    this.locationinfo[130]['number'] += 1
                                    } else if (this.totallist[i].location2 === "광주시"){
                                    this.locationinfo[131]['number'] += 1
                                    } else if (this.totallist[i].location2 === "구리시"){
                                    this.locationinfo[132]['number'] += 1
                                    } else if (this.totallist[i].location2 === "군포시"){
                                    this.locationinfo[133]['number'] += 1
                                    } else if (this.totallist[i].location2 === "김포시"){
                                    this.locationinfo[134]['number'] += 1
                                    } else if (this.totallist[i].location2 === "남양주시"){
                                    this.locationinfo[135]['number'] += 1
                                    } else if (this.totallist[i].location2 === "동두천시"){
                                    this.locationinfo[136]['number'] += 1
                                    } else if (this.totallist[i].location2 === "부천시"){
                                    this.locationinfo[137]['number'] += 1
                                    } else if (this.totallist[i].location2 === "성남시"){
                                    this.locationinfo[138]['number'] += 1
                                    } else if (this.totallist[i].location2 === "수원시"){
                                    this.locationinfo[139]['number'] += 1
                                    } else if (this.totallist[i].location2 === "시흥시"){
                                    this.locationinfo[140]['number'] += 1
                                    } else if (this.totallist[i].location2 === "안산시"){
                                    this.locationinfo[141]['number'] += 1
                                    } else if (this.totallist[i].location2 === "안성시"){
                                    this.locationinfo[142]['number'] += 1
                                    } else if (this.totallist[i].location2 === "안양시"){
                                    this.locationinfo[143]['number'] += 1
                                    } else if (this.totallist[i].location2 === "양주시"){
                                    this.locationinfo[144]['number'] += 1
                                    } else if (this.totallist[i].location2 === "여주시"){
                                    this.locationinfo[145]['number'] += 1
                                    } else if (this.totallist[i].location2 === "오산시"){
                                    this.locationinfo[146]['number'] += 1
                                    } else if (this.totallist[i].location2 === "용인시"){
                                    this.locationinfo[147]['number'] += 1
                                    } else if (this.totallist[i].location2 === "의왕시"){
                                    this.locationinfo[148]['number'] += 1
                                    } else if (this.totallist[i].location2 === "의정부시"){
                                    this.locationinfo[149]['number'] += 1
                                    } else if (this.totallist[i].location2 === "이천시"){
                                    this.locationinfo[150]['number'] += 1
                                    } else if (this.totallist[i].location2 === "파주시"){
                                    this.locationinfo[151]['number'] += 1
                                    } else if (this.totallist[i].location2 === "평택시"){
                                    this.locationinfo[152]['number'] += 1
                                    } else if (this.totallist[i].location2 === "포천시"){
                                    this.locationinfo[153]['number'] += 1
                                    } else if (this.totallist[i].location2 === "하남시"){
                                    this.locationinfo[154]['number'] += 1
                                    } else if (this.totallist[i].location2 === "화성시"){
                                    this.locationinfo[155]['number'] += 1
                                    } else if (this.totallist[i].location2 === "서귀포시"){
                                    this.locationinfo[156]['number'] += 1
                                    } else if (this.totallist[i].location2 === "제주시"){
                                    this.locationinfo[157]['number'] += 1
                                    }
                             
                            }
                        this.mapLoad()
                    })            
            

            },
        
}
</script>

<style>

</style>