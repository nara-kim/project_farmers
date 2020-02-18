<template>
<!-- <div class="container">
	<h2>반응형 테이블</h2>  
	<div class="table-responsive">
        <table class="table">
            <thead>
                <tr>
		<th>#</th>
		<th>Table heading</th>
		<th>Table heading</th>
		<th>Table heading</th>
		<th>Table heading</th>
		<th>Table heading</th>
		<th>Table heading</th>
        </tr>
        </thead>
        <tbody>
            <tr>
		<td>1</td>
		<td>Table cell</td>
		<td>Table cell</td>
		<td>Table cell</td>
		<td>Table cell</td>
		<td>Table cell</td>
		<td>Table cell</td>
        </tr>
        <tr>
		<td>2</td>
		<td>Table cell</td>
		<td>Table cell</td>
		<td>Table cell</td>
		<td>Table cell</td>
		<td>Table cell</td>
		<td>Table cell</td>
        </tr>
        <tr>
		<td>3</td>
		<td>Table cell</td>
		<td>Table cell</td>
		<td>Table cell</td>
		<td>Table cell</td>
		<td>Table cell</td>
		<td>Table cell</td>
        </tr>
        </tbody>
        </table>
	</div>
</div> -->

<!-- 두번째 -->
<div class = "boardtable">
    <div class="container">
        <div class="row">
            <table>
                <thead>
                    <tr>
                        <th>제목</th>
                        <th>내용</th>
                        <th>인원</th>
                    </tr>
                </thead>
                <tbody>
					<tr v-for="help in help_list" :key="help.id">
						<router-link to="/detail_board"><td>{{help.title}}</td></router-link>
						<td>{{help.content}}</td>
						<td>{{help.people}}</td>
					</tr>
                </tbody>
            </table>
        </div>
			<button class = "button"><router-link to ='view_board_write'>글쓰기</router-link></button>

    </div>

</div>
</template>
<script>
import axios from 'axios'
export default {
	data(){
		return {
			help_list: [],
		}
	},
	methods: {
		gethelp(){
			axios
				.get('http://127.0.0.1:8000/helppage/gethelp/')
				.then(res => {
					console.log('gethelp')
					this.help_list = res.data;
				})
				.catch(err => console.log(err))
		}
	},
	mounted(){
		this.gethelp()
	}
}
</script>
<style scoped>
.boardtable{
	font-family: 'Jua', sans-serif;
    margin-bottom: 10%;
}
.button{
	font-family: 'Jua', sans-serif;
	margin-top: 2%;
	height: 45px;
	border-radius: 10px;
	float: right;
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

	td:nth-of-type(1):before { content: "First Name"; }
	td:nth-of-type(2):before { content: "Last Name"; }
	td:nth-of-type(3):before { content: "Job Title"; }
	td:nth-of-type(4):before { content: "Favorite Color"; }
	td:nth-of-type(5):before { content: "Wars of Trek?"; }
	td:nth-of-type(6):before { content: "Porn Name"; }
	td:nth-of-type(7):before { content: "Date of Birth"; }
	td:nth-of-type(8):before { content: "Dream Vacation City"; }
	td:nth-of-type(9):before { content: "GPA"; }
	td:nth-of-type(10):before { content: "Arbitrary Data"; }
}
</style>