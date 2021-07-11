/*
 * Solution to https://leetcode.com/problems/sort-colors/
 */

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int partition(vector<int>& nums, int l, int h, int p) {
        int pivot = nums[p];
        
        int i = l, target = l;
        while (i <= h) {
            if (nums[i] < pivot) {
                swap(nums[i], nums[target]);
                target++;
            }
            i++;
        }
        
        i = target = h;
        while (i >= l) {
            if (nums[i] < pivot) {
                break;  
            } else if (nums[i] > pivot) {
                swap(nums[i], nums[target]);
                target--;
            }
            i--;
        }
        
        return i+1;
    }
    
    void quicksort(vector<int>& nums, int l, int h) {
        if (l >= h) {
            return;
        }
        int pivot_index = l;
        //printVec(nums);
        //cout << "pivot: " << nums[pivot_index] << " at location: " << pivot_index << endl;
        pivot_index = partition(nums, l, h, pivot_index);
        //printVec(nums);
        //cout << "new location: " << pivot_index << endl;
        
        quicksort(nums, l, pivot_index-1);
        quicksort(nums, pivot_index+1, h);
    }
    
    void printVec(vector<int>& nums) {
        for (auto i : nums) {
            cout << i << ' ';
        }
        cout << endl;
    }

    void sortColors(vector<int>& nums) {
        //printVec(nums);
        quicksort(nums, 0, nums.size()-1);
        //printVec(nums);
    }
};


int main(void) {
    Solution s;

    vector<int> v = {23, 4, 6, 2, 98, 45, 98};

    s.sortColors(v);

    s.printVec(v);
}
