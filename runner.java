import java.util.*;

public class runner {
	
	public static void run() {
		String[] input = input();
		String[][] grid = grid(input);
		String[][] smaller = condense(grid);
		int loc = Integer.valueOf(input[input.length - 1]) - 1;
		String[][] filled = fillSpots(smaller, loc);
		System.out.println(findChar(filled, loc));
		/* I originally wrote an additional algorithm to test runtime of this code.
		 * Average was 0.4 ms
		 * Runs significantly faster than the Python equivalent I wrote. 
		 * This could be because of Java being faster, or simply the fact that I've gotten better at coding over time.
		 */
	}
	
	public static String[] input() {
		//Taking input data and throwing it in a String Array
		Scanner input = new Scanner(System.in);
		System.out.println("Please input the necessary data.");
		return input.nextLine().split(", ");
	}
	
	public static String baseToString(String[][] base) {
		//Taking a Square double array and turning it into a readable string
		String ans = "";
		for(int i = 0; i < base.length; i++) {
			ans += "[";
			for(int j = 0; j < base[0].length; j++) {
				if(base[i][j] == null) {
					ans += " ";
				}
				else {
					ans += base[i][j];
				}
			}
			ans += "]";
			if(i != base.length - 1) {
				ans += "\n";
			}
		}
		return ans;
	}
	
	public static String[][] grid(String[] input) {
		//Adding initial values based on input data.
		String[][] base = new String[6][6];
		for(int i = 0; i < 4; i++) {
			int x = Integer.valueOf(input[i]) - 1;
			base[x / 6][x % 6] = "X";
		}
		int reps = Integer.valueOf(input[4]);
		int loc = 0;
		String value = "";
		for(int j = 0; j < reps; j++) {
			loc = Integer.valueOf(input[2 * j + 6]) - 1;
			value = input[2 * j + 5];
			base[loc / 6][loc % 6] = value;
			base = add(base, loc, value);
		}
		return base;
	}
	
	public static String[][] add(String[][] base, int loc, String value) {
		//adds additional values to the original grid based on starting values
		//AS PER original project's instructions
		int direction;
		if(loc < 6) {
			direction = 6;
		}
		else if(loc > 30) {
			direction = -6;
		}
		else if(loc % 6 == 0) {
			direction = 1;
		}
		else {
			direction = -1;
		}
		for(int i = 0; i < 5; i++) {
			loc += direction;
			if(base[loc / 6][loc % 6] != "X") {
				base[loc / 6][loc % 6] = value;
				return base;
			}
		}
		return base;
	}
	
	public static String[][] condense(String[][] grid) {
		//Turning the original 6x6 into a 4x4
		//Helps remove unnecessary info for analysis
		String[][] smaller = new String[4][4];
		for(int i = 1; i < 5; i++) {
			for(int j = 1; j < 5; j++) {
				smaller[i - 1][j - 1] = grid[i][j];
			}
		}
		return smaller;
	}
	
	public static String[][] fillSpots(String[][] grid, int loc) {
		//fills in grid with data until necessary value is found
		while(grid[loc / 6 - 1][loc % 6 - 1] == null) {
			for(int i = 0; i < grid.length; i++) {
				for(int j = 0; j < grid[0].length; j++) {
					if(grid[i][j] == null) {
						grid[i][j] = fillSpot(grid, i, j);
					}
				}
			}
		}
		return grid;
		
	}
	
	public static String fillSpot(String[][] grid, int x, int y) {
		//Looks at a certain empty point and checks if its value can be found
		String key = "ABCX";
		for(int i = 0; i < grid.length; i++) {
			if(grid[i][y] != null) {
				key = key.replaceFirst(grid[i][y], "");
			}
			if(grid[x][i] != null) {
				key = key.replaceFirst(grid[x][i], "");
			}
			//Checks which values in "ABCX" are found in the point's row and column
		}
		if(key.length() == 1) {
			//if all values minus one are found in the associated row and column, the final value is the output
			return key;
		}
		return null;
	}
	
	public static String findChar(String[][] base, int loc) {
		//finds the value associated with the location, found in the last array spot
		return base[loc / 6 - 1][loc % 6 - 1];
	}
	
	public static void main(String[] args) {
		run();
	}
}
