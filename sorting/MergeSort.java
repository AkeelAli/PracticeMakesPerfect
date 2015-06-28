import java.util.List;
import java.util.ArrayList;

public class MergeSort {

    public static List<Integer> mergeSort (List<Integer> list) {
	
        if (list == null || list.size() < 2) {
            return list;
        }

        int mid = (list.size() / 2);
        
        List<Integer> left = mergeSort(list.subList(0, mid));
        List<Integer> right = mergeSort(list.subList(mid, list.size()));

        return merge(left, right);
    } 

    private static List<Integer> merge (List<Integer> left, List<Integer> right) {

	ArrayList<Integer> merged = new ArrayList<Integer>();

        int j = 0;
	int k = 0;

        while (j < left.size() && k < right.size()) {
            if (left.get(j) < right.get(k)) 
                merged.add(left.get(j++));
            else 
                merged.add(right.get(k++));
        }

        if (j < left.size())
            merged.add(left.get(j++));

	if (k < right.size())	
            merged.add(right.get(k++));

        return merged;
    }
}
