import java.util.ArrayList;

public class Main {

	public static void main(String args[]) {
		ArrayList<Integer> list = new ArrayList<Integer>();

		list.add(5);
		list.add(3);
		list.add(10);
		list.add(-1);
		list.add(20);
		list.add(7);

		System.out.println(MergeSort.mergeSort(list));
	}
}
