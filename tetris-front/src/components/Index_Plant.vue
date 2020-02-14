<template>
<div style="font-family: 'Jua', sans-serif; margin-top:30px;">
    병해충정보<hr>
    <div> 
        <select v-model="selected"> 
            <option disabled value="">식물 명</option> 
            <option>가지</option>
            <option>감</option>
            <option>감귤</option>
            <option>감자</option>
            <option>감초</option>
            <option>갓</option>
            <option>개나리</option>
            <option>거베라</option>
            <option>고구마</option>
            <option>고추</option>
            <option>고추냉이</option>
            <option>곰취</option>
            <option>과꽃</option>
            <option>관음죽</option>
            <option>구기자</option>
            <option>국화</option>
            <option>군자란</option>
            <option>글라디올러스</option>
            <option>금어초</option>
            <option>금잔화</option>
            <option>은빛담쟁이덩굴</option>
            <option>꽃양배추</option>
            <option>논벼</option>
            <option>다알리아</option>
            <option>당근</option>
            <option>금잔화</option>
            <option>은빛담쟁이덩굴</option>
            <option>꽃양배추</option>
            <option>논벼</option>
            <option>다알리아</option>
            <option>당근</option>
            <option>대추</option>
            <option>더덕</option>
            <option>도라지</option>
            <option>동백나무</option>
            <option>동양심비</option>
            <option>드라세나</option>
            <option>디펜바키아</option>
            <option>딸기</option>
            <option>마</option>
            <option>마늘</option>
            <option>매실</option>
            <option>맥문동</option>
            <option>메리골드</option>
            <option>모과</option>
            <option>모란</option>
            <option>몬스테라</option>
            <option>무</option>
            <option>마</option>
        </select> 
        <select v-model="selected2" v-if="`${selected}` === '가지'">
            <option disabled value="">병 명</option> 
             <option>갈색둥근무늬병</option>
             <option>갈색무늬병</option>
             <option>검은썩음병</option>
             <option>검은점뿌리썩음병</option>
             <option>겹무늬병</option>
             <option>균핵병</option>
             <option>모자이크병</option>
             <option>시들음병</option>
             <option>역병</option>
             <option>잎곰팡이병</option>
             <!-- <option>잘록병</option>
             <option>잿빛곰팡이병</option>
             <option>점무늬병</option>
             <option>풋마름병</option>
             <option>흰가루병</option> -->
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '감'">
            <option disabled value="">병 명</option> 
             <option>검은점무늬병</option>
             <option>그을음병</option>
             <option>둥근무늬낙엽병</option>
             <option>모두늬낙엽병</option>
             <option>잎마름병</option>
             <option>잿빛곰팡이병</option>
             <option>줄기마름병</option>
             <option>줄기썩음병</option>
             <option>탄저병</option>
             <option>흰가루병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '감귤'">
            <option disabled value="">병 명</option> 
             <!-- <option>갈색썩음병</option> -->
             <option>갈색줄무늬오갈병</option>
             <option>검은무늬병</option>
             <option>검은썩음병</option>
             <option>검은점무늬병</option>
             <option>궤양병</option>
             <option>균핵병</option>
             <option>그을음병</option>
             <option>녹색곰팡이병</option>
             <option>누른무늬병</option>
             <option>더뎅이병</option>
             <!-- <option>모자이크병</option>
             <option>무름병</option>
             <option>붉은썩음병</option>
             <option>스템필리움썩음병</option>
             <option>역병</option>
             <option>온주위축병</option>
             <option>잿빛곰팡이병</option>
             <option>접목부이상병</option>
             <option>청색곰팡이병</option>
             <option>탄저병</option>
             <option>흰곰팡이병</option>
             <option>소립검은점무늬병</option>
             <option>수지병</option> -->
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '감자'">
            <option disabled value="">병 명</option> 
             <option>검은무늬썩음병</option>
             <option>겹둥근무늬병</option>
             <option>균핵병</option>
             <option>더뎅이병</option>
             <option>역병</option>
             <option>탄저병</option>
             <!-- <option>풋마름병</option> -->
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '감초'">
            <option disabled value="">병 명</option>
             <option>세균점무늬병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '갓'">
            <option disabled value="">병 명</option>
             <option>검은무늬병</option>
             <option>노균병</option>
             <option>모자이크병</option>
             <option>뿌리혹병, 무사마귀병</option>
             <option>세균성잎마름병</option>
             <option>잘록병</option>
             <option>흰녹가루병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '개나리'">
            <option disabled value="">병 명</option>
             <option>탄저병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '거베라'">
            <option disabled value="">병 명</option>
             <option>균핵병</option>
             <option>그루썩음병</option>
             <option>시들음병</option>
             <option>잿빛곰팡이병</option>
             <option>점무늬병</option>
             <option>흰가루병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '고구마'">
            <option disabled value="">병 명</option>
             <option>검은무늬병</option>
             <option>더뎅이병</option>
             <option>덩굴쪼김병</option>
             <option>모틀병</option>
             <option>무름병</option>
             <option>밑썩음병</option>
             <option>자주날개무늬병</option>
             <option>점균병</option>
             <option>점무늬병</option>
             <option>푸른곰팡이병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '고무나무'">
            <option disabled value="">병 명</option>
             <option>반점세균병 인도고무나무</option>
             <option>줄기썩음병 벤자미나고무나무</option>
             <option>탄저병 데코라고무나무</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '고추'">
            <option disabled value="">병 명</option>
             <option>갈색점무늬병</option>
             <option>검은곰팡이병</option>
             <option>검은점열매썩음병</option>
             <option>겹무늬병</option>
             <option>궤양병</option>
             <option>균핵병</option>
             <option>꼭지썩음병</option>
             <option>누른모자이크병</option>
             <option>모자이크병</option>
             <option>무름병</option>
             <!-- <option>세균성점무늬병</option>
             <option>시들음병</option>
             <option>역병</option>
             <option>옆맥투명병</option>
             <option>원형반점병</option>
             <option>위조병</option>
             <option>잘록병</option>
             <option>잿빛곰팡이병</option>
             <option>점무늬병</option>
             <option>탄저병</option>
             <option>풋마름병</option>
             <option>흰가루병</option>
             <option>흰무늬병</option>
             <option>모자이크병</option> -->
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '고추냉이'">
            <option disabled value="">병 명</option>
             <option>검은점무늬병</option>
             <option>관부썩음병</option>
             <option>뿌리썩음병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '곰취'">
            <option disabled value="">병 명</option>
             <option>흰비단병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '과꽃'">
            <option disabled value="">병 명</option>
             <option>시들음병</option>
             <option>잘록병</option>
             <option>잿빛곰팡이병</option>
             <option>점무늬병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '관음죽'">
            <option disabled value="">병 명</option>
             <option>점무늬병</option>
             <option>탄저병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '구기자'">
            <option disabled value="">병 명</option>
             <option>뒷면곰팡이병</option>
             <option>탄저병</option>
             <option>흰가루병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '국화'">
            <option disabled value="">병 명</option>
             <option>균핵병</option>
             <option>뿌리썩음병</option>
             <option>역병</option>
             <option>잿빛곰팡이병</option>
             <option>점무늬병</option>
             <option>흰녹병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '군자란'">
            <option disabled value="">병 명</option>
             <option>잿빛곰팡이병</option>
             <option>탄저병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '글라디올러스'">
            <option disabled value="">병 명</option>
             <option>마른썩음병</option>
             <option>모자이크병</option>
             <option>목썩음병</option>
             <option>붉은반점병</option>
             <option>잿빛곰팡이병</option>
             <option>푸른곰팡이</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '금어초'">
            <option disabled value="">병 명</option>
             <option>검은무늬병</option>
             <option>균핵병</option>
             <option>잘록병</option>
             <option>잿빛곰팡이병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '금잔화'">
            <option disabled value="">병 명</option>
             <option>잘록병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '꽃양배추'">
            <option disabled value="">병 명</option>
             <option>검은무늬병</option>
             <option>균핵병</option>
             <option>시들음병</option>
             <option>잘록병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '논벼'">
            <option disabled value="">병 명</option>
             <option>갈색균핵병</option>
             <option>갈색잎마름병</option>
             <option>검은줄오갈병</option>
             <!-- <option>그을음병</option> -->
             <option>깨씨무늬병</option>
             <option>누른오갈병</option>
             <option>도열병</option>
             <option>모마름병</option>
             <option>모썩음병</option>
             <option>붉은곰팡이병</option>
             <option>세균성벼알마름병</option>
             <!-- <option>오갈병</option>
             <option>이삭누룩병</option>
             <option>잎집눈무늬병</option>
             <option>잎집썩음병</option>
             <option>적색균핵병</option>
             <option>좀공균핵병</option>
             <option>줄무늬잎마름병</option>
             <option>키다리병</option>
             <option>회색균핵병</option>
             <option>흰잎마름병</option> -->
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '다알리아'">
            <option disabled value="">병 명</option>
             <option>모자이크병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '당근'">
            <option disabled value="">병 명</option>
             <option>검은무늬병</option>
             <option>검은잎마름병</option>
             <option>관부썩음병</option>
             <option>균핵병</option>
             <option>마른썩음병</option>
             <option>모자이크병</option>
             <option>무름병</option>
             <option>점무늬병</option>
             <option>흰가루병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '대추'">
            <option disabled value="">병 명</option>
             <option>그을음병</option>
             <option>녹병</option>
             <option>빗자루병</option>
             <option>역병</option>
             <option>잎마름병</option>
             <option>잎줄기마름병</option>
             <option>잿빛곰팡이병</option>
             <option>점무늬병</option>
             <option>줄기썩음병</option>
             <option>탄저병</option>
             <!-- <option>흰날개무늬병</option> -->
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '더덕'">
            <option disabled value="">병 명</option>
             <option>녹병</option>
             <option>점무늬병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '도라지'">
            <option disabled value="">병 명</option>
             <option>시들음병</option>
             <option>점무늬병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '도라지(길경)'">
            <option disabled value="">병 명</option>
             <option>꽃썩음병</option>
             <option>뇌두부패 증상</option>
             <option>당근뿌리혹선충</option>
             <option>점무늬병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '동백나무'">
            <option disabled value="">병 명</option>
             <option>잎마름병</option>
             <option>줄기썩음병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '동양심비'">
            <option disabled value="">병 명</option>
             <option>잎마름병 한란</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '드라세나'">
            <option disabled value="">병 명</option>
             <option>탄저병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '디펜바키아'">
            <option disabled value="">병 명</option>
             <option>탄저병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '딸기'">
            <option disabled value="">병 명</option>
             <option>겹무늬병</option>
             <option>균핵병</option>
             <option>누른오갈병</option>
             <option>눈마름병</option>
             <option>뱀눈무늬병</option>
             <option>뿌리썩음병</option>
             <option>세균모무늬병</option>
             <option>시들음병</option>
             <option>얼룩무늬병</option>
             <option>역병</option>
             <!-- <option>잿빛곰팡이병</option>
              <option>점균병</option>
             <option>탄저병</option>
             <option>흰가루병</option> -->
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '마'">
            <option disabled value="">병 명</option>
             <option>마뿌리썩음병</option>
             <option>점무늬병</option>
             <option>탄저병</option>
             <option>흰무늬병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '마늘'">
            <option disabled value="">병 명</option>
             <option>갈색잎마름병</option>
             <option>녹병</option>
             <option>마른썩음병</option>
             <option>모자이크병</option>
             <option>잎마름병</option>
             <option>잎집썩음병</option>
             <option>잿빛곰팡이병</option>
             <option>푸른곰팡이병</option>
             <option>흑색썩음균핵병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '매실'">
            <option disabled value="">병 명</option>
             <option>갈색고약병</option>
             <option>궤양병</option>
             <option>둥근점무늬병</option>
             <option>서리흰가루병</option>
             <option>자두곰보병</option>
             <option>잿빛무늬병</option>
             <option>점무늬병</option>
             <option>탄저병</option>
             <option>혹병</option>
             <option>흰가루병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '맥문동'">
            <option disabled value="">병 명</option>
             <option>붉은점무늬병</option>
             <option>뿌리썩음병</option>
             <option>탄저병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '메리골드'">
            <option disabled value="">병 명</option>
             <option>모자이크병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '모과'">
            <option disabled value="">병 명</option>
             <option>그을음(점무늬병)</option>
             <option>붉은별무늬병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '모란(목단)'">
            <option disabled value="">병 명</option>
             <option>잿빛곰팡이병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '몬스테라'">
            <option disabled value="">병 명</option>
             <option>잿빛곰팡이병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '무'">
            <option disabled value="">병 명</option>
             <option>갈색뿌리썩음병</option>
             <option>검은무늬병</option>
             <option>검은뿌리썩음병</option>
             <option>검은썩음병</option>
             <option>균핵병</option>
             <!-- <option>뇨균병</option>
             <option>무름병</option>
             <option>뿌리썩음병</option>
             <option>뿌리혹병, 무사마귀병</option>
             <option>세균성검은무늬병</option>
             <option>세균성시들음병</option>
             <option>시들음병</option>
             <option>잎마름병</option>
             <option>잘록병</option>
             <option>점균병</option>
             <option>탄저병</option>
             <option>흰녹가루병</option>
             <option>흰무늬병</option>
             <option>모자이크병</option> -->
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '무궁화'">
            <option disabled value="">병 명</option>
            <option>검은무늬병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '무화과'">
            <option disabled value="">병 명</option>
            <option>검은곰팡이병</option>
            <option>검은줄기썩음병(가칭)</option>
            <option>과실점무늬병</option>
            <option>더뎅이병</option>
            <option>역병</option>
            <option>잎자루마름병(가칭)</option>
            <option>잿빛곰팡이병</option>
            <option>점무늬병</option>
            <option>줄기마름병</option>
            <option>탄저병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '문주란'">
            <option disabled value="">병 명</option>
            <option>탄저병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '미나리'">
            <option disabled value="">병 명</option>
            <option>갈색무늬병</option>
            <option>균핵병</option>
            <option>녹병</option>
            <option>빗자루병</option>
            <option>뿌리썩음병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '밤'">
            <option disabled value="">병 명</option>
            <option>갈색고약병</option>
            <option>검은가지마름병</option>
            <option>그을음병</option>
            <option>둥근갈색무늬병</option>
            <option>부채버섯썩음병</option>
            <option>점무늬병</option>
            <option>줄기마름병</option>
            <option>탄저병</option>
            <option>흰가루병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '배'">
            <option disabled value="">병 명</option>
            <option>검은무늬병</option>
            <option>검은별무늬병</option>
            <option>겹무늬병</option>
            <option>과수화상병</option>
            <option>그을음병</option>
            <option>근두암종병</option>
            <!-- <option>뒷면흰가루병</option>
            <option>배갈색썩음병</option>
            <option>붉은가지마름병</option>
            <option>붉은별무늬병</option>
            <option>잎검은점병</option>
            <option>잿빛곰팡이병</option>
            <option>줄기마름병</option>
            <option>탄저병</option>
            <option>푸른곰팡이병</option>
            <option>화상병</option>
            <option>흰가루병</option>
            <option>흰날개무늬병</option>
            <option>흰별무늬병</option> -->
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '배추'">
            <option disabled value="">병 명</option>
            <option>검은무늬병</option>
            <option>검은썩음병</option>
            <option>균핵병</option>
            <option>그루썩음병</option>
            <option>노균병</option>
            <option>모자이크병</option>
            <!-- <option>무름병</option>
            <option>밑둥썩음병</option>
            <option>뿌리마름병</option>
            <option>뿌리혹병, 무사마귀병</option>
            <option>순무황화모자이크바이러스병</option>
            <option>시들음병</option>
            <option>역병</option>
            <option>잘록병</option>
            <option>점균병</option>
            <option>탄저병</option>
            <option>흰가루병</option>
            <option>흰무늬병</option> -->
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '백일홍'">
            <option disabled value="">병 명</option>
            <option>검은무늬병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '백합(나리)'">
            <option disabled value="">병 명</option>
            <option>모자이크병</option>
            <option>잎마름병</option>
            <option>줄기썩음병</option>
            <option>탄저병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '복숭아'">
            <option disabled value="">병 명</option>
            <option>검은별무늬병</option>
            <option>과일흰가루병</option>
            <option>그을음병</option>
            <option>세균성구멍병</option>
            <option>잎오갈병</option>
            <option>잎흰가루병</option>
            <option>자두곰보병</option>
            <option>잿빛곰팡이병</option>
            <option>잿빛무늬병</option>
            <option>줄기마름병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '봉숭아(봉선화)'">
            <option disabled value="">병 명</option>
            <option>겹무늬병</option>
            <option>모자이크병</option>
            <option>흰가루병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '부추'">
            <option disabled value="">병 명</option>
            <option>균핵병</option>
            <option>녹병</option>
            <option>시들음병</option>
            <option>잘록병</option>
            <option>흰잎마름병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '붓꽃'">
            <option disabled value="">병 명</option>
            <option>모자이크병</option>
            <option>잎마름병</option>
            <option>잿빛곰팡이병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '블루베리'">
            <option disabled value="">병 명</option>
            <option>가지마름병</option>
            <option>갈색무늬병</option>
            <option>그을음병</option>
            <option>블루베리붉은원형반점병</option>
            <option>잿빛곰팡이병</option>
            <option>줄기마름병</option>
            <option>탄저병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '비파'">
            <option disabled value="">병 명</option>
            <option>둥근점무늬병</option>
            <option>잿빛무늬병</option>
            <option>점무늬병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '사과'">
            <option disabled value="">병 명</option>
            <option>가지검은마름병</option>
            <option>갈색무늬병</option>
            <option>검은별무늬병</option>
            <option>겹무늬썩음병</option>
            <option>고두병</option>
            <option>고접병</option>
            <option>과수화상병</option>
            <option>과심곰팡이병</option>
            <option>그을음병</option>
            <option>그을음점무늬병</option>
            <!-- <option>금두암종병</option>
            <option>모자이크병</option>
            <option>바이러스 잎반점병</option>
            <option>바이로이드병</option>
            <option>붉은별무늬병</option>
            <option>뿌리혹병</option>
            <option>사과모자이크바이러스병</option>
            <option>역병</option>
            <option>열매검은병, 열매점무늬병</option>
            <option>은엽병</option>
            <option>자색점무늬병</option>
            <option>자주날개무늬병</option>
            <option>잿빛곰팡이병</option>
            <option>잿빛무늬병</option>
            <option>점무늬낙엽병</option>
            <option>줄기마름병</option>
            <option>축과병</option>
            <option>탄저병</option>
            <option>푸른곰팡이병</option>
            <option>흰가루병</option>
            <option>흰날개무늬병</option>
            <option>흰무늬병</option>
            <option>흰비단병</option>
            <option>부란병</option> -->
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '산수유'">
            <option disabled value="">병 명</option>
            <option>산슈유열매탄저병</option>
            <option>산수유잎반점병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '살구'">
            <option disabled value="">병 명</option>
            <option>갈색썩음병</option>
            <option>세균성구멍병</option>
            <option>잿빛무늬병</option>
            <option>흰가루병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '삽주'">
            <option disabled value="">병 명</option>
            <option>역병</option>
            <option>탄저병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '상추'">
            <option disabled value="">병 명</option>
            <option>갈색무늬병</option>
            <option>균핵병</option>
            <option>노균병</option>
            <option>모자이크병</option>
            <option>무름병</option>
            <option>밑둥썩음병</option>
            <option>뿌리썩음병</option>
            <option>시들음병</option>
            <option>역병</option>
            <option>잎썩음병</option>
            <!-- <option>잿빛곰팡이병</option> -->
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '샐러리'">
            <option disabled value="">병 명</option>
            <option>검은무늬병</option>
            <option>무름병</option>
            <option>잎마름병</option>
            <option>잿빛곰팡이병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '샐비어'">
            <option disabled value="">병 명</option>
            <option>탄저병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '생강'">
            <option disabled value="">병 명</option>
            <option>근경썩음병</option>
            <option>마른썩음병</option>
            <option>모자이크병</option>
            <option>잎집무늬마름병</option>
            <option>잎집썩음병</option>
            <option>흰별무늬병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '선인장'">
            <option disabled value="">병 명</option>
            <option>모자이크병</option>
            <option>밑둥썩음병</option>
            <option>줄기썩음병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '소철'">
            <option disabled value="">병 명</option>
            <option>점무늬병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '수국'">
            <option disabled value="">병 명</option>
            <option>잿빛곰팡이병</option>
            <option>점무늬병</option>
            <option>흰가루병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '수박'">
            <option disabled value="">병 명</option>
            <option>검은별무늬병</option>
            <option>검은점뿌리썩음병</option>
            <option>과실썩음병</option>
            <option>괴저반점바이러스병</option>
            <option>균핵병</option>
            <option>덩굴마름병</option>
            <option>덩굴쪼김병</option>
            <option>모자이크병</option>
            <option>얼룩모자이크병</option>
            <option>역병</option>
            <!-- <option>잎마름병</option>
            <option>잘록병</option>
            <option>잿빛곰팡이병</option>
            <option>점무늬병</option>
            <option>탄저병</option>
            <option>흰가루병</option> -->
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '순무'">
            <option disabled value="">병 명</option>
            <option>노균병</option>
            <option>모자이크병</option>
            <option>뿌리혹병, 무사마귀</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '쉐프렐라'">
            <option disabled value="">병 명</option>
            <option>탄저병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '스파티필럼'">
            <option disabled value="">병 명</option>
            <option>잿빛곰팡이병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '시금치'">
            <option disabled value="">병 명</option>
            <option>노균병</option>
            <option>누른위조병</option>
            <option>모자이크병</option>
            <option>시들음병</option>
            <option>역병</option>
            <option>잘록병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '시써스'">
            <option disabled value="">병 명</option>
            <option>점무늬병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '식나무'">
            <option disabled value="">병 명</option>
            <option>잿빛곰팡이병</option>
            <option>점무늬병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '심비디움'">
            <option disabled value="">병 명</option>
            <option>검은잎마름병</option>
            <option>괴저점무늬병</option>
            <option>무름병</option>
            <option>심비디움모자익바이러스</option>
            <option>점무늬병</option>
            <option>줄기썩음병</option>
            <option>탄저병</option>
            <option>흰비단병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '쑥갓'">
            <option disabled value="">병 명</option>
             <option>균핵병</option>
             <option>모자이크병</option>
             <option>잘록병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '아레카야자'">
            <option disabled value="">병 명</option>
             <option>탄저병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '아마릴리스'">
            <option disabled value="">병 명</option>
             <option>모자이크병</option>
             <option>붉은무늬병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '아스파라가스'">
            <option disabled value="">병 명</option>
             <option>시들음병</option>
             <option>잿빛곰팡이병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '아스파라거스'">
            <option disabled value="">병 명</option>
             <option>검은무늬병</option>
             <option>줄기썩음병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '아욱'">
            <option disabled value="">병 명</option>
             <option>균핵병</option>
             <option>잘록병</option>
             <option>탄저병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '아이비(헤데라)'">
            <option disabled value="">병 명</option>
             <option>잿빛곰팡이병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '안개꽃'">
            <option disabled value="">병 명</option>
             <option>시들음병</option>
             <option>잿빛곰팡이병</option>
             <option>흰가루병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '앵두'">
            <option disabled value="">병 명</option>
             <option>갈색무늬병</option>
             <option>부채버섯썩음병</option>
             <option>세균성구멍병</option>
             <option>잿빛곰팡이병</option>
             <option>줄기썩음병</option>
             <option>탄저병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '양배추'">
            <option disabled value="">병 명</option>
             <option>검은무늬병</option>
             <option>검은뿌리썩음병</option>
             <option>검은썩음병</option>
             <option>균핵병</option>
             <option>무름병</option>
             <option>뿌리썩음병</option>
             <!-- <option>뿌리혹병, 무사마귀</option>
             <option>시들음병</option>
             <option>잎썩음병</option> -->
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '양파'">
            <option disabled value="">병 명</option>
             <option>검은무늬병</option>
             <option>검은점무늬마름병</option>
             <option>깜부기병</option>
             <option>노균병</option>
             <option>누른오갈병</option>
             <option>무름병</option>
             <option>세균썩음병</option>
             <option>시들음병</option>
             <option>잎마름병</option>
             <option>잘록병</option>
             <!-- <option>잿빛곰팡이병</option>
             <option>쿠키병2</option>
             <option>푸른곰팡이병</option>
             <option>흑색썩음균핵병</option> -->
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '오미자'">
            <option disabled value="">병 명</option>
             <option>고약병</option>
             <option>점무늬병</option>
             <option>푸른곰팡이병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '오이'">
            <option disabled value="">병 명</option>
             <option>검은별무늬병</option>
             <option>균핵병</option>
             <option>노균병</option>
             <option>덩굴마름병</option>
             <option>덩굴쪼김병</option>
             <option>모자이크병</option>
             <option>세균성모무늬병</option>
             <option>세균성시들음병</option>
             <option>얼룩(綠斑)모자이크병</option>
             <option>역병</option>
             <!-- <option>잘록병</option>
             <option>잿빛곰팡이병</option>
             <option>탄저병</option>
             <option>흰가루병</option> -->
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '옥수수'">
            <option disabled value="">병 명</option>
             <option>검은줄오갈병</option>
             <option>깜부기병</option>
             <option>깨씨무늬병</option>
             <option>모잘록병</option>
             <option>뿌리썩음병</option>
             <option>이삭썩음병</option>
             <option>잎집무늬마름병</option>
             <option>줄기썩음병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '우엉'">
            <option disabled value="">병 명</option>
             <option>뿌리썩음병</option>
             <option>흰가루병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '유자'">
            <option disabled value="">병 명</option>
             <option>갈색줄무늬오갈병</option>
             <option>검은점무늬병</option>
             <option>얼룩무늬병</option>
             <option>탄저병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '자두'">
            <option disabled value="">병 명</option>
             <option>갈색고약병</option>
             <option>검은점무늬병</option>
             <option>궤양병</option>
             <option>세균성구멍병</option>
             <option>자두곰보병</option>
             <option>잿빛곰팡이병</option>
             <option>잿빛무늬병</option>
             <option>주머니병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '작약'">
            <option disabled value="">병 명</option>
             <option>검은무늬병</option>
             <option>녹병</option>
             <option>잿빛곰팡이병</option>
             <option>점무늬병</option>
             <option>탄저병</option>
             <option>흰가루병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '장미'">
            <option disabled value="">병 명</option>
             <option>가지마름병</option>
             <option>검은무늬병</option>
             <option>노균병</option>
             <option>잿빛곰팡이병</option>
             <option>탄저병</option>
             <option>흰가루병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '제라늄'">
            <option disabled value="">병 명</option>
             <option>갈색무늬병</option>
             <option>잿빛곰팡이병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '종려죽'">
            <option disabled value="">병 명</option>
             <option>점무늬병</option>
             <option>탄저병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '지치'">
            <option disabled value="">병 명</option>
             <option>역병</option>
             <option>점무늬병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '지황'">
            <option disabled value="">병 명</option>
             <option>뿌리썩음병</option>
             <option>점무늬병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '진달래'">
            <option disabled value="">병 명</option>
             <option>잿빛점무늬병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '참다래(키위,다래)'">
            <option disabled value="">병 명</option>
             <option>갈색고약병</option>
             <option>갈색점무늬병</option>
             <option>과실무름병</option>
             <option>궤양병</option>
             <option>붉은줄기마름병</option>
             <option>잿빛곰팡이병</option>
             <option>점무늬병</option>
             <option>줄기썩음병</option>
             <option>탄저병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '참당귀(당귀)'">
            <option disabled value="">병 명</option>
             <option>점무늬병</option>
             <option>줄기썩음병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '참외'">
            <option disabled value="">병 명</option>
             <option>검은별무늬병</option>
             <option>균핵병</option>
             <option>노균병</option>
             <option>덩굴마름병</option>
             <option>덩굴쪼김병</option>
             <option>모자이크병</option>
             <option>뿌리썩음병</option>
             <option>얼룩모자이크병</option>
             <option>역병</option>
             <option>잘록병</option>
             <!-- <option>탄저병</option>
             <option>흰가루병</option>
             <option>역병</option> -->
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '천궁'">
            <option disabled value="">병 명</option>
             <option>뿌리썩음병</option>
             <option>잎마름병</option>
             <option>흰가루병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '천일홍'">
            <option disabled value="">병 명</option>
             <option>잘록병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '치자나무'">
            <option disabled value="">병 명</option>
             <option>잿빛곰팡이병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '카네이션'">
            <option disabled value="">병 명</option>
             <option>검은무늬병</option>
             <option>녹병</option>
             <option>모자이크병</option>
             <option>반점세균병</option>
             <option>시들음병</option>
             <option>잿빛곰팡이병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '칸나'">
            <option disabled value="">병 명</option>
             <option>모자이크병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '케일'">
            <option disabled value="">병 명</option>
             <option>균핵병</option>
             <option>뿌리혹병, 무사마귀병</option>
             <option>세균성점무늬병</option>
             <option></option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '켄차야자'">
            <option disabled value="">병 명</option>
             <option>탄저병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '콩'">
            <option disabled value="">병 명</option>
             <option>검은뿌리썩음병</option>
             <option>괴저모자이크병</option>
             <option>균핵병</option>
             <option>노균병</option>
             <option>모자이크병</option>
             <option>모잘록병</option>
             <option>미이라병</option>
             <option>불마름병</option>
             <option>새삼</option>
             <option>세균성점무늬병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '클레로덴드럼'">
            <option disabled value="">병 명</option>
             <option>탄저병</option>
             <option>괴저모자이크병</option>
             <option>균핵병</option>
             <option>노균병</option>
             <option>모자이크병</option>
             <option>모잘록병</option>
             <option>미이라병</option>
             <option>불마름병</option>
             <option>새삼</option>
             <option>세균성점무늬병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '클레로덴드럼'">
            <option disabled value="">병 명</option>
             <option>탄저병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '토마토'">
            <option disabled value="">병 명</option>
             <option>검은점뿌리썩음병</option>
             <option>겹무늬병</option>
             <option>궤양병</option>
             <option>균핵병</option>
             <option>덤불위축바이러스</option>
             <option>모자이크병</option>
             <option>반점위조바이러스</option>
             <option>뿌리역병</option>
             <option>시들음병</option>
             <option>잎곰팡이병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '파슬리'">
            <option disabled value="">병 명</option>
             <option>무름병</option>
             <option>시들음병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '팔손이'">
            <option disabled value="">병 명</option>
             <option>더뎅이병</option>
             <option>잿빛곰팡이병</option>
             <option>탄저병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '패랭이꽃'">
            <option disabled value="">병 명</option>
             <option>시들음병</option>
             <option>잿빛곰팡이병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '팬지'">
            <option disabled value="">병 명</option>
             <option>잿빛곰팡이병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '페튜니아'">
            <option disabled value="">병 명</option>
             <option>모자이크병</option>
             <option>잿빛곰팡이병</option>
             <option>점무늬병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '포도'">
            <option disabled value="">병 명</option>
             <option>갈색무늬병</option>
             <option>그을음점무늬병</option>
             <option>근두암종병</option>
             <option>꼭지마름병</option>
             <option>노균병</option>
             <option>녹병</option>
             <option>덩굴쪼김병</option>
             <option>먼지곰팡이병</option>
             <option>부채버섯썩음병</option>
             <option>붉은가지마름병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '피닉스야자'">
            <option disabled value="">병 명</option>
             <option>점무늬병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '해바라기'">
            <option disabled value="">병 명</option>
             <option>검은무늬병</option>
             <option>녹병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '협죽도'">
            <option disabled value="">병 명</option>
             <option>잿빛곰팡이병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '호두나무'">
            <option disabled value="">병 명</option>
             <option>갈색고약병</option>
             <option>갈색무늬병</option>
             <option>갈색점무늬병</option>
             <option>검은가지마름병</option>
             <option>과실썩음병</option>
             <option>잿빛곰팡이병</option>
             <option>점무늬병</option>
             <option>줄기마름병</option>
             <option>줄기썩음병</option>
             <option>탄저병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '호박'">
            <option disabled value="">병 명</option>
             <option>검은별무늬병</option>
             <option>규리얼룩모자이크</option>
             <option>균핵병</option>
             <option>노균병</option>
             <option>노균병+D46</option>
             <option>누른모자이크병</option>
             <option>덩굴마름병</option>
             <option>덩굴쪼김병</option>
             <option>모자이크병</option>
             <option>뿌리썩음병</option>
        </select>
        <select v-model="selected2" v-else-if="`${selected}` === '황기'">
            <option disabled value="">병 명</option>
             <option>노균병</option>
             <option>뿌리썩음병</option>
             <option>뿌리썩음병</option>
             <option>흰가루병</option>
        </select>







        <button v-if="`${selected}` && `${selected2}`" @click="buginfo()">정보보기</button>
        <button v-else disabled>선택</button>
    
    </div>
    
   <div>
    <div class="hovereffect">
        <img class="img-responsive"  v-bind:src="`${buglist.이미지}`" alt="">
            <div class="overlay">
                <h2></h2>
            <h2>
                    <button type="button" class="btn btn-info" data-toggle="modal" data-target="#exampleModal">자세히</button>
                </h2>
            </div>
    </div>
    </div>
    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
        <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">식물명:{{buglist.작물명}}</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
            </button>
        </div>
        <div class="modal-body">
            <h3>{{buglist.병명}}</h3>
            <img  v-bind:src="`${buglist.이미지}`" style="width:200px;" alt="">
        </div>
        <hr>
        <div class="modal-body">
            <h4>발생환경</h4>
            <div v-html="buglist.발생환경"></div>
        </div>
        <hr>
        <div class="modal-body">
            <h4>증상</h4>
            <div v-html="buglist.증상"></div>
        </div>
        <hr>
        <div class="modal-body">
            <h4>방제방법</h4>
            <div v-html="buglist.방제방법"></div>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        </div>
        </div>
    </div>
    </div>
</div>

</template>



<script>
import axios from 'axios';
export default {
  data() {
    return {
      buglist: [],
      selected: "",
      selected2: "",
          }
  },
  methods: {
    buginfo() {
        let formData = new FormData();
        formData.append('selected', this.selected)
        formData.append('selected2', this.selected2)
        axios.get('http://127.0.0.1:8000/api/buginfo/', {
            params:{
                'selected': this.selected,
                'selected2': this.selected2
            }
        }
        )
        .then( response => {
                    this.buglist = response.data,
                    this.buglist.발생환경 = this.buglist.발생환경.split('\n').join('<br />')
                    this.buglist.방제방법 = this.buglist.방제방법.split('\n').join('<br />')
                    this.buglist.증상 = this.buglist.증상.split('\n').join('<br />')
        })
        .catch( err => {
                    console.log(err)
      });
    }
  },
}

</script>




<style>
.hovereffect {
  width: 100%;
  height: 100%;
  float: left;
  overflow: hidden;
  position: relative;
  text-align: center;
  cursor: default;
}

.hovereffect .overlay {
  position: absolute;
  overflow: hidden;
  width: 80%;
  height: 80%;
  left: 10%;
  top: 10%;
  border-bottom: 2px solid white;
  border-top: 2px solid white;
  -webkit-transition: opacity 0.35s, -webkit-transform 0.35s;
  transition: opacity 0.35s, transform 0.35s;
  -webkit-transform: scale(0,1);
  -ms-transform: scale(0,1);
  transform: scale(0,1);
}

.hovereffect:hover .overlay {
  opacity: 1;
  filter: alpha(opacity=100);
  -webkit-transform: scale(1);
  -ms-transform: scale(1);
  transform: scale(1);
}

.hovereffect img {
  display: block;
  position: relative;
  -webkit-transition: all 0.35s;
  transition: all 0.35s;
  width: 400px;
}

.hovereffect h2 {
  text-transform: uppercase;
  text-align: center;
  position: relative;
  font-size: 17px;
  background-color: transparent;
  color: black;
  padding: 1em 0;
  opacity: 0;
  filter: alpha(opacity=0);
  -webkit-transition: opacity 0.35s, -webkit-transform 0.35s;
  transition: opacity 0.35s, transform 0.35s;
  -webkit-transform: translate3d(0,-100%,0);
  transform: translate3d(0,-100%,0);
}

.hovereffect a, .hovereffect p {
  color: #FFF;
  padding: 1em 0;
  opacity: 0;
  filter: alpha(opacity=0);
  -webkit-transition: opacity 0.35s, -webkit-transform 0.35s;
  transition: opacity 0.35s, transform 0.35s;
  -webkit-transform: translate3d(0,100%,0);
  transform: translate3d(0,100%,0);
}

.hovereffect:hover a, .hovereffect:hover p, .hovereffect:hover h2 {
  opacity: 1;
  filter: alpha(opacity=100);
  -webkit-transform: translate3d(0,0,0);
  transform: translate3d(0,0,0);
}
</style>