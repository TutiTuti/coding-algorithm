import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		String[] arr = new String[N];
		
		for(int i = 0; i < N; i++) {
			arr[i] = sc.next();
		}
		String ans = "";
		for(int i = 0; i < arr[0].length(); i++) {
			Boolean flag = true;
			for(int j = 1; j < arr.length; j++) {
				String tmp1 = String.valueOf(arr[j-1].charAt(i));
				String tmp2 = String.valueOf(arr[j].charAt(i));

				if(!tmp1.equals(tmp2)  ) {
					flag = false;
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
