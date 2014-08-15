//6枚のカードの並べ方を求めて！ https://codeiq.jp/ace/chocolate_bar/q847
/* package whatever; // don't place package name! */
 
import java.util.*;
import java.lang.*;
import java.io.*;
 
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		int[] num = {5, 4, 3, 2, 1, 0};
		ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
 
		result.add(new ArrayList<Integer>());
 
		for (int i = 0; i < num.length; i++) {
			ArrayList<ArrayList<Integer>> current = new ArrayList<ArrayList<Integer>>();
 
			for (ArrayList<Integer> a : result) {
				for (int j = 0; j < a.size()+1; j++) {
					a.add(j, num[i]);
					ArrayList<Integer> temp = new ArrayList<Integer>(a);
					current.add(temp);
					a.remove(j);
				}
			}
			result = new ArrayList<ArrayList<Integer>>(current);
		}
		for (ArrayList<Integer> a : result) {
			for (Integer b : a) {
				System.out.print(b);
			}
			System.out.print('\n');
		}
	}
}
