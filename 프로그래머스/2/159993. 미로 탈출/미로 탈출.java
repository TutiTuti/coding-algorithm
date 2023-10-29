import java.util.LinkedList;
import java.util.Queue;

class Solution {
    static String[][] MIRO; 
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0 , -1, 1};
    
    public int solution(String[] maps) {
        MIRO = new String[maps.length][maps[0].length()]; 
        int[] start = new int[2];
        int[] labor = new int[2];
        
        for(int i = 0; i < maps.length; i++){
            String[] tmp = maps[i].split("");
            for(int j = 0; j < tmp.length; j++){
                MIRO[i][j] = tmp[j];
                //S : 시작 지점
                //E : 출구
                //L : 레버
                if (MIRO[i][j].equals("S")) {
                    start = new int[]{i, j};
                };
                
                if (MIRO[i][j].equals("L")) {
                    labor= new int[]{i, j};
                };
                
            }
        }
        for(int k = 0; k < MIRO.length; k++){
            for(int w = 0; w<MIRO[0].length; w++){
                System.out.print(MIRO[k][w]);
            }
            System.out.println(' ');
            
        }
        
        int findLabor = bfs(start, "L");
        int findExit = bfs(labor, "E");
        System.out.println("cccccccccccccc");
        System.out.println(findLabor);
        System.out.println(findExit);
        int ans = (findLabor == -1 | findExit == -1)? -1 : (findLabor + findExit);
        return ans;
    }
    
    
    public int bfs(int[] loc, String target){
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{loc[0], loc[1], 0});
        
        boolean[][] vstd = new boolean[MIRO.length][MIRO[0].length];
        System.out.println("갑니다!!!!!");
        while (!queue.isEmpty()) {
            System.out.println(queue.size());
            int r = queue.peek()[0];
            int c = queue.peek()[1];
            int m = queue.peek()[2];
            vstd[r][c] = true;
            
            if (MIRO[r][c].equals(target)){
                System.out.println("goal" + r+ ' ' + c + target + ' ' + MIRO[r][c]);
                return m;
            }
            
            queue.poll();
            
            for(int i = 0; i < 4; i++){
                int nr = r + dr[i];
                int nc = c + dc[i];
                
                if(nr >= 0 && nr < MIRO.length && nc >= 0 && nc < MIRO[0].length && !vstd[nr][nc]) {
                    if(!MIRO[nr][nc].equals("X")) {
                        vstd[nr][nc] = true;
                        queue.add(new int[]{nr, nc, m + 1});
                    }
                }
                
            }
        }
        return -1;
    }
}