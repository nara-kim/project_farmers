<template>

    <table class="table table-striped table-rwd-name table-hidden" style="width:50%; margin-left:400px;  ">

<thead class="table-only-hide">
    <h3>공지사항</h3>

    <tr>
        <th>번호</th>
        <th style="padding-left : 390px;">제목</th>
        <th style="padding-right : 80px;">글쓴이</th>
    </tr>
</thead>
    <tbody>
  <tr>
      <td data-label="num">1</td>
      <td data-label="name">제목자리</td>
      <td data-label="writer">글쓴이자리</td>
  </tr>
  <tr>
      <td data-label="num">2</td>
      <td data-label="name">제목자리</td>
      <td data-label="writer">글쓴이자리</td>
  </tr>
  <tr>
      <td data-label="num">3</td>
      <td data-label="name">제목자리</td>
      <td data-label="writer">글쓴이자리</td>
  </tr>
 
</tbody>
        </table>

</template>

<style scoped>
.table-hidden tbody{
    /* overflow-y: scroll; */
   height: 200px;
   display: block;   
}
.table-hidden tr {
   width: 100%;
   display: inline-table;
}
.table-rwd-name{background-color: rgba(255,255,255,0.5);}
.table-rwd-name tfoot th{
    background-color: #FFF;
   border-bottom: 1px solid #F90 !important;
   text-align: left;
   background-color: #fcf5e6;
   
}
.board{
    width :"10px";
}
@media (max-width: 736px) {
  .table-rwd-name tr, 
  .table-rwd-name td, 
  .table-rwd-name th
  {
      display: block;
      border-top: 0 !important;
  }
  .table-rwd-name td {
    text-align: left;
    font-size: 15px;
    overflow: hidden;
    width: 100%;
    }
 .table-rwd-name td:before {
    content: attr(data-label);
    float: left;
    text-transform: uppercase;
    font-weight: bold;
   margin-right: 10px
  }
  thead.table-only-hide {
    display: none !important;
  }
}
@media (min-width: 736px) {
.table-hidden td[data-label="name"]{ width:150px;}
.table-hidden td[data-label="writer"]{ width:183px;}    
}
</style>