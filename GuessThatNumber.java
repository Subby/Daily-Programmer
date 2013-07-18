//Easy Challenge #115 (http://www.reddit.com/r/dailyprogrammer/comments/15ul7q/122013_challenge_115_easy_guessthatnumber_game/)
import java.util.Scanner;
public class GuessThatNumber {
	public static void main(String args[]) {
		int number = (int) Math.floor((Math.random() * 100 + 1));
		boolean active = true;
		Scanner input = new Scanner(System.in);
		System.out.println("Hey! Guess a number between 1 and 100!");
		/*
		 * Uncomment the line below to reveal the number at runtime.
		 */
		//System.out.println("[DEBUG]: The number is " + number);
		while(active) {
			int guess = input.nextInt();
			if (guess < number) {
				System.out.println("Wrong. That number is below my number.");
			}
			else if (guess > number) {
				System.out.println("Wrong. That number is above my number.");
			} 
			else if (guess == number) {
				System.out.println("Correct! That is my number, you win!");
				active = false;
			}
		}
	}
}
