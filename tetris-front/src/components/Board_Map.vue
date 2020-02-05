<template>
<div>
  <div id="map" style="width:800px;height:400px;"></div>
  <button @click="me()">지도 중심좌표 부드럽게 이동시키기</button>
  <div>
      {{weaherlist}}
  <button @click="location()">위치전송</button>
  </div>
</div>
</template>

<script>

const kakao = window.kakao
import axios from 'axios';

export default {
    data(){
        return{
        map:{},
        aaa: { location: "박승재"},
        weaherlist: null
        }
    },
 name:'dmap',
 methods:{
     me(){
        if (navigator.geolocation) {
            // GeoLocation을 이용해서 접속 위치를 얻어옵니다
            var displayMarker = this.displayMarker;
            const a = this
            navigator.geolocation.getCurrentPosition(function(position) {
                
                const lat = position.coords.latitude, // 위도
                    lon = position.coords.longitude; // 경도
                
                
                var locPosition = new kakao.maps.LatLng(lat, lon), // 마커가 표시될 위치를 geolocation으로 얻어온 좌표로 생성합니다
                    message = '<div style="padding:5px;">여기에 계신가요?!</div>'; // 인포윈도우에 표시될 내용입니다
                
                // 마커와 인포윈도우를 표시합니다
                displayMarker(locPosition, message);
                axios.get('http://127.0.0.1:8000/api/mapinfo/', {
                        params:{
                            aaa : lat,
                            bbb : lon,
                                }})
                    .then(res=>{
                        console.log(res.data)
                        a.weaherlist = res.data
                        console.log(a.weaherlist)
                // console.log(res.data.location)
                    })
        
    });
            
        } else { // HTML5의 GeoLocation을 사용할 수 없을때 마커 표시 위치와 인포윈도우 내용을 설정합니다
            
            var locPosition = new kakao.maps.LatLng(33.450701, 126.570667),    
                message = 'geolocation을 사용할수 없어요..'
                
            this.displayMarker(locPosition, message);
        }  
    },
        
     displayMarker(locPosition, message) {

        // 마커를 생성합니다
        var marker = new kakao.maps.Marker({  
            map: this.map, 
            position: locPosition
        }); 
        
        var iwContent = message, // 인포윈도우에 표시할 내용
            iwRemoveable = true;

        // 인포윈도우를 생성합니다
        var infowindow = new kakao.maps.InfoWindow({
            content : iwContent,
            removable : iwRemoveable
        });

        
        // 인포윈도우를 마커위에 표시합니다 
        infowindow.open(this.map, marker);
        
        // 지도 중심좌표를 접속위치로 변경합니다
        this.map.setCenter(locPosition);      
    },
    location: function(){
        axios.get('http://127.0.0.1:8000/api/mapinfo/', {
            params:{
                aaa : this.aaa
            }
        })
        .then(res=>{
            console.log(res)
        })
    }
 },
 mounted(){
    //  var latitud = position.coords.latitude;
    //  var longitude = position.coords.longitude;
    var mapContainer = document.getElementById("map") 
    var mapOption = {
        center : new kakao.maps.LatLng(33.450701, 126.570667)    // 지도의 중심좌표
        , level : 3    // 지도의 확대레벨
    };
    this.map = new kakao.maps.Map(mapContainer, mapOption)

    this.me();

 }
}

</script>