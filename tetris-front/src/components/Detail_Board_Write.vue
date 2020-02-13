<template>
   <div class="container">
  <form action="action_page.php">

    <label for="fname">선택</label>
    <select>
      <option value="일손구하기">일손구하기</option>
      <option value="장소구하기">장소구하기</option>
    </select>

    <label for="lname">제목</label>
    <input type="text" id="fname" name="firstname" placeholder="제목을 입력하세요.">

    <label for="lname">지역</label>
    <input type="text" id="lname" name="lastname" placeholder="지역을 입력하세요.">

    <label for="lname">날짜</label>
    <br>
    <input type="date" id="date" name="date">
    <br>

    <label for="lname">인원</label>
    <input type="number" id = "num" style="ime-mode:disabled;" placeholder="인원을 입력하세요.">

    <label for="subject">내용</label>
    <textarea id="subject" name="subject" placeholder="내용을 입력하세요." style="height:200px"></textarea>

    <input type="submit" value="제출">

  </form>
</div>
</template>

<style scoped>

input[type=text], select, textarea {
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