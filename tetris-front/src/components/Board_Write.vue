<template>
<div>
	<section class="search-sec">
		<div class="container">
			<!-- <form action="#" method="post" novalidate="novalidate"> -->
				<div class="row">
					<div class="col-lg-12">
						<div class="row">
							<div class="col-lg-3 col-md-3 col-sm-12 p-0">
								<select class="form-control search-slt" v-model="selected3"> 
									<option disabled value="">카데고리별</option> 
									<option value="전체">전체</option> 
									<option value="일손구하기">일손구하기</option> 
									<option value="도와드리기">도와드리기</option> 
								</select>
							</div>
							<div class="col-lg-3 col-md-3 col-sm-12 p-0">
								<select class="form-control search-slt" v-model="location1">
									<option disabled value="">지역을 선택해주세요</option>
									<option>경기도</option>
									<option>강원도</option>
									<option>충청북도</option>
									<option>충청남도</option>
									<option>경상북도</option>
									<option>경상남도</option>
									<option>전라북도</option>
									<option>전라남도</option>
									<option>제주특별자치도</option>
									<option>서울특별시</option>
									<option>광주광역시</option>
									<option>인천광역시</option>
									<option>대전광역시</option>
									<option>대구광역시</option>
									<option>부산광역시</option>
									<option>울산광역시</option>
								</select>
							</div>
							<div class="col-lg-3 col-md-3 col-sm-12 p-0">
								<select class="form-control search-slt" v-model="location2" v-if="`${location1}` === '경기도'">
									<option disabled value="">지역을 선택해주세요</option>
									<option>고양시</option>
									<option>과천시</option>
									<option>광명시</option>
									<option>광주시</option>
									<option>구리시</option>
									<option>군포시</option>
									<option>김포시</option>
									<option>남양주시</option>
									<option>동두천시</option>
									<option>부천시</option>
									<option>성남시</option>
									<option>수원시</option>
									<option>시흥시</option>
									<option>안산시</option>
									<option>안성시</option>
									<option>안양시</option>
									<option>양주시</option>
									<option>여주시</option>
									<option>오산시</option>
									<option>용인시</option>
									<option>의왕시</option>
									<option>의정부시</option>
									<option>이천시</option>
									<option>파주시</option>
									<option>평택시</option>
									<option>포천시</option>
									<option>하남시</option>
									<option>화성시</option>
								</select>
								<select class="form-control search-slt" v-model="location2" v-else-if="`${location1}` === '강원도'">
									<option disabled value="">지역을 선택해주세요</option>
									<option>강릉시</option>
									<option>동해시</option>
									<option>삼척시</option>
									<option>속초시</option>
									<option>원주시</option>
									<option>춘천시</option>
									<option>태백시</option>
									<option>고성군</option>
									<option>양구군</option>
									<option>양양군</option>
									<option>영월군</option>
									<option>인제군</option>
									<option>정선군</option>
									<option>철원군</option>
									<option>평창군</option>
									<option>홍천군</option>
									<option>화천군</option>
									<option>횡성군</option>
								</select>
								<select class="form-control search-slt" v-model="location2" v-else-if="`${location1}` ==='충청북도'">
									<option disabled value="">지역을 선택해주세요</option>
									<option>제천시</option>
									<option>청주시</option>
									<option>충주시</option>
									<option>괴산군</option>
									<option>단양군</option>
									<option>보은군</option>
									<option>영동군</option>
									<option>옥천군</option>
									<option>음성군</option>
									<option>증평군</option>
									<option>진천군</option>
								</select>
								<select class="form-control search-slt" v-model="location2" v-else-if="`${location1}` === '충청남도'">
									<option disabled value=""></option>
									<option>계룡시</option>
									<option>공주시</option>
									<option>논산시</option>
									<option>당진시</option>
									<option>보령시</option>
									<option>서산시</option>
									<option>아산시</option>
									<option>천안시</option>
									<option>금산군</option>
									<option>부여군</option>
									<option>서천군</option>
									<option>예산군</option>
									<option>청양군</option>
									<option>태안군</option>
									<option>홍성군</option>
								</select>
								<select class="form-control search-slt" v-model="location2" v-else-if="`${location1}` === '경상북도'">
									<option disabled value="">지역을 선택해주세요</option>
									<option>경산시</option>
									<option>경주시</option>
									<option>구미시</option>
									<option>김천시</option>
									<option>문경시</option>
									<option>상주시</option>
									<option>안동시</option>
									<option>영주시</option>
									<option>영천시</option>
									<option>포항시</option>
									<option>고령군</option>
									<option>군위군</option>
									<option>봉화군</option>
									<option>성주군</option>
									<option>영덕군</option>
									<option>영양군</option>
									<option>예천군</option>
									<option>울릉군</option>
									<option>울진군</option>
									<option>의성군</option>
									<option>청도군</option>
									<option>청송군</option>
									<option>칠곡군</option>
								</select>
								<select class="form-control search-slt" v-model="location2" v-else-if="`${location1}` === '경상남도'">
									<option disabled value="">지역을 선택해주세요</option>
									<option>거제시</option>
									<option>김해시</option>
									<option>밀양시</option>
									<option>사천시</option>
									<option>양산시</option>
									<option>진주시</option>
									<option>창원시</option>
									<option>통영시</option>
									<option>거창군</option>
									<option>고성군</option>
									<option>남해군</option>
									<option>산청군</option>
									<option>의령군</option>
									<option>창녕군</option>
									<option>하동군</option>
									<option>함안군</option>
									<option>함양군</option>
									<option>합천군</option>
								</select>
								<select class="form-control search-slt" v-model="location2" v-else-if="`${location1}` === '전라북도'">
									<option disabled value="">지역을 선택해주세요</option>
									<option>군산시</option>
									<option>김제시</option>
									<option>남원시</option>
									<option>익산시</option>
									<option>전주시</option>
									<option>정읍시</option>
									<option>고창군</option>
									<option>무주군</option>
									<option>부안군</option>
									<option>순창군</option>
									<option>완주군</option>
									<option>임실군</option>
									<option>장수군</option>
									<option>진안군</option>
								</select>
								<select class="form-control search-slt" v-model="location2" v-else-if="`${location1}` === '전라남도'">
									<option disabled value="">지역을 선택해주세요</option>
									<option>광양시</option>
									<option>나주시</option>
									<option>목포시</option>
									<option>순천시</option>
									<option>여수시</option>
									<option>강진군</option>
									<option>고흥군</option>
									<option>곡성군</option>
									<option>구례군</option>
									<option>담양군</option>
									<option>무안군</option>
									<option>보성군</option>
									<option>신안군</option>
									<option>영광군</option>
									<option>영암군</option>
									<option>완도군</option>
									<option>장성군</option>
									<option>장흥군</option>
									<option>진도군</option>
									<option>함평군</option>
									<option>해남군</option>
									<option>화순군</option>
								</select>
								<select class="form-control search-slt" v-model="location2" v-else-if="`${location1}` === '제주특별자치도'">
									<option disabled value="">지역을 선택해주세요</option>
									<option>서귀포시</option>
									<option>제주시</option>
								</select>
								<select class="form-control search-slt" v-model="location2" v-else-if="`${location1}` === '서울특별시'">
									<option disabled value=""></option>
									<option>강남구</option>
									<option>강동구</option>
									<option>강북구</option>
									<option>강서구</option>
									<option>관악구</option>
									<option>광진구</option>
									<option>구로구</option>
									<option>금천구</option>
									<option>노원구</option>
									<option>도봉구</option>
									<option>동대문구</option>
									<option>동작구</option>
									<option>마포구</option>
									<option>서대문구</option>
									<option>서초구</option>
									<option>성동구</option>
									<option>성북구</option>
									<option>송파구</option>
									<option>양천구</option>
									<option>영등포구</option>
									<option>용산구</option>
									<option>은평구</option>
									<option>종로구</option>
									<option>중구</option>
									<option>중랑구</option>
								</select>
								<select class="form-control search-slt" v-model="location2" v-else-if="`${location1}` === '광주광역시'">
									<option disabled value="">지역을 선택해주세요</option>
									<option>광산구</option>
									<option>남구</option>
									<option>동구</option>
									<option>북구</option>
									<option>서구</option>
								</select>
								<select class="form-control search-slt" v-model="location2" v-else-if="`${location1}` === '인천광역시'">
									<option disabled value="">지역을 선택해주세요</option>
									<option>계양구</option>
									<option>남동구</option>
									<option>동구</option>
									<option>미추홀구</option>
									<option>부평구</option>
									<option>서구</option>
									<option>연수구</option>
									<option>중구</option>
									<option>강화군</option>
									<option>옹진군</option>
								</select>
								<select class="form-control search-slt" v-model="location2" v-else-if="`${location1}` === '대전광역시'">
									<option disabled value="">지역을 선택해주세요</option>
									<option>대덕구</option>
									<option>동구</option>
									<option>서구</option>
									<option>유성구</option>
									<option>중구</option>
								</select>
								<select class="form-control search-slt" v-model="location2" v-else-if="`${location1}` === '대구광역시'">
									<option disabled value=""></option>
									<option>남구</option>
									<option>달서구</option>
									<option>동구</option>
									<option>북구</option>
									<option>서구</option>
									<option>수성구</option>
									<option>중구</option>
								</select>
								<select class="form-control search-slt" v-model="location2" v-else-if="`${location1}` === '부산광역시'">
									<option disabled value="">지역을 선택해주세요</option>
									<option>강서구</option>
									<option>금정구</option>
									<option>남구</option>
									<option>동구</option>
									<option>동래구</option>
									<option>부산진구</option>
									<option>북구</option>
									<option>사상구</option>
									<option>사하구</option>
									<option>서구</option>
									<option>수영구</option>
									<option>연제구</option>
									<option>영도구</option>
									<option>중구</option>
									<option>해운대구</option>
									<option>기장군</option>
								</select>
								<select class="form-control search-slt" v-model="location2" v-else-if="`${location1}` === '울산광역시'">
									<option disabled value="">지역을 선택해주세요</option>
									<option>남구</option>
									<option>동구</option>
									<option>북구</option>
									<option>중구</option>
									<option>울주군</option>
								</select>
							</div>
							<div class="col-lg-3 col-md-3 col-sm-12 p-0">
								<!-- <button type="button" class="btn btn-primary wrn-btn">Search</button> -->
								<button class="btn btn-info wrn-btn" v-if="`${location1}` && `${location2}`" @click="locationhelp()">
									지역선택
								</button>
							</div>
						</div>
					</div>
				</div>
			<!-- </form> -->
		</div>
	</section>

	<div class = "boardtable">
		<div class="container">
			<div class="row">
				<table>
               <thead>
                  <tr>
                     <th>구분</th>
                     <th>제목</th>
                     <th>글쓴이</th>
                     <th>지역</th>
                  </tr>
               </thead>
               <tbody>
                  <tr v-for="filterlist in filteredHelpList" :key="filterlist.id">
                  <td>{{filterlist.help_select}}</td>
                  <td>{{filterlist.title}}</td>
                  <td>{{filterlist.username}}</td>
                  <td>{{filterlist.location1}} {{filterlist.location2}}</td>
                  </tr>
               </tbody>
            </table>
			</div>
				<button class = "button"><router-link to ='view_board_write'>글쓰기</router-link></button>
		</div>
	</div>
</div>
</template>
<script>
import axios from 'axios'
export default {
   data(){
      return {
         help_list: [],
         location_list: [],
         selected3: "",
         location1:'',
         location2:'',
               }
   },
   methods: {
      gethelp(){
         axios
            .get('http://15.165.77.204:8000/helppage/gethelp/')
            .then(res => {
               console.log('gethelp')
               this.help_list = res.data;
            })
            .catch(err => console.log(err))
      },
      locationhelp(){
            let formData = new FormData();
            formData.append('location1', this.location1)
            formData.append('location2', this.location2)
            axios.post('http://15.165.77.204:8000/helppage/locationhelp/', formData)
            .then(response => {
               this.location_list = response.data
               this.help_list = response.data
         })
      }
   },
   computed: {
      filteredHelpList() {

         if (this.selected3 === "일손구하기" || this.selected3 == "도와드리기") {
            const filterList = this.help_list.filter(help => help.help_select === this.selected3)   
            return filterList
         } else {
            const filterList = this.help_list
            return filterList
         }       
      },
   },
   mounted(){
      this.gethelp()
   },
}
</script>
<style scoped>
.boardtable{
   font-family: 'Jua', sans-serif;
    margin-bottom: 10%;
}

table { 
  width: 100%; 
  border-collapse: collapse; 
}
tr:nth-of-type(odd) { 
  background: #eee; 
}
th { 
  background: #333; 
  color: white; 
  font-weight: bold; 
}
td, th { 
  padding: 6px; 
  border: 1px solid #ccc; 
  text-align: left; 
}

@media 
only screen and (max-width: 760px),
(min-device-width: 768px) and (max-device-width: 1024px)  {

   table, thead, tbody, th, td, tr { 
      display: block; 
   }
   
   thead tr { 
      position: absolute;
      top: -9999px;
      left: -9999px;
   }
   
   tr { border: 1px solid #ccc; }
   
   td { 
      border: none;
      border-bottom: 1px solid #eee; 
      position: relative;
      padding-left: 50%; 
   }
   
   td:before { 
      position: absolute;
      top: 6px;
      left: 6px;
      width: 45%; 
      padding-right: 10px; 
      white-space: nowrap;
   }

   td:nth-of-type(1):before { content: "구분"; }
   td:nth-of-type(2):before { content: "제목"; }
   td:nth-of-type(3):before { content: "글쓴이"; }
   td:nth-of-type(4):before { content: "지역"; }
  
}

/*search box css start here*/
.search-sec{
    /* background: #938fad; */
	padding: 2rem;
}
.search-slt{
    display: block;
    width: 100%;
    font-size: 0.875rem;
    line-height: 1.5;
    color: #55595c;
    background-color: #fff;
    background-image: none;
    border: 1px solid #ccc;
    height: calc(3rem + 2px) !important;
    border-radius:0;
}
.wrn-btn{
    width: 100%;
    font-size: 16px;
    font-weight: 400;
    text-transform: capitalize;
     height: calc(3rem + 2px) !important;
     border-radius:0;
}

</style>