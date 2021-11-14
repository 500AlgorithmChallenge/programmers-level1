public class hsh_86051 {
    public int solution(int[] numbers) {
        /*
        0부터 9까지 숫자 중 일부가 들어있는 배열 numbers가 매개변수
        * numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return
        *
        * 1. numbers 길이만큼 반복
        * 2. 0부터 9까지 들어있는 배열 tmp와 비교
        * 3. 숫자가 tmp에도 존재하면 삭제
        * 4. tmp에 남아있는 숫자 answer에 더해주기
        */
        int answer = 0;
        int[] tmp = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}; // numbers와 비교해서 없는 수를 남길 배열
        for(int i: numbers){ // numbers의 크기만큼 반복
            for(int j = 0; j < tmp.length; j++){ // tmp의 크기만큼 반복
                if(i == tmp[j]){ // numbers와 tmp 모두 가지고 있는 수라면
                    tmp[j] = 0; // tmp에서 삭제
                }
            }
        }
        for(int k = 0; k < tmp.length; k++){ // tmp의 크기만큼 반복
            answer += tmp[k]; // answer에 tmp에 남아있는 수를 더해준다
        }
        return answer;
    }
}
