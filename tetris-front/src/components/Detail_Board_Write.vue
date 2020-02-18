<template>
   <div class="container">

    <label for="fname">선택</label>
    <select v-model="help_select">
      <option value="일손구하기">일손구하기</option>
      <option value="장소구하기">장소구하기</option>
    </select>

    <label for="lname">제목</label>
    <input type="text" id="fname" name="firstname" v-model="title" placeholder="제목을 입력하세요.">

    <label for="lname">지역</label>
    <!-- <input type="text" id="lname" name="lastname" placeholder="지역을 입력하세요."> -->
    <select v-model="location1">
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

    <label for="lname">지역</label>
    <!-- <input type="text" id="lname" name="lastname" placeholder="지역을 입력하세요."> -->
    <select v-model="location2" v-if="`${location1}` === '경기도'">
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
    <select v-model="location2" v-else-if="`${location1}` === '강원도'">
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
    <select v-model="location2" v-else-if="`${location1}` ==='충청북도'">
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
    <select v-model="location2" v-else-if="`${location1}` === '충청남도'">
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
    <select v-model="location2" v-else-if="`${location1}` === '경상북도'">
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
    <select v-model="location2" v-else-if="`${location1}` === '경상남도'">
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
    <select v-model="location2" v-else-if="`${location1}` === '전라북도'">
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
    <select v-model="location2" v-else-if="`${location1}` === '전라남도'">
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
    <select v-model="location2" v-else-if="`${location1}` === '제주특별자치도'">
      <option disabled value="">지역을 선택해주세요</option>
      <option>서귀포시</option>
      <option>제주시</option>
    </select>
    <select v-model="location2" v-else-if="`${location1}` === '서울특별시'">
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
    <select v-model="location2" v-else-if="`${location1}` === '광주광역시'">
      <option disabled value="">지역을 선택해주세요</option>
      <option>광산구</option>
      <option>남구</option>
      <option>동구</option>
      <option>북구</option>
      <option>서구</option>
    </select>
    <select v-model="location2" v-else-if="`${location1}` === '인천광역시'">
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
    <select v-model="location2" v-else-if="`${location1}` === '대전광역시'">
      <option disabled value="">지역을 선택해주세요</option>
      <option>대덕구</option>
      <option>동구</option>
      <option>서구</option>
      <option>유성구</option>
      <option>중구</option>
    </select>
    <select v-model="location2" v-else-if="`${location1}` === '대구광역시'">
      <option disabled value=""></option>
      <option>남구</option>
      <option>달서구</option>
      <option>동구</option>
      <option>북구</option>
      <option>서구</option>
      <option>수성구</option>
      <option>중구</option>
    </select>
    <select v-model="location2" v-else-if="`${location1}` === '부산광역시'">
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
    <select v-model="location2" v-else-if="`${location1}` === '울산광역시'">
      <option disabled value="">지역을 선택해주세요</option>
      <option>남구</option>
      <option>동구</option>
      <option>북구</option>
      <option>중구</option>
      <option>울주군</option>
    </select>

    <label for="lname">날짜</label>
    <br>
    <input type="date" id="date" name="date" v-model="help_date">
    <br>

    <label for="lname">인원</label>
    <input type="number" id = "num" v-model="people" style="ime-mode:disabled;" placeholder="인원을 입력하세요.">

    <label for="subject">내용</label>
    <textarea id="subject" name="subject" v-model="content" placeholder="내용을 입력하세요." style="height:200px"></textarea>

    <button @click.prevent="CreateHelp">
      일손 구하기 작성
    </button>
    <input type="submit" value="제출">

</div>
</template>
<script>
import axios from 'axios';
export default {
  data(){
    return{
      help_select:'',
      title:'',
      location1:'',
      location2:'',
      help_date:'',
      people:'',
      content:'',
    }
  },
  methods: {
    CreateHelp() {
      let formData = new FormData();
      formData.append('help_select', this.help_select);
      formData.append('title',this.title)
      formData.append('location1',this.location1)
      formData.append('location2',this.location2)
      formData.append('help_date',this.help_date)
      formData.append('people', this.people)
      formData.append('content',this.content)
      formData.append('user', this.userName)
      axios
        .post('http://127.0.0.1:8000/helppage/create/', formData)
        .then(res=> {
          this.dumy = res.data;
          this.$router.push("/board")
        })
        .catch((err)=>{
          console.log(err)
        })
    }
  },
  computed: {
    userName() {
      return this.$store.getters.loggedInUser.username;
      }
  }
  
}
</script>
<style scoped>

input[type=text], select, textarea, input[type=date] {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box; 
  margin-top: 6px;
  margin-bottom: 16px;
  resize: vertical 
}

input[type=submit] {
  background-color: #4CAF50;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}

.container {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}

#date{
    width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  margin-top: 6px; 
  margin-bottom: 16px;
  resize: vertical
}
#num{
    width: 100%;
  padding: 12px;
  border: 1px solid #ccc; 
  border-radius: 4px; 
  box-sizing: border-box;
  margin-top: 6px; 
  margin-bottom: 16px;
  resize: vertical 
}

</style>