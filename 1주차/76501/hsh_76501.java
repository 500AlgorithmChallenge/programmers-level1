public class hsh_76501 {
    public int solution(int[] absolutes, boolean[] signs){
        int answer = 0;
        for(int i = 0; i < absolutes.length; i++){ // absolute와 signs의 길이는 같으므로 absolute의 길이만큼 반복
            if(signs[i] == true){ // signs가 참(양수)이라면
                answer += absolutes[i]; // absolute를 그냥 answer에 더해준다
            }
            else if(signs[i] == false){ // 거짓(음수)이라면
                answer += (-1) * absolutes[i]; // absolute에 -1을 곱해서 더해준다
            }
        }
        return answer;
    }
}
