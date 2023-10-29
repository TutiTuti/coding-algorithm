class Solution {
    public int[] solution(String[] wallpaper) {
        
        int lr = 50, lc = 50, rr= 0, rc = 0;
        for (int i = 0; i < wallpaper.length; i++){
            for (int j = 0; j < wallpaper[i].length(); j++){
                if(wallpaper[i].charAt(j) =='#'){
                    if(lr > i){lr = i;};
                    if(lc > j){lc = j;};
                    if(rr < i){rr = i;};
                    if(rc < j){rc = j;};
                }
            };
        };

       
        int[] answer = {lr, lc, rr + 1, rc + 1};
        return answer;
    }
}