import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in); 
		int N = sc.nextInt(); 					// 입력받는 단어 개수 N
		
		String[] arr = new String[N];			// N 크기 만큼 Stringp[] 초기화
		
		for(int i = 0; i < N; i++) {
			arr[i] = sc.next();					// 단어 입력 받기
		}	
        
		String ans = "";
		for(int i = 0; i < arr[0].length(); i++) { // 문장의 길이 만큼 순환
        
			Boolean flag = true;				// 단어일치여부를 판단하는 flag
            
			for(int j = 1; j < arr.length; j++) {	// 문장 개수 만큼 순환
            
            	// 한번에 비교할 자신이 없어서 2문장씩 글자를 비교하였음
				String tmp1 = String.valueOf(arr[j-1].charAt(i));
				String tmp2 = String.valueOf(arr[j].charAt(i));

				if(!tmp1.equals(tmp2)  ) { // 다르다면 flag 바꾸기
					flag = false;
                    break;
				}
			}
			if(flag) {
				ans += String.valueOf(arr[0].charAt(i));
			}else {
				ans += "?";
			}
		}
		System.out.println(ans);
	}

}