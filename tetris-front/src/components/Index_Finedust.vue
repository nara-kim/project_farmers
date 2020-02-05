<template>
  <div class="col-lg-4 sidebar-widgets">
   
    <div class="widget-wrap">
      <div class="single-sidebar-widget post-category-widget">
        <h4 class="single-sidebar-widget__title" style="letter-spacing:3px">미세먼지</h4>

        <div>
          <div>
              <div>
                <div class="weather">
                    <div class="current">
                        <div class="info">
                            <div>&nbsp;</div>
                            <div class="city"><small><small>현재위치:</small></small> London</div>
                            <div class="temp">67&deg; <small>F</small></div>
                            <div class="wind"><small><small>WIND:</small></small> 22 km/h</div>
                            <div>&nbsp;</div>
                        </div>
                        <div class="icon">
                            <span class="wi-day-sunny"></span>
                        </div>
                    </div>
                    <div class="future">
                        <div class="day">
                            <h3>Mon</h3>
                            <p><span class="wi-day-cloudy"></span></p>
                        </div>
                        <div class="day">
                            <h3>Tue</h3>
                            <p><span class="wi-showers"></span></p>
                        </div>
                        <div class="day">
                            <h3>Wed</h3>
                            <p><span class="wi-rain"></span></p>
                        </div>
                    </div>
                </div>
            </div>
          </div>
        </div>   

      </div>
    </div>

  </div>
    

</template>



<style scoped>
.single-sidebar-widget__title{
  font-size: 180%;
}
.single-sidebar-widget{
  background-color: white;
  border: 1px solid #e4e4e4;
}
.weather
    {
        display: flex;
        flex-flow: column wrap;
        box-shadow: 0px 1px 10px 0px #cfcfcf;
        overflow: hidden;
    }

.weather .current
{
    display: flex;
    flex-flow: row wrap;
    background-repeat: repeat-x;
    color: white;
    padding: 20px;
    text-shadow: 1px 1px #F68D2E;
}

.weather .current .info
{
    display: flex;
    flex-flow: column wrap;
    justify-content: space-around;
    flex-grow: 2;
}

.weather .current .info .city
{
    font-size: 26px;
}

.weather .current .info .temp
{
    font-size: 56px;
}

.weather .current .info .wind
{
    font-size: 24px;
}

.weather .current .icon
{
  text-align: center;
  font-size: 64px;
  flex-grow: 1;
}

.weather .future
{
    display: flex;
    flex-flow: row nowrap;
}

.weather .future .day
{
    flex-grow: 1;
    text-align: center;
    cursor: pointer;
}

.weather .future .day:hover
{
    color: #fff;
    background-color: #F68D2E;
}

.weather .future .day h3
{
    text-transform: uppercase;
}

.weather .future .day p
{
    font-size: 28px;
}
</style>
