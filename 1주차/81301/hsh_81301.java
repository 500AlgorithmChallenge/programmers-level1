//public class hsh_81301 {
//    public int solution(String s){
//        /*자릿수의 일부가 영단어로 바뀐 문자열에서 원래 숫자 찾기
//        * 자릿수의 일부가 영단어로 바뀌었거나 그대로인 문자열 s를 매개변수로 가짐
//        * 1. s의 길이만큼 반복문
//        * 2. 중첩반복문으로 영어문자열 자르기
//        * 3. 'zero', 'one'...과 비교해서 맞으면 tmp 문자열에 넣어주기
//        * 4. 마지막에 숫자로 변환
//        * */
//        int answer = 0; // 출력해야 하는 수
//
//        for(int i = 0; i < s.length(); i++){ // 문자열 크기 만큼 반복
////            for(int j = 0; j < 3; j++){ // 1 ~ 9까지의 문자 크기가 5를 넘기지 않으므로 최대 5번 반복
////            }
//
//        }
//        return answer;
//    }
//}
public class hsh_81301 {
    public int solution(String s){
        int answer = 0;
        String[] num = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}; // 문자로된 숫자를 바꿔줄 숫자
        String[] word = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}; // 바꿔야 할 문자열
        System.out.println(s); // 문자열 s 출력
        for(int i = 0; i < num.length; i++){ // num의 길이만큼 반복(0~9)
            s = s.replace(word[i], num[i]); // s에 word[i]가 존재한다면 num[i]로 치환
        }
        answer = Integer.parseInt(s); // s를 정수형으로 변환

        return answer;
    }
}