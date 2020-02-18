<template>
    <div class="container">
          <div id="map" style="width:auto;height:400px;"></div>

    </div>
</template>

<script>
const kakao = window.kakao

export default {
    mounted(){
                var mapContainer = document.getElementById("map") 
                var mapOption = {
                                    center : new kakao.maps.LatLng(35.950701, 127.870667),
                                    level : 12
                                };
                this.map = new kakao.maps.Map(mapContainer, mapOption)
                this.zoomControl = new kakao.maps.ZoomControl();
                this.map.addControl(this.zoomControl, kakao.maps.ControlPosition.RIGHT);
            }
}
</script>

<style>

</style>